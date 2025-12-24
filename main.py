import os
import sys
from pathlib import Path

def getDirectory() -> Path:
    # Check if there is an argument supplied, if not then set default directory to current
    if len(sys.argv) < 2:
        return Path(".")
    else:
        return Path(sys.argv[1]) # directory is the first argument

"""
def displayDirectory(startingDirectory: list[str]) -> None:
    # for each entry, check if is a file. if so just print it on a new line, if not then it's a subfolder, if it is a subfolder, then we want to go through each element in the subfolder 
    depth: int = 0 # how deep in a subdirectory we are 
    indentation: str = " " # how indentation looks, for example "-", will likely replace this with a funcction that does it smartly, but for now this is fine 
    i: int = 0 # index through directory 
    directory: list[str] = startingDirectory # directory we are currently traversing 
    directoryStack: list[tuple[str, int]] = [] # each directory in the stack is paired with how far it has been explored so far (index i)

    while True:
        entry = directory[i] # current entry being viewed
        if sys.

"""


def main():
    directory: Path = getDirectory()

    for entry in directory.iterdir():
        print(entry)

    # plan is, for each directory, we want to print it nicely, but if it's a file we just print it, but if it is a sub folder we do something different

    # maybe if we want a command line argument --layers=x, where x is an integer >= 1, then we could allow people to choose how many layers deep. 
    # we could either use a depth first algorithm or a breadth first algorithm. the depth would be the easiest, but would make making layers harder, as we would
    # have to keep track of the number of layers deep we are and then stop going deeper if it's too many layers deep. with a breadth first, we could just do
    # x passes through the dir, each time expanding the folders. tho i think this is less efficient so i'm going to try the depth first (since the directory can be displayed as a graph, it might be an in order traversal but who cares). 

    """
    depth = 0 # starting depth, how deep in the directory we are. this matters sinsce the subfolders and printed with larger indentation
    indentation = " " # change the indentation if needed, could be done with a function
    traversing = True
    i: int = 0
    directory = the directory we are traversing
    directoryStack # when entering a subfolder, push the current directory to the stack to get back to it. we would also have to store it with it's current progress through the subfolder, which would be `i`. probably a tuple
    while traversing:
        entry = directory[i] # intially, get the first dirctory, might be beneficial to check if is a subfolder, whether or not it is empty, if it's empty just treat it like a file (different symbol tho so would need a different case)
        if isFile:
            print(indentation * depth + " " + entry.name)
        elif is subfolder and is empty:
            print(indentation * depth + " " + entry.name) # different statement with same code in case i want to add a separate symbol for folders

        else: # is a dir that is not empty, so must go through it's contents too
            print(indentation * depth + " " + entry.name)
            directoryStack.push((directory, i)) # store the index with it
            directory = the directory we are on now
            depth += 1 # we are in another subfolder so increase the depth
            i = 0 # reset i to start from the start of the subdirectory

        if len(directory) > i + 1: # something like this, just wanting to check that increasing i won't lead to an index out of bounds error
            i += 1

        else: # we are at the end of the directory so move on 
            depth -= 1
            (directory, i) = directoryStack.pop()



    go through each element of a directory 
    if the element is a file, print the file with a given indentation based on it's subfolder depth
    if the element is a directory, then print the folder and now go through each element of this sub directory (do this with a stack)
    then once you have finished with the directory, pop off the element from the stack and keep going
            

    """


if __name__ == "__main__":
    main()
