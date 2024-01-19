import random
import string


def build_short_url(host, alias) -> str:
    res = build_random_string()

    if alias != "":
        res = alias

    return f"{host}/{res}"


def build_random_string(k=8) -> str:
    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=k))

    return res
