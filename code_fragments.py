#!/usr/bin/env python3

from cgitb import handler
import sys
from typing import Any

count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

for word in ["My", "name", "is", "John"]:
    if word == "name":
        continue
    print(word)

fruits = []
for fruit in ["apple", "banana", "orange"]:
    if fruit == "banana":
        print("I stop eating")
        break
    fruits.append(fruit)
    print(f"I ate {fruits}")


def what_is_this(color):
    if color == "red":
        return "tomato"
    elif color == "green":
        return "green pepper"
    else:
        return "I don't know"


result = what_is_this("red")
print(result)


def add_num(a: int, b: int) -> int:
    return a + b


result = add_num(1, 2)
print(result)

result = add_num("1", "2")
print(result)


def menu(entree, drink="beer", desert="ice cream"):
    print(f"Entree: {entree}")
    print(f"Drink: {drink}")
    print(f"Desert: {desert}")


menu("Steak", "Ice Cream")


def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


print(test_func(100))
print(test_func(200))


def say_something(name, age, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")


say_something(
    "John", 30, "Python", "Rust", "C++", "Go", "SQL", first="John", last="Smith"
)

t = ("Rust", "C++", "Go", "SQL")
say_something("John", 40, *t, first="John", last="Smith")


def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k}: {v}")


menu(entree="Steak", drink="Coke", desert="Cake")

m = {"entree": "Chicken", "drink": "Beer", "desert": "Chocolate"}
menu(**m)


def example_func(
    param1, param2, param3, param4, param5, param6, param7, param8, param9, param10
):
    """Example function with types documented in the docstring.

    Args:
        param1 (int): 整数
        param2 (str): 文字列
        param3 (list): リスト
        param4 (dict): 辞書
        param5 (float): 浮動小数点数
        param6 (bool): 真偽値
        param7 (None): None
        param8 (tuple): タプル
        param9 (set): 集合
        param10 (frozenset): 凍結された集合

    Returns:
        int: 整数
        str: 文字列
        list: リスト
        dict: 辞書
        float: 浮動小数点数
        bool: 真偽値
        None: None
        tuple: タプル
        set: 集合
        frozenset: 凍結された集合

    Examples:
        >>> example_func(1, 'a', [1, 2, 3], {'a': 1, 'b': 2}, 1.0, True, None, (1, 2, 3), {1, 2, 3}, frozenset([1, 2, 3]))
    """
    print(param1)
    print(param2)
    print(param3)
    print(param4)
    return (
        param1,
        param2,
        param3,
        param4,
        param5,
        param6,
        param7,
        param8,
        param9,
        param10,
        True,
    )


example_func(
    1,
    "a",
    [3, 55, "xyz", (1, 2, 3)],
    {"capital": "Tokyo"},
    5.0,
    True,
    None,
    (6,),
    {7},
    frozenset([8]),
)
print(example_func.__doc__)

# 関数内関数
def outer(a, b):
    def inner(c, d):
        return c + d

    r1 = inner(a, b)
    r2 = inner(b, a)
    print(r1 + r2)


outer(1, 2)

# closure
def outer(a, b):
    def inner():
        return a + b

    return inner


print(outer(1, 2))
f = outer(1, 2)
r = f()
print(r)


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius**2

    return circle_area


c1 = circle_area_func(3.14)
c2 = circle_area_func(3.141592653589793)

print(c1(10))
print(c2(10))

# decorator
def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


@print_info
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)


@print_info
def sub_num(a, b):
    return a - b


r = sub_num(10, 20)
print(r)


def print_more(func):
    def wrapper(*args, **kwargs):
        print(f"func: {func.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        print(f"result: {result}")
        return result

    return wrapper


@print_more
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)

f = print_info(print_more(add_num))
r = f(10, 20)
print(r)

# lambda
l = ["Mon", "tue", "Wed", "thu", "fri", "sat", "sun"]


def change_words(words, func):
    for word in words:
        print(func(word))


def sample_func(word):
    return word.capitalize()


