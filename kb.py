#!/usr/bin/env python3

from collections import OrderedDict

from peewee import *

db = SqliteDatabase('kb_questions.db')


def create_questionnaire():
    """Create a questionnaire"""
    print("Let's create the questionnaire")
    pass


def view_questionnaire():
    """View the entries of the questionnaire"""
    print("Let's view the questionnaire")
    pass


def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()

menu = OrderedDict([
    ('1', create_questionnaire),
    ('2', view_questionnaire),
])


if __name__ == '__main__':
    menu_loop()
