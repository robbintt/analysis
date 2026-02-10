#!/usr/bin/env python3
"""
Index YAML frontmatter from research analysis markdown files into SQLite.

Skips files already indexed (by filename). Handles the v2 frontmatter schema:
  ver, title, arxiv_id, source_url, tags (list), core_contribution

Usage:
  python scripts/index_frontmatter.py [directory] [--db path/to/db.sqlite]

Defaults:
  directory: ml_research_analysis
  db: analysis_outputs/research_index.sqlite
"""

import argparse
import json
import os
import sqlite3
import sys
from pathlib import Path


DB_DEFAULT = "analysis_outputs/research_index.sqlite"
DIR_DEFAULT = "ml_research_analysis"


def init_db(conn: sqlite3.Connection):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            filename    TEXT PRIMARY KEY,
            ver         TEXT,
            title       TEXT,
            arxiv_id    TEXT,
            source_url  TEXT,
            tags        TEXT,
            core_contribution TEXT,
            indexed_at  TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_arxiv_id ON papers(arxiv_id)
    """)
    conn.commit()


def get_existing(conn: sqlite3.Connection) -> set:
    rows = conn.execute("SELECT filename FROM papers").fetchall()
    return {r[0] for r in rows}


def extract_frontmatter(filepath: str) -> dict | None:
    """Fast YAML frontmatter extraction without importing PyYAML.

    Parses the small subset of YAML we actually see in these files:
    scalar fields and one list (tags). Handles multi-line quoted strings.
    Falls back to PyYAML if available and fast parse fails.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            first_line = f.readline().rstrip()
            if first_line != "---":
                return None
            lines = []
            for line in f:
                if line.rstrip() == "---":
                    break
                lines.append(line.rstrip("\n"))
            else:
                # Never hit closing ---, malformed
                return None
    except Exception:
        return None

    if not lines:
        return None

    # Try PyYAML first (most reliable)
    try:
        import yaml
        raw = "\n".join(lines)
        data = yaml.safe_load(raw)
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    # Fallback: simple key-value parse
    result = {}
    current_key = None
    current_val_lines = []
    in_list = False
    list_items = []

    def flush():
        nonlocal current_key, current_val_lines, in_list, list_items
        if current_key is None:
            return
        if in_list:
            result[current_key] = list_items
        else:
            val = " ".join(current_val_lines).strip()
            # Strip surrounding quotes
            if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
                val = val[1:-1]
            result[current_key] = val
        current_key = None
        current_val_lines = []
        in_list = False
        list_items = []

    for line in lines:
        # New key?
        if not line.startswith(" ") and not line.startswith("-") and ":" in line:
            flush()
            key, _, val = line.partition(":")
            current_key = key.strip()
            val = val.strip()
            if val == "":
                # Could be a list or multi-line string coming
                pass
            else:
                current_val_lines.append(val)
        elif line.startswith("- ") and current_key:
            in_list = True
            list_items.append(line[2:].strip())
        elif current_key:
            # Continuation line
            current_val_lines.append(line.strip())

    flush()
    return result if result else None


def index_directory(dirpath: str, db_path: str):
    os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    conn = sqlite3.connect(db_path)
    init_db(conn)

    existing = get_existing(conn)
    md_files = sorted(
        f for f in os.listdir(dirpath)
        if f.endswith(".md") and os.path.isfile(os.path.join(dirpath, f))
    )

    new_files = [f for f in md_files if f not in existing]
    if not new_files:
        print(f"All {len(md_files)} files already indexed.")
        conn.close()
        return

    print(f"Found {len(md_files)} .md files, {len(existing)} already indexed, {len(new_files)} to process.")

    inserted = 0
    errors = 0
    batch = []

    for fname in new_files:
        fpath = os.path.join(dirpath, fname)
        fm = extract_frontmatter(fpath)
        if fm is None:
            errors += 1
            continue

        tags = fm.get("tags", [])
        if isinstance(tags, list):
            tags_json = json.dumps(tags)
        else:
            tags_json = json.dumps([str(tags)]) if tags else "[]"

        batch.append((
            fname,
            str(fm.get("ver", "")),
            str(fm.get("title", "")),
            str(fm.get("arxiv_id", "")),
            str(fm.get("source_url", "")),
            tags_json,
            str(fm.get("core_contribution", "")),
        ))

        if len(batch) >= 500:
            conn.executemany(
                "INSERT OR IGNORE INTO papers (filename, ver, title, arxiv_id, source_url, tags, core_contribution) VALUES (?,?,?,?,?,?,?)",
                batch,
            )
            conn.commit()
            inserted += len(batch)
            batch = []

    if batch:
        conn.executemany(
            "INSERT OR IGNORE INTO papers (filename, ver, title, arxiv_id, source_url, tags, core_contribution) VALUES (?,?,?,?,?,?,?)",
            batch,
        )
        conn.commit()
        inserted += len(batch)

    total_in_db = conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
    conn.close()

    print(f"Done. Inserted {inserted}, errors {errors}, total in DB: {total_in_db}")


def main():
    parser = argparse.ArgumentParser(description="Index markdown frontmatter into SQLite")
    parser.add_argument("directory", nargs="?", default=DIR_DEFAULT, help=f"Directory to scan (default: {DIR_DEFAULT})")
    parser.add_argument("--db", default=DB_DEFAULT, help=f"SQLite database path (default: {DB_DEFAULT})")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a directory", file=sys.stderr)
        sys.exit(1)

    index_directory(args.directory, args.db)


if __name__ == "__main__":
    main()
