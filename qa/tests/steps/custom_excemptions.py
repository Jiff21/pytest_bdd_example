"""Custom Exceptions for use with tests"""


def loop_thru_messages(messages):
    """function that loops through messages and returns them all in 1 string"""
    value = ""
    for message in messages:
        value += "\r\n" + str(message)
    return str(value)


def dictionary_printer(dictionary):
    """get a string representation of a dictionary"""
    value = ""
    for key in dictionary:
        value += "\r\n%s - %s" % (key, dictionary[key])
    return str(value)


class LoopThruMessagesException(Exception):
    """loops through a list of messages for use when list is not empty"""

    def __init__(self, messages):
        super().__init__(messages)
        self.value = ""
        for message in messages:
            self.value += "\r\n" + str(message)

    def __str__(self):
        return str(self.value)
