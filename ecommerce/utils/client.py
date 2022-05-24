from django.http import HttpResponse


def remove_cookie(response: HttpResponse, cookie_key: str) -> HttpResponse:
    """
    remove specific in a response
    :param response: a http response
    :param cookie_key: a string key in cookie
    :return: response
    """
    response.delete_cookie(cookie_key)
    return response