from .log_main import log
from .startup import enable_ansi
from .ansi import ansi

logger = log()

__all__ = ["logger", "enable_ansi", "ansi"]
