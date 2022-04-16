from typing import List


def checkDFALanguage(lang, acceptables: List, allowEmpty: bool = False):
    if(allowEmpty == True and len(lang) == 0):
        return True
    for char in range(len(lang)):
        if lang[char] not in acceptables:
            return False
