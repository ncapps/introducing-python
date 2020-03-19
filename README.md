# Notes and Examples from Introducing Python by Bill Lubanovic
## Part 1. Python Basics
### Chapter 1. A Taste of Py
- Python is a good general-purpose, high-level language. It's design make it very *readable*.

### Chapter 2. Data: Types, Values, Variables, and Names
- Python is *strongly typed*, which means that the type of an object does not change, even if its value is mutable

### Chapter 3. Numbers
- In Python, the expressino on the right side of the = is calculated first, and then assigned to the variable on the left side
- You can express literal integers in three bases besides decimal with these integer prefixes:
  - `0b` or `0B` for *binary* (base 2)
  - `0o` or `0O` for *octal* (base 8)
  - `0x` or `0X` for *hex* (base 16)

### Chapter 4. Choose with if
  - The recommended maximum line length is 80 characters
  - Whenever you need to make a lot of comparisons separate by `or`, use the *membership operator* `in`

### Chapter 5. Text Strings
 - Strings in Python are `immutable`
 - You can extract a *substring* from a string by using a *slice*

### Chapter 6. Loops with while and for
  - Python makes frequent use of *iterators*. Iterators make it possible to traverse data structures without knowing how large they are or how they are implemented.
  - `while` and `for` loops have an optional `else` that is executed if the loop completes without calling `break`
  - `range()` returns an *iterable* object, so you need to step through the values with `for ... in` or convert the object to a sequence like a list

## Chapter 7. Tuples and lists
  - Python has three sequence structures: *strings*, *tuples*, *lists*
  - Tuples are immutable, Lists are mutable
  - Use a *set* if you want to track unique values but do not care about order
  - `list()` function also converts other *iterable* data types to lists (e.g., tuples, strings, sets, and dictionaries)
  - The `reverse()` function changes a list, slices do not change the list
  - `del` is a Python *statement* not a list method. It detaches a name from a Python object and can free up the object's memory if that name were the last reference to it
  - Get an item by offset and delete it with `pop(offset)`
  - The Pythonic way to check for existence of a value in a list is using `in`
  - `join()` *is the opposite of* `split()`
  - The list method `sort()` sorts the list itself, *in place*
  - The general function `sorted()` returns a sorted *copy* of the list
  - You can *copy* the values of a list to an independent list using:
    - `copy()` method
    - `list()` conversion function
    - list slice `[:]`
    - `deepcopy()` can handle deeply nested lists, dictionaries
  - Iterate over multiple sequences in paralle by using the `zip()` function. The return value from `zip()` is an iterable value which can be turned into a list or tuple
  - The simplest form of *list comprehension* looks like: `[expression for item in iterable]`
  - A list comprehension can include a conditional expression: `[expression for item in iterable if condition]`


## Attribution
*Introducing Python* by Bill Lubanovic (O’Reilly). Copyright 2020 Bill Lubanovic, 978-1-492-05136-7.