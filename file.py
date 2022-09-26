
class Info:
    def __init__(self, s: str):
        count, table, algo, kind = parse_filename(s)

        self.kind = kind # 'mem' | 'retr'
        self.count = count
        self.table = table
        self.algo = algo
        self.filename = s

def parse_magnitude(s):
    i = 0
    for c in s:
        if not (c >= '0' and c <= '9'):
            break
        i+=1


    n = int(s[:i])

    if len(s) <= i:
        return n, ""

    m = s[i]

    if m == "k":
        i += 1
        n *= 1_000
    if m == "M":
        i += 1
        n *= 1_000_000
    if m == "G":
        i += 1
        n *= 1_000_000_000

    return n, s[i:]


def parse_filename(s: str):
    # separate basepath from filename
    s = s.rsplit("/", maxsplit=1)[-1]


    if not s.endswith('.csv'):
        raise Exception("not a csv file")

    # cut of .csv part
    s = s[:-4]

    kind = ""
    if s.endswith("-mem"):
        # memory stats
        kind = "mem"
        s = s[:-4]
    if s.endswith("-retr"):
        kind = "retr"
        s = s[:-5]

    count,table,algo = s.split("-", maxsplit=2)

    magn, _rest = parse_magnitude(count)
    return magn,table, algo, kind


def __test_magnitude():
    count, rest = parse_magnitude("55k-hello")
    assert rest == "-hello"
    assert count == 55_000

    count, rest = parse_magnitude("70M")
    assert rest == ""
    assert count == 70_000_000

def __test_parse_filename():
    s = "./4k-gittables_main_tokenized-duplicate-hash-mem.csv"

    i = Info(s)

    assert i.kind == "mem"
    assert i.algo == "duplicate-hash"
    assert i.table == "gittables_main_tokenized"
    assert i.count ==  4000

if __name__ == '__main__':
    __test_magnitude()
    __test_parse_filename()
    print("all tests passed")
