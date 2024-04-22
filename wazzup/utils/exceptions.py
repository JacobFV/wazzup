class AuthenticationError(Exception):
    pass

class DataIngestionError(Exception):
    pass

class SamplingError(Exception):
    pass

class GenerationError(Exception):
    pass

__all__ = [
    "AuthenticationError",
    "DataIngestionError",
    "SamplingError",
    "GenerationError",
]
