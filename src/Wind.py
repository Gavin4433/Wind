# Author: @liang_awa
import inspect


class WindWrapFailedError(Exception):
    pass


class Wind:
    def __init__(self, target_func, global_handlers, *args, **kwargs):
        """
        :param target_func_name: NAME OF TARGET FUNCTION
        :param args: ARGS
        :param kwargs: KEY WORD ARGS
        """
        self.runtime_gh = global_handlers
        self.target = target_func.__name__
        self.target_func = self._wrap()
        self.runtime_args = args
        self.runtime_kwargs = kwargs

    def run(self, args_dict, *args, **kwargs):
        """This method needs to have a change"""
        pass

    def _wrap(self):
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

    def __call__(self):
        """
        The author of this project is really smart! I'll give this project a star!!!
        OR YOU CAN SUBSCRIBE MY CHANNEL ON BILIBILI.COM
        LINK:https://space.bilibili.com/1659221136
        我真不要脸QAQ，但看得懂中文的朋友能给这个项目一个STAR，再去b站上关注我一下吗，秋梨膏QAQ
        """
        return self._main

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
