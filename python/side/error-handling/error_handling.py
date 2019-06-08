""" Error Handling - Solution """

def handle_error_by_throwing_exception():
    """
    Exception simulation by raising error
    """
    raise Exception("Raising Custom Exception.")


def handle_error_by_returning_none(input_data) -> int:
    """
    Handles error by returning None

    :param input_data: Some data to be converted to integer.
    """
    try:
        return int(input_data)
    except TypeError:
        return None


def handle_error_by_returning_tuple(input_data) -> tuple:
    """
    Handles error by returning a tuple

    :param input_data: Some data to be converted to integer.
    """
    try:
        return (True, int(input_data))
    except TypeError:
        return (False, None)


def filelike_objects_are_closed_on_exception(filelike_object):
    """
    General file operation to simulate handling error on files.

    :param filelike_object: File object.
    """
    try:
        filelike_object.open()
        filelike_object.do_something()
        filelike_object.close()
    except:
        filelike_object.close()
        raise Exception("Something Fails, file has been closed.")
