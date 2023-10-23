#!/usr/bin/python3
def safe_function(fct, *args):
    """executes a function safely"""
    import sys
    try:
        return fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return None
