# -*- coding:utf-8 -*-

class Operand(object):
    class AException(Exception):
        pass

    def add(self, op):
        pass

    def send(self):
        pass

class Something(object):
    class NetworkProblemException(Exception):
        pass

    def __init__(self, received_object):
        self.attribute = received_object
        self.op1 = None
        self.op2 = None

    def doing_something(self):
        if self.attribute == "what":
            return "something"
        return "something else"

    def send_result(self):
        if self.op1 is None:
            raise self.NetworkProblemException
        self.op1.add(self.op2)
        try:
            self.op1.send()
            if True:
                pass # doing_something_really_important()
            self.op1.send()
        except Operand.AException:
            self.op1.rollback()
