import os


def dequote_str(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    Ignores None value

    https://stackoverflow.com/a/20577580
    """
    if s:
        if (s[0] == s[-1]) and s.startswith(("'", '"')):
            return s[1:-1]
    return s


def read_int_env_var(variable, default):
    """
    Read an int variable from environment, use default if not found
    """
    try:
        value = int(os.environ.get(variable, default))
    except Exception as e:
        value = default
    return value


def read_float_env_var(variable, default):
    """
    Read an float variable from environment, use default if not found
    """
    try:
        value = float(os.environ.get(variable, default))
    except Exception as e:
        value = default
    return value


def read_bool_env_var(variable, default):
    """
    Read an boolean variable from environment, use default if not found
    """
    try:
        value = os.environ.get(variable, default)
    except Exception as e:
        value = default
    return value.lower() in ['true', '1']


def read_str_env_var(variable, default, dequote=True):
    """
    Read an str variable from environment, use default if not found

    Will strip leading/ending double and single quotes by default, but this
    can be overridden with the dequote=False
    """
    try:
        value = os.environ.get(variable, default)
    except Exception as e:
        value = default
    if dequote:
        value = dequote_str(value)
    return value
