#!/usr/bin/env python3

import sys

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


def outer(a, b):
    def inner(c, d):
        return c + d

    r = inner(a, b)
    return r


r = outer(1, 2)
print(r)

if __name__ == "__main__":
    sys.exit(0)
