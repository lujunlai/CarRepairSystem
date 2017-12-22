#   encoding=utf8

import functools
import logging
import time

logger = logging.getLogger('CarRepairSystem')
logger.setLevel(logging.INFO)

# create a file handler

handler = logging.FileHandler('CarRepairSystem.log')
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)


def logged(method):
    """Cause the decorated method to be run and its results logged, along
    with some other diagnostic information."""

    @functools.wraps(method)
    def inner(*args, **kwargs):
        # Record our start time.
        start = time.time()
        # Run the decorated method.
        return_value = method(*args, **kwargs)
        # Record our completion time, and calculate the delta.
        end = time.time()
        delta = end - start
        # Log the method call and the result.
        logger.info('Called method %s; execution time %.02f seconds; result %r.' %
                    (method.__name__, delta, return_value))
        # Return the methods original return value.
        return return_value

    return inner
