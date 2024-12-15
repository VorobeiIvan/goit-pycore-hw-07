from src.decorator.colorize_message import colorize_message
from src.constants import messages_error

@colorize_message
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return messages_error["value_error"]
        except KeyError:
            return messages_error["key_error"]
        except IndexError:
            return messages_error["index_error"]
        except TypeError:
            return messages_error["type_error"]
    return inner
