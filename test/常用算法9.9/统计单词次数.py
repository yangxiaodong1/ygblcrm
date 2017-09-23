# Author : July  Yang 
import re
def findTopFreqWords(filename, num=1):
    'Find Top Frequent Words:'
    fp = open(filename, 'r')
    text = fp.read()
    fp.close()

    lst = re.split('[0-9\W]+', text)

    # create words set, no repeat
    words = set(lst)
    d = {}
    for word in words:
        d[word] = lst.count(word)
    del d['']

    result = []
    for key, value in sorted(d.items(), key=lambda k, v: (v, k), reverse=True):
        result.append((key, value))
    return result[:num]


def test():
    topWords = findTopFreqWords('test.txt', 10)
    print
    topWords


if __name__ == '__main__':
    test()






