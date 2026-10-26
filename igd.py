#####
# Iterables, Iterators and Generator Functions

# 1. Iterable - Any object you can loop over to get its items one by one (list, string, tuple, set, dict, range).
names = ["Hema", "Ravi", "Priya"]
for name in names: # here names is iterable
    print(name)

# 2. Iterator - An object that remembers its position and returns the next item each time it's asked.
# 3. iter() - Creates an iterator from an iterable.
num = [10, 20, 30]
iterator = iter(num)
print(iterator)                 # <list_iterator object at 0x...>

# 4. next() - Returns the iterator's next item and moves forward; it can't go back.
print(next(iterator))           # 10
print(next(iterator))           # 20
print(next(iterator))           # 30

# 5. StopIteration - Raised when next() is called after the last item.
# print(next(iterator))         # StopIteration

# 6. Normal function with return - Builds and returns everything at once, then ends.
def get_numbers():
    return [10, 20, 30]

print(get_numbers())            # [10, 20, 30]

# 7. Generator function - A function that uses yield; calling it returns a generator instead of running the body.
# 8. yield - Gives back one value and pauses the function, resuming from the same point on the next request.
def get_numbers():
    yield 10
    yield 20
    yield 30

gen = get_numbers()
print(next(gen))                # 10
print(next(gen))                # 20

# 9. Looping over a generator - for calls next() automatically and stops cleanly at the end.
for n in get_numbers():
    print(n)                    # 10, 20, 30

# 10. Generator with a loop - Produces values on demand, so it can handle very large or endless sequences.
def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1

print(list(count_up_to(5)))     # [1, 2, 3, 4, 5]

#####
# Generator Expressions and Decorators

# 1. List comprehension - Builds the whole list in memory at once, using square brackets.
numbers = [1, 2, 3, 4, 5]
squares_list = [x*x for x in numbers]
print(squares_list)             # [1, 4, 9, 16, 25]

# 2. Generator expression - Same syntax with parentheses; produces values one at a time, only when asked.
squares = (x*x for x in numbers)
print(squares)                  # <generator object <genexpr> at 0x...>  (values not created yet)

# 3. Using a generator expression - Get values with next() or a for loop; it can be used only once.
for value in squares:
    print(value)                # 1, 4, 9, 16, 25

# 4. Generator expressions in functions - Can be passed directly, without extra brackets.
print(sum(x*x for x in numbers))    # 55


# 5. Decorator - A function that takes another function and returns a new one with extra behaviour added, without changing the original's code.
# 6. Wrapper function - The inner function that adds code before and/or after calling the original.
def check_login(func):              # func is the function being decorated
    def wrapper():
        print("checking user...")   # Runs before the original function
        func()                      # Calls the original function
        print("completed")          # Runs after
    return wrapper                  # Returns the new, wrapped function

# 7. Applying a decorator manually - Replace the function with its wrapped version.
def login():
    print("user logged in")

loginfunc = check_login(login)
loginfunc()
# checking user...
# user logged in
# completed

# 8. @ syntax - A shortcut that does the same as login = check_login(login).
@check_login
def login():
    print("user logged in")

login()                             # Same output as above

# 9. Decorating functions with arguments - Use *args and **kwargs so the wrapper accepts any arguments.
def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)    # Pass the arguments on, and return the result
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(3, 4))
# Calling add
# 7
