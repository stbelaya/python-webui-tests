import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10 # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_text(prefix, maxlen, maxrows):
    symbols = string.ascii_letters + string.digits + " " * 10 + "\n" * random.randrange(maxrows) # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def clear_spaces(s):
    return " ".join(s.split()) if s is not None else ""
