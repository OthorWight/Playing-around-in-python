import wikipedia
import re

def get_page_sumarries(page_name):
    try:
        return [[page_name, wikipedia.page(page_name).summary]]
    except wikipedia.exceptions.DisambiguationError as e:
        return [[p, wikipedia.page(p).summary] for p in e.options]

def get_random_pages_summary(pages=0):
    ret = []
    page_names = [wikipedia.random(1) for i in range(pages)]
    for p in page_names:
        for page_summary in get_page_sumarries(p):
            ret.append(page_summary)
    return  ret

text = get_random_pages_summary(1)
text = text[0]
t = text[0]
s = text[1]
regex = re.compile('[^a-zA-Z ]')
s = regex.sub('', s)
s = s.split(' ')
s = sorted(s,key=len)
print(t)
print(s)