[![pypi](https://img.shields.io/pypi/v/WIND-liang233.svg)][![pypi](https://img.shields.io/pypi/pyversions/WIND-liang233.svg)]

#How To Install 
```commandline
pip install WIND-liang233
```

#Wind Is Not a Decorator
A dynamic decorator? Maybe...

# **How To Use**
Just as the example.py

# Features
1.Modify the function dynamically!

JUST LIKE THE CODE IN EXAMPLE.py
```
import Wind


# DEFINE
class WRAPPER(Wind.Wind):
    def __init__(self, target_func, global_handlers, *args, **kwargs):
        ...

    def run(self, args_dict, *args, **kwargs):
        self.target_func(*args, **kwargs)
        print(args_dict["string"])
        print("Wind is not a decorator!")


class WRAPPER2(Wind.Wind):
    def __init__(self, target_func, global_handlers, *args, **kwargs):
        ...

    def run(self, args_dict, *args, **kwargs):
        print("Begin!")
        self.target_func(*args, **kwargs)
        print("End")


# TEST FUNCTION
def liang(string, string2):
    print(string + ", " + string2 + "!")


# EXECUTION

# The First Wrap
a = WRAPPER(liang, globals())
a.wrap(vars())
liang("HELLO", "MR.liang")

# RESET THE FUNCTION
a.reset(vars())
print()

# The Second Wrap
b = WRAPPER2(liang, globals())
b.wrap(vars())
liang("HELLO", "MR.liang")
b.reset(vars())
```
And We Get These Outputs:
```
HELLO, MR.liang!
HELLO
Wind is not a decorator!

Begin!
HELLO, MR.liang!
End
```

2.Maybe you can ... get the arguments of the function:
```

...

class GET_ARGS(Wind.Wind):
    def __init__(self, target_func, global_handlers, *args, **kwargs):
       ...

    def run(self, args_dict, *args, **kwargs):
        print(args_dict)
        
c = GET_ARGS(liang, globals())
c.wrap(vars())
liang("HELLO", "MR.liang")

```

And We can get these:
```
{'string': 'HELLO', 'string2': 'MR.liang', 'KWARGS': {}}
```

Really Powerful, isn't it?


# SOMETHING ELSE

Bilibili: @liang_awa

DONATE? : [HERE](https://afdian.net/@liangcha_awa)
