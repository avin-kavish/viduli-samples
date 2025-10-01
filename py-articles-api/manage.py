#!/usr/bin/env python3
"""
Management script for the Articles API.

Usage:
    python manage.py create_db    # Create database tables
    python manage.py --help       # Show help
"""

import argparse
import sys
from database import create_db_and_tables


def main():
    parser = argparse.ArgumentParser(
        description="Management script for Articles API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available commands:
  create_db    Create all database tables
        """,
    )

    parser.add_argument(
        "command",
        choices=["create_db"],
        help="Command to run",
    )

    args = parser.parse_args()

    if args.command == "create_db":
        try:
            create_db_and_tables()
            print("✅ Database tables created successfully!")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Error creating database tables: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
