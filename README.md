# Problem Set 9

### Due Wednesday November 23 @ 11:59pm EST

As always, you will submit to Canvas **a single .zip file**. Detailed instructions for what the .zip file should contain are at the end of this problem set. 

Download this whole directory to your desktop, unzip it, and carry out the tasks described below.


---

## Part 1: Debugging
For this part of the problem set, find `ps7-buggy.py` in the `ps7` folder within this folder. I took my solution for ps7, and I introduced one bug in each of the 5 image functions (`colorswitch()`, `fliphorizontal()`, `greyscale()`, `monochrome()`, `upsidedown()`). Your goal will be to test the program in order to identify these 5 bugs, determine what is causing them, and fix them in your version of the program.

In 4 of the 5 functions, the bug causes the whole program to crash. You will have to look at the stack trace and the code to identify and repair the bug.

In the remaining function, the bug will not cause the program to crash. Instead, it will edit the image in an unintended way.

Here is what you need to do:

1. Create a document using a text editor, Word, Google Docs, latex, or your preferred document creation software.

2. In the document, for each of the 5 functions (`colorswitch()`, `fliphorizontal()`, `greyscale()`, `monochrome()`, `upsidedown()`), provide the following information in plain English, using the sample below as a guide. Points will be taken off if we can't understand what you are talking about. Please use complete sentences.

* Copy the error from the stack trace (if it's one of the bugs that crashes the program) or describe the problem (if it's the bug that just has an unintended effect on the image).
* Copy the line of code that triggered the error (i.e., the one in the stack trace or the one that messes up the output).
* If there is a line earlier in the code that is actually causing the problem, also reproduce that line.
* Describe a few sentences what the bug is and how someone might have made that mistake.
* Describe how you would fix the error. 

3. In the code of the program, fix the error.

For instance, if you were given this code

```
a = 2
b = "pac"
c = a + b
```

I'd want to see something like this:

* The error from the stacktrace was  `TypeError: unsupported operand type(s) for +: 'int' and 'str'`.
* The line that triggered this error was this one: `c = a + b`
* Either of the first two lines is the problem since that's where these variables were created.
* The problem is that the code tried to add a string to an integer, which is not possible. 
* I'd fix this by having `a = "2"` so that I could concatenate the two variables together as a string to make "2pac".

And then you would fix the error in the code as you describe in your document.

---

## Part 2: Recursion
In class, I demonstrated recursion by rewriting some of our favorite old functions recursively. In part 2, you will write a recursive version of random search. I've given you some starter code in `recursive-search.py`, which includes recursive versions of sequential search and binary search, as well as a main method that calls all three functions.

If the number to be guessed is 14, I will expect to see this output after running the `main()` function. Of course, the number of guesses for random search will vary because it guesses randomly. :)

```
Pick a number between 1 and 100: 14
Sequential search guessed the number 14 in 14 guesses
Binary search  guessed the number 14 in 5 guesses
Random search guessed the number 14 in 76 guesses
```

---
## What to submit 

Create a folder containing these files: 
1. The document with the description of each bug, as described in part 1.
2. Your version of `ps7-buggy.py` with all five bug fixed, as described in part 1.
3. Your version of `recursive-search.py` with a recurisve implementation of random search.

Zip the file up, and submit the `.zip` file to Canvas. You do not need to include any other files.

### Due Wednesday November 23 @ 11:59pm EST



