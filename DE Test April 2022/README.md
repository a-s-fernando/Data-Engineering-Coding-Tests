# Data engineering Python tests

> For interviews in April 2022.

This test is to assess your ability to write Python code and to discuss how you think about coding problems during the interview. Don't worry if you don't complete the whole test - you can still pass the interview.

You should have been introduced to a person you can contact to clarify questions or solve technical issues. If anything is unclear or something is wrong, ask them as soon as possible. Asking questions will not affect how we score you on the test, so it is better to ask sooner rather than later.

You are free to use the internet to solve these tests and you can install additional packages. However, the solutions to this test can be achieved using Python and its standard libraries. Use whatever you're most comfortable with. This coding test was written and tested with python 3.8.

## Working with the code

If you can, clone this repo and work on your solutions on your own computer.

If you don't have a computer where you can do this, you can [complete the test on Google Colab](https://colab.research.google.com/drive/1jIYgeEKarkr6FHAnys6wVSoTIl24PjW6?usp=sharing) instead. Please create a copy of the notebook before you start.

During the interview we'll ask you to share your screen to show and discuss your solutions. You don't need to push your changes to Github or save them anywhere else.

## Doing the tests

There are 3 scripts in the root of this repo/directory:

- test_1.py
- test_2.py
- test_3.py

These scripts do not need to be completed in order, but we do recommend you do.

In each script is a comment block starting with `[TODO]`. This lays out what needs to be done to solve the test for that particular script. The remaining comments are there to explain the code and direct you.
**TODO lines have been removed after having completed the tasks.**

### Test 1

This asks you to extract and structure data from the file `sample.log`. You'll need to complete 2 short functions.

When you think you have the answer, run `python test_1.py` and it will be automatically tested.

**Although unspecified, validation for the `log_level` has been added to the `is_log_file` function.**

### Test 2

This asks you do get data from an API and match it with data from the file `people.csv`.

You're free to approach this however you like. We'll ask you to describe your approach and reasoning during the interview.

**Main prints the original csv data with each row having some extra data appended to it, resulting to a final list of dictionaries with keys: `person_name, home_postcode, looking_for_court_type, nearest_court_name, nearest_court_distance, nearest_court_dx_number (if applicable)`**

**Tests can be run using `pytest test_2.py`**

### Test 3

This asks you to fix a broken function and then write a unit test for it.

**The function has been edited to perform additional verification on whether the time inputted is valid. Tests can be run using `pytest test_3.py`**
