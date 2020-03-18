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

## Attribution
*Introducing Python* by Bill Lubanovic (O’Reilly). Copyright 2020 Bill Lubanovic, 978-1-492-05136-7.