def sample_func2(word):
    return word.lower()


sample_func = lambda word: word.capitalize()
sample_func2 = lambda word: word.lower()
change_words(l, sample_func)
change_words(l, sample_func2)
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

# generator
l = ["Good morning", "Good afternoon", "Good evening"]

for i in l:
    print(i)

print("-----------------------------------------------------")


def greeting():
    yield "Good morning"
    yield "Good afternoon"
    yield "Good evening"


for g in greeting():
    print(g)

print("=====================================================")
g = greeting()
print(next(g))
print("=====================================================")
print(next(g))
print("=====================================================")
print(next(g))
print("=====================================================")

# 辞書内包表記
w = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
f = ["coffee", "tea", "milk", "water", "coke", "juice", "beer"]

d_1 = {}
for w, f in zip(w, f):
    d_1[w] = f


d_2 = dict(zip(w, f))
d_3 = {w: f for w, f in zip(w, f)}

print(f"d_1: {d_1}")
print(f"d_2: {d_2}")
print(f"d_3: {d_3}")

# 集合内包表記
s_1 = set()

for i in range(1, 10):
    if i % 2 == 0:
        s_1.add(i)

s_2 = {i for i in range(1, 10) if i % 2 == 0}

print(f"s_1: {sorted(s_1)}")
print(f"s_2: {s_2}")

# generator内包表記
# generator内包表記は、for文で使用するために、yield文を使用する
def generator_func():
    for i in range(1, 10):
        if i % 2 == 0:
            yield i


g = generator_func()

g_1 = (i for i in range(1, 10) if i % 2 == 0)
t_com = tuple(i for i in range(1, 10) if i % 2 == 0)
t = tuple(g_1)

print(f"type: {type(g)}\ng:{(g)}")
print(f"type: {type(g_1)}\ng_1: {(g_1)}")
print(f"type: {type(t_com)}\nt_com: {(t_com)}")
print(f"type: {type(t)}\nt: {(t)}")

# namespace
"""test docstring"""

animal = "cat"


def f():
    # print(animal)
    # global animal
    animal = "dog"
    print(f"local animal: {locals()}")
    print(f"local animal: {animal}")


f()
# print(f"func: {func}")
print(f"global animal: {animal}")


def f():
    """test func docstring"""
    print(f"func name: {f.__name__}")
    print(f"func name: {f.__doc__}")


f()
print(f"global: {globals()}")

# 例外処理
l = [1, 2, 3, 4, 5]
i = 10

try:
    (i + 1) / 0 + l
    print(l[i])
except NameError as e:
    print(f"NameError: {e}")
except IndexError as e:
    print(f"IndexError: {e}")
    print("but Don't worry!!")
except Exception as e:
    print(f"Exception: {e}")
    print("but Don't worry!!")
else:
    print("Done!")
finally:
    print("Clean up!")

print("Keep goin'!!!")


class UpperCaseError(Exception):
    pass


def check(d: list) -> None:
    for word in d:
        if word.isupper():
            raise UpperCaseError(f"{word} is upper case")


try:
    check(["Hello", "W", "Goodbye"])
except UpperCaseError as e:
    print(f"UpperCaseError: {e}")
else:
    print("Done!")
finally:
    print("Clean up!")

# import package_lesson.utils as utils
from package_lesson.say import utils

result = utils.say_twice("Hello")
print(result)

from package_lesson.talk import human

result = human.sing()
print(result)

print(human.cry())

from package_lesson.talk import animal

print(animal.sing())
print(animal.cry())

try:
    from package_lesson import talk
except ImportError as e:
    from package_lesson import tools

    print("tools is imported successfully!")
else:
    print("talk is imported successfully!")

print(talk.human.sing())
print(talk.animal.cry())

# built-in packages
import random
import string

rand_list = [random.randrange(1, 100) for _ in range(1, 100)]
alphabets = string.ascii_lowercase
ranking = {k: v for k, v in zip(alphabets, rand_list)}

