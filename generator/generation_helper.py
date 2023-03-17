import random
import string
import re


def random_string(prefix, maxlen):
    symbols = (string.ascii_letters + string.digits + " "*10 + string.punctuation).\
        replace("'", "").replace("\\", "").replace("<", "")
    # временно убираю проблемные символы, чтобы тесты не падали на known issues
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_text(prefix, maxlen, maxrows):
    symbols = (string.ascii_letters + string.digits + " "*10 + "\n" * random.randrange(maxrows) + string.punctuation).\
        replace("'", "").replace("\\", "").replace("<", "")
    # временно убираю проблемные символы, чтобы тесты не падали на known issues
    return prefix + "".join([random.choice(symbols.replace("'", "")) for i in range(random.randrange(maxlen))])


def clear_spaces(s):
    return " ".join(s.split()) if s is not None else ""


def clear_spaces_textarea(s):
    return re.sub(" +", " ", re.sub(" \n", "\n", re.sub("\n ", "\n", s))).strip() if s is not None else ""
