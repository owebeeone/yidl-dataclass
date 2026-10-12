"""Public declaration and field callback diagnostics."""


class DataclassDefinitionError(TypeError):
    """A declaration cannot satisfy its requested dataclass contract."""


class FieldConversionError(TypeError):
    """A field converter failed."""


class FieldValidationError(ValueError):
    """A field validator rejected a value or failed."""


class FieldInitializationError(RuntimeError):
    """A field factory failed."""


class LazyInitializationError(RuntimeError):
    """Lazy initialization failed or reentered."""
