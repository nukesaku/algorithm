# coding: utf-8 

def find_palindrome(text):
    textlen = len(text)
    for i in range(len(text)):
        if not text[i].isalnum():
            continue
        # ithは、文字列textの第i文字の添え字
        ith = i
        # hitは、第i文字と一致した文字の添え字
        hit = find_char(text, ith + 1, text[ith])
        #hit = find_last_char(text, ith + 1, text[ith], textlen - i - 1)
        while hit != -1:
            # psizeは、文字の並びの長さ
            psize = hit - ith + 1
            if is_palindrome(text, ith, psize):
                while ith < hit + 1:
                    print(text[ith], "")
                    ith += 1
                print()
                return
            hit = find_char(text, hit + 1, text[ith])
            #hit = find_last_char(text, hit + 1, text[ith], psize - 2)

def is_palindrome(chars, idx, size):
    l = idx
    r = idx + size - 1
    while l < r:
        while not chars[l].isalnum():
            l += 1
        while not chars[r].isalnum():
            r -= 1
        if chars[l].lower() != chars[r].lower():
            return 0
        l += 1
        r -= 1
    return 1

def find_char(st, idx, ch):
    for i in range(idx, len(st)):
        if ch.lower() == st[i].lower():
            return i
    return -1

def find_last_char(st, idx, ch, count):
    for i in range(idx + count - 1, idx - 1, -1):
        if ch.lower() == st[i].lower():
            return i
    return -1
print '#find_palindrome:'
#find_palindrome('abc0cbe')
find_palindrome('abc0cb1bc0cbe')
print '#is_palindrome:'+str(is_palindrome('abc0cbe', 1, 5))
print '#find_char:'+str(find_char('abc0cbe', 2, 'b'))
print '#find_last_char:'+str(find_last_char('abc0cbeb', 2, 'b', 8 - 1 - 1))
