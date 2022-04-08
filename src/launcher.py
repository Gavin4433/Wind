def run_func(Wind_Class, func_name, global_handler, *args, **kwargs):
    """Really Terrible Realize, isn't it?"""
    Wind_Class(func_name, global_handler)()(*args, **kwargs)
