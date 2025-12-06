
def sort_dict(d):
    l = []
    for k, v in d.items():
        l.append({ "char": k, "num": v})
    return sorted(l, key=lambda d: d['num'])


def get_char_count(text):
    text = text.lower()
    d = {}
    for x in text:
        if not x.isalpha():
            continue
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d

def get_book_text(filename):
    with open(filename) as f:
        content = f.read()
    return content

def get_num_words(text):
    if text:
        return len(text.split())
    else:
        return 0

