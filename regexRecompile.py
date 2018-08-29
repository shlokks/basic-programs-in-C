import re
def main():
    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore',re.I)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('####',line),end = '')
        