print(ranking)
print(sorted(ranking.items(), key=lambda x: x[1], reverse=True))
print(sorted(ranking, key=ranking.get, reverse=True))

# standard library
# collections
s = "sdksgdgkmdldmvlskfvvkdghdgdkdbldbddbvvs"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {c: s.count(c) for c in s}

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

import collections
from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

import termcolor
from termcolor import colored

print("test")
print(colored("test", "red"))

print(f"termcolor: {termcolor.__file__}")
print(f"collections: {collections.__file__}")
print(f"sys.path: {sys.path}")

# class
import abc


class Person(object, metaclass=abc.ABCMeta):
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # abstract method
    @abc.abstractmethod
    def drive(self):
        pass

    # method
    def say_hello(self):
        print(f"Hello, I'm {self.name}")

    # method
    def say_age(self):
        print(f"I'm {self.age} years old")

    def drive(self):
        if self.age >= 18:
            print(f"{self.name} can drive")
        else:
            print(f"{self.name} can't drive")

    # destructor
    def __del__(self):
        print(f"Goodbye, {self.name}")


class Baby(Person):
    def __init__(self, name, age):
        if age < 18:
            super().__init__(name, age)
        else:
            raise ValueError

    def drive(self):
        try:
            super().drive()
        except:
            print(f"{self.name} can't drive")
            raise Exception("You are too young to drive!")
        else:
            print(f"{self.name} can't drive")


class Adult(Person):
    def __init__(self, name, age):
        if age >= 18:
            super().__init__(name, age)
        else:
            raise ValueError

    def drive(self):
        print(f"{self.name} can drive!!")


