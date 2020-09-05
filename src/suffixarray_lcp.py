class SuffixArray():
    def __init__(self, magic_string):
        self.magic_string = magic_string
        self.size = len(magic_string)
        self.suffix_array = []
        self.suftab = []
        self.sufinv = []
        self.lcp = []
        self.build_suffix_array()
    
    def build_suffix_array(self):
        for i in range(0, len(self.magic_string)):
            self.suffix_array.append([self.magic_string[i:], i])
        print(self.suffix_array)
        self.suffix_array = sorted(self.suffix_array) #Python's sorted uses TimSort so O(nlogn)
        print(self.suffix_array)
        self.suftab = []
        for j in range(0, len(self.suffix_array)):
            self.suftab.insert(j, self.suffix_array[j][1])
        #print(self.suffix_array, self.suftab, self.sufinv)
        for i, val in enumerate(self.suftab):
            self.sufinv.insert(val, i)
            #print(val, i, self.sufinv)
        length = 0
        n = len(self.suffix_array)
        for i in range(0, n):
            if self.sufinv[i] == n:
                length = 0
                #print(length)
                continue
            #if self.sufinv[i] > 0 :
            k = self.suffix_array[self.sufinv[i]-1][1]
            while i+length < n and k+length < n and \
                self.magic_string[i+length] ==  self.magic_string[k+length]:
                #print(self.magic_string[i+length], self.magic_string[k+length])
                length += 1
            self.lcp.insert(self.sufinv[i], length)
            #print(self.sufinv[i], length)
            if length > 0:
                length -= 1
        print(self.suffix_array, self.suftab, self.sufinv, self.lcp)

sa = SuffixArray("banana")
sa1 = SuffixArray("abaababbabbb$")
sa2 = SuffixArray("acaaacatat$")

from itertools import zip_longest, islice
def to_int_keys(l):
    """
    l: iterable of keys
    returns: a list with integer keys
    """
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    print(ls)
    index = {v: i for i, v in enumerate(ls)}
    print(index)
    return [index[v] for v in l]


def suffix_array(s):
    n = len(s)
    k = 1
    keys = to_int_keys(s)
    ans = [keys]
    while max(keys) < n-1 :
        keys = to_int_keys(
            list(zip_longest(keys, islice(keys, k, None), fillvalue=-1))
        )
        #print("w",list(zip_longest(keys, islice(keys, k, None), fillvalue=-1)))
        ans.append(keys)
        k << 1
    return ans

def lcp(sa, i, j):
    n = len(sa[-1])
    if i == j:
        return n-i
    k = 1 << (len(sa)-2)
    ans = 0
    for line in sa[-2::-1]:
        if i >= n or j >= n:
            break
        if line[i] == line[j]:
            ans ^= k
            i += k
            j += k
        k >>= 1
    return ans


print(lcp(suffix_array("banana"),2,4))
