import re

def main():
    fh = open('raven.txt')
    for line  in fh:
        match =  re.search('raven',line)
        if match:
            print(enumerate(fh),match.group())
            
            
            