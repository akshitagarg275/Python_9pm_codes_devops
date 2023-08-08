# version 2

import random
import string

random.seed(56)
DB = {}

def getShortURL(longURL, myShortURL = None):
    if myShortURL:
        if myShortURL in DB:
            return "Short URL already exists"
        else:
            DB[myShortURL] = longURL
            res ="cm.in/"+ myShortURL
            return res
    
    l = random.randint(4,6)

    # generating random characters or numbers
    chars = string.ascii_lowercase + string.digits
    shortURL = ''.join([random.choice(chars) for i in range(l)])

    if shortURL in DB:
        return getShortURL(longURL)
    else:
        DB[shortURL] = longURL
        res = "cm.in/"+ shortURL
    return res

url = "www.google.com"
print(getShortURL(url, "abcde"))
# print(DB)


def getLongURL(shortURL, newLongURL):
    """
    given a short URL, returns LONG URL
    """
    print("ShortURL: ",shortURL)

    # https://www/cm.in.abcde -> abcde
    if shortURL in DB:
        shortURL = shortURL.split('/')[-1]
        DB[shortURL] = newLongURL
        res = "cm.in/"+ shortURL
        return res
    else:
        return "Short URL doesn't exist"

url2 = "abcde"
print("BEFORE:",DB)
print(getLongURL(url2, "www,facebook.com"))
print("AFTER:",DB)