class NamedJohn(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def drive(self):
        print(f"{self.name} can drive!!")


person = NamedJohn("John", 30)
person.say_hello()
person.say_age()
del person
print("person is deleted")

baby = Baby("マリン", 3)
baby.drive()

adult = Adult("Mark", 20)
adult.drive()


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print("run")

    def ride(self, person):
        person.drive()


car = Car()
car.ride(baby)
car.ride(adult)


class ToyotaCar(Car):
    def run(self):
        print("run fast")


class TeslaCar(Car):
    def __init__(self, model="Model S", enabled_auto_run=False, passwd="1234"):
        super().__init__(model)
        self._enabled_auto_run = enabled_auto_run
        self._passwd = passwd

    # getter
    @property
    def enabled_auto_run(self):
        return self._enabled_auto_run

    # setter
    @enabled_auto_run.setter
    def enabled_auto_run(self, _is_enabled):
        if self._passwd == "1234":
            self._enabled_auto_run = _is_enabled
        else:
            print("wrong password!!!")
            raise ValueError(f"Invalid password: {self._passwd}")

    def run(self):
        print("run super fast")

    def auto_run(self):
        print("auto run")


car = Car()
car.run()

toyota_car = ToyotaCar("Lexus")
print(toyota_car.model)
toyota_car.run()

tesla_car = TeslaCar("Model S", passwd="1234")
print(tesla_car.model)
tesla_car.auto_run()
tesla_car.run()
try:
    tesla_car.enabled_auto_run = True
except AttributeError as e:
    print(f"AttributeError: {e}")
else:
    print(tesla_car.enabled_auto_run)
finally:
    print("Clean up!")


class Human(object):

    kind = "human"

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(f"I'm {self.name}. I'm a {self.kind}.")


a = Human("John")
b = Human("Mary")
a.who_are_you()
b.who_are_you()


class T(object):

    words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word("hello")
c.add_word("world")
print(c.words)

d = T()
d.add_word("hola")
d.add_word("mundo")
print(d.words)

# class method
class Person(object):

    kind = "human"

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about_me(year):
        print(f"I'm a human born in {year}")


a = Person()
print(a.what_is_your_kind())
print(a.about_me(1979))
print(Person.kind)
print(Person.what_is_your_kind())

Person.about_me(2020)


class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

    def __repr__(self):
        return f"Word('{self.text}')"


w1 = Word("Hello")
w2 = Word("World")

print(w1)
print(w1 + w2)
print(w1 == w2)
print(len(w1))
print(repr(w1))

"""
__eq__(self, other) : self == other
__ne__(self, other) : self != other
__lt__(self, other) : self < other
__gt__(self, other) : self > other
__le__(self, other) : self <= other
__ge__(self, other) : self >= other

__add__(self, other) : self + other
__radd__(self, other) : other + self
__iadd__(self, other) : self += other
__sub__(self, other) : self - other
__rsub__(self, other) : other - self
__isub__(self, other) : self -= other
__mul__(self, other) : self * other
__rmul__(self, other) : other * self
__imul__(self, other) : self *= other
__truediv__(self, other) : self / other
__rtruediv__(self, other) : other / self
__itruediv__(self, other) : self /= other
__floordiv__(self, other) : self // other
__rfloordiv__(self, other) : other // self
__ifloordiv__(self, other) : self //= other
__mod__(self, other) : self % other
__rmod__(self, other) : other % self
__imod__(self, other) : self %= other
__pow__(self, other) : self ** other
__rpow__(self, other) : other ** self
__ipow__(self, other) : self **= other
__lshift__(self, other) : self << other
__rshift__(self, other) : self >> other
__ilshift__(self, other) : self <<= other
__irshift__(self, other) : self >>= other
__and__(self, other) : self & other
__rand__(self, other) : other & self
__iand__(self, other) : self &= other
__xor__(self, other) : self ^ other
__rxor__(self, other) : other ^ self
__ixor__(self, other) : self ^= other
__or__(self, other) : self | other
__ror__(self, other) : other | self
__ior__(self, other) : self |= other
__rshift(self, other) : self >> other
__rrshift(self, other) : other >> self
__irshift(self, other) : self >>= other
__neg__(self) : -self
__pos__(self) : +self
__abs__(self) : abs(self)
__invert__(self) : ~self
__complex__(self) : complex(self)
__int__(self) : int(self)
__float__(self) : float(self)
__oct__(self) : oct(self)
__hex__(self) : hex(self)
__index__(self) : self.__index__()
__trunc__(self) : self.__trunc__()
__floor__(self) : self.__floor__()
__ceil__(self) : self.__ceil__()
__round__(self) : self.__round__()
"""

f = open("test.txt", "w")
f.write("Hello World!\n")
print("My", "name", "is", "John", sep=" ", end="!", file=f)
f.close()

words = """\
Hello
World
matrix
"""

with open("test.txt", "w") as f:
    f.write(words)

with open("test.txt", "r") as f:
    print(f.read())

s = """\
Hi $name.

$contents

Have a good day!
"""

t = string.Template(s)
contents = t.substitute(name="John", contents="How are you?")
print(contents)

with open("design/index_template.html", "r") as f:
    t = string.Template(f.read())

contents = t.substitute(name="John", contents="How are you?")
print(contents)

import csv

with open("test.csv", "w", newline="") as f:
    fieldnames = ["Name", "Count"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({"Name": "John", "Count": 1})
    writer.writerow({"Name": "Mary", "Count": 2})

with open("test.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Count"])

import os

print(os.getcwd())
print(os.listdir())
print(os.path.exists("test.txt"))
print(os.path.isfile("test.txt"))
print(os.path.isdir("design"))
print(os.path.splitext("test.txt"))
print(os.path.basename("test.txt"))
print(os.path.dirname("test.txt"))
print(os.path.join("design", "index.html"))
print(os.path.abspath("test.txt"))
print(os.path.relpath("test.txt", "design"))
print(os.path.getsize("test.txt"))
print(os.path.getmtime("test.txt"))
print(os.path.getatime("test.txt"))
print(os.path.getctime("test.txt"))
if os.path.exists("test_link.txt"):
    os.remove("test_link.txt")
    os.symlink("test.txt", "test_link.txt")
print(os.name)

import platform

print(platform.system())
print(platform.release())
print(platform.version())
print(platform.platform())
print(platform.architecture())
print(platform.machine())
print(platform.processor())
print(platform.python_version())
print(platform.python_implementation())
print(platform.python_compiler())
print(platform.python_build())
print(platform.python_branch())
print(platform.uname())
print(platform.win32_ver())

import pathlib

pathlib.Path("empty.txt").touch()

import glob
import shutil
import tarfile

# with tarfile.open("test.tar.gz", "w:gz") as tr:
#     tr.add("test_dir")

# with tarfile.open("test.tar.gz", "r:gz") as tr:
#     tr.extractall(path="test_dir_extract")
#     with tr.extractfile("/path/to/test.txt") as f:
#         print(f.read())

import zipfile

if os.path.exists("test_dir"):
    shutil.rmtree("test_dir")
os.mkdir("test_dir")
pathlib.Path("test_dir/test.txt").touch()
# os.chdir("test_dir")
with zipfile.ZipFile("test.zip", "w") as zf:
    # zf.write("test_dir")
    # zf.write("test_dir/test.txt")
    for i in glob.glob("test_dir/**", recursive=True):
        print(i)
        zf.write(i)

with zipfile.ZipFile("test.zip", "r") as zf:
    for i in zf.namelist():
        print(i)
    with zf.open("test_dir/test.txt") as f:
        print(f.read())

import tempfile

with tempfile.TemporaryFile() as t:
    t.write(b"Hello World!")
    t.seek(0)
    print(t.read())

with tempfile.NamedTemporaryFile() as t:
    print(t.name)
    # with open(t.name, "w+") as f:
    #     f.write("Hello World!")
    #     t.seek(0)
    #     print(t.read())

with tempfile.TemporaryDirectory() as td:
    print(td)
    pathlib.Path(td).touch()
    print(pathlib.Path(td).glob("*"))

temp_dir = tempfile.mkdtemp()
print(temp_dir)

import subprocess

# subprocess.run(["dir", "-ah"])
subprocess.run("dir -ah", shell=True)

import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.isoformat())
print(now.strftime("%Y-%m-%d %H:%M:%S"))

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime("%Y-%m-%d"))

