from django.shortcuts import render
from util.exc import RedirectException


def safe_view(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RedirectException as re:
            return redirect(re.url)

    return func_wrapper
