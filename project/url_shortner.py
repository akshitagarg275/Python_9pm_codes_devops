# version 1

import random
import string

random.seed(56)
DB = {}


def getShortURL(longURL):
    """
    given a long URL , returns a short URL
    """
    chars = string.ascii_lowercase
    l = random.randint(4,6)
    # generating random characters
    shortURL = ''.join([random.choice(chars) for i in range(l)])

    if shortURL in DB:
        return getShortURL(longURL)
    else:
        DB[shortURL] = longURL

    res = "cm.in/"+ shortURL
    return res

url = "www.google.com"
print(getShortURL(url))
print(DB)

def getLongURL(shortURL):
    """
    given a short URL, returns LONG URL
    """

    # https://www/cm.in.abcde -> abcde

    key = shortURL.split('/')[-1]

    if key in DB:
        return DB[key]
    else:
        return "Short URL doesn't exist"

url2 = "cm.in/apuqjy"
print(getLongURL(url2))