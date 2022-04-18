import string

UNALLOWED = [
 'class', 'mro', 'init', 'builtins', 'request', 'app','sleep', 'add', '+', 'config', 'subclasses', 'format', 'dict', 'get', 'attr', 'globals', 'time', 'read', 'import', 'sys', 'cookies', 'headers', 'doc', 'url', 'encode', 'decode', 'chr', 'ord', 'replace', 'echo', 'base', 'self', 'template', 'print', 'exec', 'response', 'join', 'cat', '%s', '{}', '\\', '*', '&',"{{", "}}", '[]',"''",'""','|','=','~']


def check_filter(input):
    input = input.lower()
    if input.count('.') > 1 or input.count(':') > 1 or input.count('/') > 1:
        return False
    if len(input) < 115:
        for char in input:
            if char in string.digits:
                return False
        for i in UNALLOWED:
            if i in input:
                return False
        return True
    return False