from file import Info
from table import TableMatrix

import os
import sys

args = sys.argv[1:]

fileinfos = map(Info, args)

# mem:
#   cells   Bytes   insert_duration (nanoseconds)

# retr:
#   retrieval_duration (nanoseconds)

# filter out so we're only left with "mem" files.
fileinfos = list(filter(lambda i: i.kind == "mem", fileinfos))

# no need for pandas or anything fancy. we will just grab the last section

def read_last_line(filename):
    file = open(filename, "r")
    lastline = file.readlines()[-1]
    file.close()

    return lastline

def split_csv(line: str, sep=";"):
    line.split(sep)

def col_bytes(csv: list[str]):
    cells, bytes, insert_duration_nanosec = csv
    return bytes

# (count, table) => (algorithm, total_size)
bytes_per_file = dict()

for file in fileinfos:
    size_in_bytes = col_bytes(split_csv(read_last_line(file.filename)))

    # nice, we have the size in bytes

    # now we would like to generate a matrix

    # A SET OF MATRICES (bytesSize x byteSize)

    # GROUPED BY (COUNT, TABLE)

    bytes_per_file[(file.count, file.table)] = (file.algo, size_in_bytes)

# (count, table) => Matrix(algo x algo => compression rate)
matrices = dict()

for (count, table),v in bytes_per_file.items():
    # stable order for matrix
    v.sort()

    algos = list(map(lambda i: i[0], v))

    matrix = TableMatrix(rows=algos, cols=algos)

    for (row,bytes) in v:
        for (col,bytes2) in v:
            ration = bytes / bytes2
            matrix.set(row, col, value)

    matrices[(count, table)] = matrix

for (count, table), m in matrices:
    filename = f"{count}--{table}.md"
    f = open(filename, 'w')
    f.write(m.markdown())
    f.close()
