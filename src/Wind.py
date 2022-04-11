# Author: @liang_awa
import inspect


class WindWrapFailedError(Exception):
    pass


class Wind:
    def __init__(self, target_func, global_handler, *args, **kwargs):
        """
        :param target_func_name: NAME OF TARGET FUNCTION
        :param args: ARGS
        :param kwargs: KEY WORD ARGS
        """
        self.runtime_gh = global_handler
        self.target = target_func.__name__
        self.target_func = self._get_func_definition()
        self.runtime_args = args
        self.runtime_kwargs = kwargs

    def run(self, args_dict, *args, **kwargs):
        """This method needs to have a change"""
        pass

    def _get_func_definition(self):
        """WRAP? OR JUST GET THE TARGET?"""
        try:
            func = self.runtime_gh[self.target]
        except KeyError:
            raise WindWrapFailedError("No Function called " + self.target)
        else:
            return func

    def _main(self, *args, **kwargs):
        """
        EXECUTION PART TO REPLACE THE TARGE
        """
        self.run(self._ArgPairingByPos(args, kwargs), *args, **kwargs)

    def del_kwargs_from_args(self, ARGS, KWARGS):
        """JUST AS ITS NAME"""
        ARGNAMES = KWARGS.keys()
        for an in ARGNAMES:
            ARGS = list(filter(lambda x: x != an, ARGS))
        return ARGS

    def _ArgPairingByPos(self, tfa, tfkwa):
        """
        LET'S SEE, WHICH ONE IS THE KEYWORD?
        """
        ARGUMENTS = {}
        args = self.del_kwargs_from_args(inspect.signature(self.target_func).parameters, tfkwa)
        for arg, tf in zip(args, tfa):
            ARGUMENTS[arg] = tf
        ARGUMENTS["KWARGS"] = tfkwa
        # print(ARGUMENTS) *ONLY FOR DEBUGGING
        return ARGUMENTS

    def wrap(self):
        self.runtime_gh[self.target] = self._main

    def reset(self):
        self.runtime_gh[self.target] = self.target_func
