#!usr/bin/env python3
from cli.menu import show_menu
from database.db import init_db, get_connection


def main():
    init_db()
    while True:
        show_menu()
        try:
            choice=int(input("Select an option: "))
        except ValueError:
            print("Invalid choice")
            continue
        if choice==0:
            print("Goodbye")
            break

        with get_connection() as conn:
            if choice==1:
                pass
            if choice==2:
                pass
            if choice==3:
                pass
            if choice==4:
                pass
            if choice==5:
                pass
            if choice==6:
                pass
