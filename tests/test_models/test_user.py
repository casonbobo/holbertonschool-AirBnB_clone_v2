#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        def test_init(self):
            self.assertEqual(User, type(User()))

if __name__ == "__main__":
    unittest.main()
