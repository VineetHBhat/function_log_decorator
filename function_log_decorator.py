import logging

###############################################################################
#                               LOGGER CONFIG                                 #
###############################################################################

# logger variables
log_filename = 'function_calls.log'
string_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
datetime_format = '%Y-%B-%d %H:%M:%S'

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create file handler and set level to debug
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(string_format, datetime_format)

# add formatter to fh
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(fh)

###############################################################################


def logging_decorator(undecorated_function):

    def logging_wrapper(*args):
        logger.info(f'{undecorated_function.__name__}() called with {args}')
        returned_value = undecorated_function(*args)
        return returned_value

    return logging_wrapper


@logging_decorator
def sum_all_args(*args):
    sum = 0.0
    for arg in args:
        sum += arg
    return sum


result = sum_all_args(1, 2, 3, 4, 5, 6, 7, 8, 9.9, 12.45)
print(f'{result}')
