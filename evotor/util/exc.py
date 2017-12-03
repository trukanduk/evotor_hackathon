class NotImplementedErr(Exception):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)


class RedirectException(Exception):
    def __init__(self, url):
        self.url = url
