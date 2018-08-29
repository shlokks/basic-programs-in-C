def main():
    try:
        fh = open('Rven.txt')
    except IOError as e:
        print(e)
    else:
        for i in fh:
            print(i)