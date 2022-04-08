import Wind
import launcher


# DEFINE
class WRAPPER(Wind.Wind):
    def __init__(self, target_func_name, global_handlers, *args, **kwargs):
        super().__init__(target_func_name, global_handlers, *args, **kwargs)

    def run(self, args_dict, *args, **kwargs):
        self.target_func(*args, **kwargs)
        print(args_dict["string"])
        print("Wind is not a decorator!")


# TEST FUNCTION
def liang(string, string2):
    print(string + ", " + string2 + "!")


# EXECUTE
launcher.run_func(WRAPPER, liang, globals(), "Hello", "liang")
