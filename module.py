#####
# Importing built-in modules: math, random and datetime

# basic syntax: import module_name

# 1. math
# importing the entire math module
import math 
print(math.sqrt(25))
print(math.pi)

# importing only the required piece of the math module
from math import sqrt
print(sqrt(49))

# 2. random
import random
number = random.randint(1, 10)
print("random number:", number)

# 3. datetime
from datetime import datetime
now = datetime.now()
print(now)
time = now.time()
print(time)
# %d - day
# %m - month
# %Y - year
# %H - hours
# %M - minutes
# %S - seconds
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)

#####
# Virtual environment and usage of modules by installing them
import requests
response = requests.get("http://www.youtube.com")
print(response.status_code)