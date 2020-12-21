
def get_count(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i: i + len(s2)] == s2:
            count += 1
    return count


if __name__ == '__main__':
    s1 = "ABCOABD"
    s2 = "AB"
    print(get_count(s1, s2))
    print(s1.count(s2))