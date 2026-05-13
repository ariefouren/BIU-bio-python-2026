###########    Code from chapter II.3   ###########

##f = open("./Mycobacterium_tuberculosis.txt")
##Mycobacterium_tuberculosis = f.read().replace("\n","")
##f.close()
##
##f = open("./Salmonella_enterica.txt")
##Salmonella_enterica = f.read().replace("\n","")
##f.close()

def common_substring_naive(s1, s2, k):
    ''' find a common substring of s1 and s2 of length k '''
    for i in range(len(s1) - k + 1):
        for j in range(len(s2) - k + 1):
            if s1[i:i + k] == s2[j:j + k]:
                return s1[i:i + k]  # return first match found
    return None


def common_substring_hash(s1, s2, k):
    ''' find a common length k substring of s1 and s2
        using Python built-in sets '''
    table = set()
    for i in range(len(s1) - k + 1):
        table.add(s1[i:i + k])

    for i in range(len(s2) - k + 1):
        if s2[i:i + k] in table:
            return s2[i:i + k]

    return None


def hash4strings(st):
    s = 0
    for c in st:
        s = (128*s + ord(c)) % (2**120 + 451)
    return s**2 % (2**120 + 451)


def common_substring_hash2(s1, s2, k):
    ''' find a common length k substring of s1 and s2
        using Python built-in sets '''
    if len(s2) < len(s1):
        s1, s2 = s2, s1

    table = set()
    for i in range(len(s1) - k + 1):
        table.add(s1[i:i + k])

    for i in range(len(s2) - k + 1):
        if s2[i:i + k] in table:
            return s2[i:i + k]

    return None


def common_substring_fingerprint(s1, s2, k):
    ''' find a common length k substring of s1 and s2
        using Python built-in sets and fingerprints to save memory '''
    if len(s2) < len(s1):
        s1, s2 = s2, s1

    table = set()

    for i in range(len(s1) - k + 1):
        fingerprint = hash(s1[i:i + k])
        table.add(fingerprint)

    for i in range(len(s2) - k + 1):
        fingerprint = hash(s2[i:i + k])
        if fingerprint in table:   # possible match
            if s2[i:i + k] in s1:  # sanity check
                return s2[i:i + k]
            else:
                print("ALMOST A FALSE POSITIVE:", s2[i:i + k])
    return None


def frequent_kmer(st, k):
    counters = dict()
    most_freq = ""
    max_freq = 0

    for i in range(len(st) - k + 1):
        if st[i:i + k] not in counters:
            counters[st[i:i + k]] = 1  # first time
        else:
            counters[st[i:i + k]] += 1  # found one more
            if max_freq < counters[st[i:i + k]]:
                max_freq = counters[st[i:i + k]]
                most_freq = st[i:i + k]

    return most_freq, max_freq


def common_substring_better(s1, s2, k):
    ''' find a common substring of s1 and s2 of length k '''
    for i in range(len(s1) - k + 1):
        if s1[i:i + k] in s2:
            return s1[i:i + k]
    return None



def longest_common_substring_bsearch(s1, s2):
    ''' using binary search on the length '''
    print("Starting binary search on length of common substring...")
    k = 1
    while common_substring_hash2(s1, s2, k) != None:
        print(k, "found")
        k *= 2

    print(k, "not found")

    print("\nSearching for lengths between", k // 2 + 1, "and", k - 1, "...")
    longest = k // 2
    low = k // 2 + 1
    high = k - 1
    while low <= high:
        mid = (low + high) // 2
        res = common_substring_hash2(s1, s2, mid)
        if res == None:
            print(mid, "not found")
            high = mid - 1
        else:
            print(mid, "found")
            low = mid + 1
            longest = mid

    longest_ss = common_substring_hash2(s1, s2, longest)
    print("Longest common substring of length", longest, ":", longest_ss)
