# Exam Results

Write a program that lets a user enter their exam score, then tells the user if they have passed the exam. The user must score more than 70 to pass the exam.

## Steps

Following the comments,

1. Ask the user for the exam score. Store it in a variable.
2. Print `"You passed!"` if the score is > 70
3. Print `"Try again"` otherwise

Run the tests to see if your code worked.

## Expected Results

Running with a passing score:
```
What is your score? 90
You passed!
```

With a failing score:
```
What is you score? 50
Try again
```

## Testing

1. First, run your code interactively with `python3 main.py` and try different
   values.
2. Next, run the automated tests with `python3 test.py` to check your code.

## Hints

The tests are picky about exactly what your string output is, so be sure to get your capitalization right!
