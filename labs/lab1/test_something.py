#!/usr/bin/env python
import unittest
from mockito import *
from something import Something, Operand

class SomethingTestCase(unittest.TestCase):
    def test_init_should_assign_what(self):
        # setup

        # action
        something = Something("what")

        # assert
        self.assertTrue("what", something.attribute)

    def test_doing_something_should_return_string_something(self):
        # setup
        something = Something("what")

        # action
        ret = something.doing_something()

        # assert
        self.assertTrue("something", ret)

    def test_doing_something_should_return_string_something_else(self):
        # setup
        something = Something(any(unicode))

        # action
        ret = something.doing_something()

        # assert
        self.assertTrue("something else", ret)

    def test_send_result_should_add_op2_to_op1(self):
        # setup
        something, op1, op2 = self.getSomething()

        # action
        something.send_result()

        # assert
        verify(op1).add(op2)

    def test_send_result_should_first_sum_op1_op2_then_send_op1(self):
        # setup
        something, op1, op2 = self.getSomething()

        # action
        something.send_result()

        # assert
        inorder.verify(op1, times=1).add(op2)
        inorder.verify(op1, times=2).send()

    def test_send_result_should_raise_network_problem_exception_when_op1_is_None(self):
        # setup
        something, op1, op2 = self.getSomething()
        something.op1 = None

        # assert
        with self.assertRaises(Something.NetworkProblemException):
            # action
            something.send_result()

    def test_send_result_should_execute_catch_handler_when_send_raises_exception(self):
        # setup
        something, op1, op2 = self.getSomething()
        when(op1).send().thenRaise(Operand.AException)

        # action
        something.send_result()

        # assert
        verify(op1, times=1).rollback()

    def getSomething(self):
        op1 = mock()
        op2 = mock()
        something = Something(any())
        something.op1 = op1
        something.op2 = op2
        return (something, op1, op2)

if __name__ == "__main__":
    unittest.main()
