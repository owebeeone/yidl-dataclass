"""Compiler field families; plain immutable traits, never runtime dispatch."""


class FieldKind:
    __slots__ = ()
    label = ""
    stored = False
    metadata = True
    parameter = False
    mandatory_source = False
    extension_init = False
    class_fallback = False


class OrdinaryKind(FieldKind):
    __slots__ = ()
    label = "ordinary"
    stored = True
    parameter = True
    class_fallback = True


class InitvarKind(FieldKind):
    __slots__ = ()
    label = "initvar"
    parameter = True
    mandatory_source = True
    extension_init = True


class ClassvarKind(FieldKind):
    __slots__ = ()
    label = "classvar"


class LocalKind(FieldKind):
    __slots__ = ()
    label = "local_store"
    stored = True
    metadata = False
    mandatory_source = True
    extension_init = True


class ConstKind(OrdinaryKind):
    __slots__ = ()
    label = "const"
    mandatory_source = True
    extension_init = True
    class_fallback = False
