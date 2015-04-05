#!/usr/bin/env python3

"""Retrieve and print words from a URL.

Usage:

    python3 words.py <URL>
"""

from urllib.request import urlopen
import sys


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        print(story_words)
    return story_words


def print_words(story_words):
    """Print items one per line.

    Args:
        An iterable series of printable items.
    """
    for word in story_words:
        print(word)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_words(words)

print(__name__)

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        main("http://sixty-north.com/c/t.txt")