t = datetime.time(12, 34, 56)
print(t)
print(t.isoformat())
print(t.strftime("%H:%M:%S"))

print(now)
d = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=1)
d = datetime.timedelta(hours=1)
d = datetime.timedelta(minutes=1)
d = datetime.timedelta(seconds=1)
d = datetime.timedelta(microseconds=1)
print(now + d)

long_word = []
for word in ["hello", "world", "python"]:
    long_word.append(f"additional-word {word}")
new_long_word = " ".join(long_word)
print(new_long_word)


class MyError(Exception):
    pass


def error_raise(x):
    try:
        if x == 1:
            raise MyError("This is a MyError")
        elif x == 2:
            raise Exception("This is an Exception")
        else:
            raise ValueError("This is a ValueError")
    except MyError as e:
        print(f"This is MyError e: {e}")
    finally:
        print("This is finally")


# error_raise(3)


def t():
    num = []
    for i in range(10):
        num.append(i)
    return num


for i in t():
    print(i)


def t_gen():
    for i in range(10):
        yield i


for i in t_gen():
    print(i)


def other_func(f):
    print(f(10))


def test_func(x):
    return x * 2


other_func(test_func)
other_func(lambda x: x * 2)

y = ""
x = 1 if y else 2
print(x)


def base(x):
    def plus(y):
        return x + y

    return plus


plus = base(10)
print(plus(20))
print(plus(30))

# configparser
import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {"debug": True}
config["web_server"] = {"host": "127.0.0.1", "port": 80}
config["db_server"] = {"host": "127.0.0.1", "port": 3306}
with open("config.ini", "w") as f:
    config.write(f)
print(config["DEFAULT"]["debug"])
print(config["web_server"]["host"])
print(config["db_server"]["host"])

# pyyaml
import yaml  # pip install pyyaml

