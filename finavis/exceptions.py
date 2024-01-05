class RequestUnhandledException(Exception):
    """Unhandled"""


class NotFoundException(Exception):
    """Custom exception if data not found"""


class TickerNotFoundException(Exception):
    """Custom exception if ticker not found"""


class RequestTimeoutException(Exception):
    """Exception if timeout"""


class RequestMaxRetryException(Exception):
    """Exception if max_retries on session"""


class RequestDocumentIsEmptyException(Exception):
    """If document is empty"""
