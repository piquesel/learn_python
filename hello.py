import sys

def hello_world(arg):
    print("Hello World! {}".format(arg))

def main(arg):
    hello_world(arg)

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        main("Bruno")
