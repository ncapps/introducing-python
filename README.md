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

## Chapter 8. Dictionaries and Sets
  - Get an item by `[key]` or with `get()`
  - In Python 3, you need to use the `list()` function to turn the results of `keys()`, `values()` and `items()` into normal Python lists
  - Combine dictionaries with `{**a,**b}` or `update()`
  - Dictionary comprehension: `{key_expression : value_expression for expression in iterable}`
  - Dictionary comprehension with conditional: `{key_expression : value_expression for expression in iterable if condition}`
  - use `set()` to print an empty set
  - When you give `set()` a dictionary, it uses only the keys
  - Use *set intersection operator* with `&` : `{a, b, c} & {a, b}`
  - Use *set union operator* with `|` : `{a, b, c} | {a, b, d}`
  - Use *set difference operator* with `-` : `{a, b, c} - {a, b, d}`, members of the first set but not the second
  - Use *set exclusive operator* with `^` : `{a, b, c} ^ {a, b, d}`, items in one set or the other, but not both
  - Use *set subset operator* with `<` : `{a, b, c} <= {a, b, c, d}`, all members of the first set are also in the second set
  - Set comprehension: `{ expression for expression in iterable }`, condition test: `{ expression for expression in iterable if condition }`
  - Create an immutable set with `frozenset()`

## Chapter 9. Functions
  - The values passed into a function are called *arguments*. The values of those arguments are copied to their corresponding *parameters* inside the function
  - `None` is a special Python value - It is equivalent to the boolean value `False`. Use Python's `is` operator to distinguish between `None` and `False`
  - Default parameter values are calculated when the function is *defined*, not when it is run.
  - Outside the function, `*args` explodes the tuple `args` into comma-separated positional parameters
  - Inside the function, `*args` gather all of the positional arguments into a single `args` tuple
  - Use two asterisks (**) to group keyword arguments into a dictionary, where the argument names are the keys and their values are the corresponding dictionary values.
  - Outside a function, `**kwargs` *explodes* a dictionary `kwargs` into *name=value* arguments
  - Inside a function, `**kwargs` *gathers* `name=value` arguments into the single dictionary parameter `kwargs`
  - Argument order is:
    1. Required positional arguments
    2. Optional positional arguments (`*args`)
    3. Optional keyword arguments (`**kwargs`)
  - Functions are first-class citizens in Python. You can assign them to variables, use them as arguments to other functions, and return them from functions.
  - In Python, parentheses mean *call this function*. With no parentheses, Python just treats the function like any other object
  - Functions can be elements of lists, tuples, sets, and dictionaries. Functions are immutable, so they can also be used as dictionary keys.
  - An inner function can act as a *closure*. This is a function that is dynamically generated by another function and can both change and remember the values of variables that were created outside the function.
  - A Python *lambda function* is an anonymous function expressed as a single statement. A lambda has zero or more comma-separated argumetns, followed by a colon (:), and then the definition of the function.
  - A *generator* is a Python sequence creation object. With it, you can iterate through potentially huge sequences without creating and storing the entire sequence in memory at once.
  - A *decorator* is a function that takes on function as input and returns another function
  - You can add `@decorator_name` before the function definition that you want to decorate
  - Recursion is useful when you're dealing with "uneven" data, like lists of lists of lists
  - Use `try` to wrap your code, and `except` to provide the error handling
  - 

## Attribution
*Introducing Python* by Bill Lubanovic (O’Reilly). Copyright 2020 Bill Lubanovic, 978-1-492-05136-7.