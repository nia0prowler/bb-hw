"""hello world module"""
import peewee


def hello(who):
    """function that greats"""
    return 'hello {}'.format(who)
