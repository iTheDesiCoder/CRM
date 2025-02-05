from contextvars import ContextVar


class RequestContext:
    headers = ContextVar('headers', default={})
