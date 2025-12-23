import os
import sys

def getDirectory() -> str:
    # Check if there is an argument supplied, if not then set default directory to current
    if len(sys.argv) < 2:
        return "."
    else:
        return sys.argv[1] # directory is the first argument

def main():
    directory: str = getDirectory()

    print(os.listdir(directory))


if __name__ == "__main__":
    main()
