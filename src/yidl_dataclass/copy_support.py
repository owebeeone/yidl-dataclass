"""Pickle's importable object allocation seam; field restoration is generated."""


def restore(cls):
    return object.__new__(cls)
