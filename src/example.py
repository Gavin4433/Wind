import Wind


# DEFINE
class WRAPPER(Wind.Wind):
    def __init__(self, target_func, global_handlers, *args, **kwargs):
        super().__init__(target_func, global_handlers, *args, **kwargs)

    def run(self, args_dict, *args, **kwargs):
        self.target_func(*args, **kwargs)
        print(args_dict["string"])
        print("Wind is not a decorator!")


class WRAPPER2(Wind.Wind):
    def __init__(self, target_func, global_handlers, *args, **kwargs):
        super().__init__(target_func, global_handlers, *args, **kwargs)

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
a.wrap()
liang("HELLO", "MR.liang")

# RESET THE FUNCTION
a.reset()
print()

# The Second Wrap
b = WRAPPER2(liang, globals())
b.wrap()
liang("HELLO", "MR.liang")
b.reset()


class GET_ARGS(Wind.Wind):
    def __init__(self, target_func, global_handlers, *args, **kwargs):
        super().__init__(target_func, global_handlers, *args, **kwargs)

    def run(self, args_dict, *args, **kwargs):
        print(args_dict)


c = GET_ARGS(liang, globals())
c.wrap()
liang("HELLO", "MR.liang")