with open("config.yaml", "w") as yaml_file:
    yaml.dump(
        {
            "web_server": {
                "host": "127.0.0.",
                "port": 8080,
            },
            "db_server": {
                "host": "127.0.0.1",
                "port": "3306",
            },
        },
        yaml_file,
        default_flow_style=False,
    )

with open("config.yaml", "r") as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(f"type: {type(data)}\n{data}")
    print(f"type: {type(data['web_server'])}\n{data['web_server']}")
    print(f"type: {type(data['web_server']['host'])}\n{data['web_server']['host']}")
    print(f"type: {type(data['db_server'])}\n{data['db_server']}")
    print(f"type: {type(data['db_server']['host'])}\n{data['db_server']['host']}")


import dbm

with dbm.open("cache", "c") as db:
    db["key1"] = "value1"
    db["key2"] = "value2"

with dbm.open("cache", "r") as db:
    print(db["key1"])
    print(db["key2"])

import pickle


class T(object):
    def __init__(self, name):
        self.name = name

data = {
    "a": [1, 2, 3],
    "b": ("test", "test"),
    "c": {"key", "key"},
    "d": T("test"),
}

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

with open("data.pickle", "rb") as f:
    data_loaded = pickle.load(f)
    print(data_loaded)
    print(data_loaded["d"].name)
    print(type(data_loaded["a"]))
    print(type(data_loaded["b"]))
    print(type(data_loaded["c"]))
    print(type(data_loaded["d"]))

# xml
import xml.etree.ElementTree as ET

root = ET.Element("root")
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, "employee")

employ = ET.SubElement(employee, "employ")
employ_id = ET.SubElement(employ, "id")
employ_id.text = "111"
employ_name = ET.SubElement(employ, "name")
employ_name.text = "John"

employ = ET.SubElement(employee, "employ")
employ_id = ET.SubElement(employ, "id")
employ_id.text = "222"
employ_name = ET.SubElement(employ, "name")
employ_name.text = "Mary"

tree.write("employee.xml", encoding="utf-8", xml_declaration=True)

tree = ET.ElementTree(file="employee.xml")
root = tree.getroot()

for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)

# json
import json

j = {
    "employee" :
    [
        {"id": 111, "name": "John"},
        {"id": 222, "name": "ときのそら"}
    ]
}

print(j)
print("##########")
print(json.dumps(j))
print("@@@@@@@@@@")
a = j
print(json.dumps(a, indent=4, ensure_ascii=False))

print("@@@@@@@@@@")

with open("employee.json", "w") as f:
    json.dump(j, f)

with open("employee.json", "r") as f:
    print(json.load(f))

# urllib urllib3
import urllib.request
import urllib3

payload = {"key1": "value1", "key2": "value2"}

url = "http://httpbin.org/get"
with urllib.request.urlopen(url) as response:
    # print(response.read().decode("utf-8"))
    print(json.loads(response.read().decode("utf-8")))

http = urllib3.PoolManager()
r = http.request("GET", url)
print(r.status)
print(r.data.decode("utf-8")) # json

url = "http://httpbin.org/post"
payload = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=payload, method="POST")
with urllib.request.urlopen(req) as response:
    print(json.loads(response.read().decode("utf-8")))

r = http.request("POST", url, body=payload)
print(r.status)
print(r.data.decode("utf-8")) # json

url = "http://httpbin.org/put"
# payload = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=payload, method="PUT")
with urllib.request.urlopen(req) as response:
    print(json.loads(response.read().decode("utf-8")))

r = http.request("PUT", url, body=payload)
print(r.status)
print(r.data.decode("utf-8")) # json

url = "http://httpbin.org/delete"
# payload = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=payload, method="DELETE")
with urllib.request.urlopen(req) as response:
    print(json.loads(response.read().decode("utf-8")))

r = http.request("DELETE", url, body=payload)
print(r.status)
print(r.data.decode("utf-8")) # json

# requests
import requests

r = requests.get("http://httpbin.org/get", params=payload, timeout=3)
print(r.status_code)
print(r.text)
print(r.json())


if __name__ == "__main__":
    sys.exit(0)
