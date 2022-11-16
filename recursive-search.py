import random

# RECURSIVE SEQUENTIAL SEARCH
# Add one and call the function again until your guess is correct.
def sequentialsearch(target, guess):
    if target == guess:
        print("You guessed the number {} in {} guesses".format(target, guess))
        return
    sequentialsearch(target, guess+1)

# RECURSIVE BINARY SEARCH
def binarysearch(target, lo, hi, guesscount):
    # Get the middle number using lo and hi.
    mid = (hi+lo)//2

    # Add one to the number of guesses made so far.
    guesscount = guesscount + 1

    # If the middle number is right, return.
    if mid == target:
        print("You guessed the number {} in {} guesses".format(target, guesscount))
        return

    # If the middle number is too low, call the function again
    # but make lo = mid+1
    if mid < target:
        binarysearch(target, mid+1, hi, guesscount)

    # If the middle number is too high, call the function again
    # but make hi = mid-1
    else:
        binarysearch(target, lo, mid-1, guesscount)


# RECURSIVE RANDOM SEARCH

# Arguments are
#  * target: the number to be guessed
#  * guessed: a list of the numbers guessed so far

# The code should:
# * Guess a random number, making sure it's not already guessed.
# * If it's correct, return.
# * Otherwise, add the guessed number to guessed and call again.

def randomsearch(target, guessed):

    ### WRITE YOUR CODE HERE ###

    # delete this line below of course when you're done!
    print("The student has not yet written the code for this function")
    return
    

    
# main() method is already written for you
def main():
    numbertoguess = int(input("Pick a number between 1 and 100: "))
    sequentialsearch(numbertoguess, 1)
    binarysearch(numbertoguess, 0, 100, 0)
    randomsearch(numbertoguess, [])

main()
