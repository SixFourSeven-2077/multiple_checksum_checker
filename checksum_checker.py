#!/usr/bin/env python3
import sys
import hashlib
import os

# Thanks to Nathan McBride for parts of the code

BUFFER_SIZE = 128000  # lets read stuff in 128kb chunks!
hash_table_file = sys.argv[1]
hash_type = os.path.splitext(hash_table_file)[1].replace('.', '')
hash_table = []


def reset_hash():
    new_hash = None
    if hash_type.lower() == "sha512":
        new_hash = hashlib.sha512()
    elif hash_type.lower() == "sha256":
        new_hash = hashlib.sha256()
    elif hash_type.lower() == "sha1":
        new_hash = hashlib.sha1()
    elif hash_type.lower() == "md5":
        new_hash = hashlib.md5()
    else:
        print('Unsupported hash table')
        exit(-1)
    return new_hash


config_hash = reset_hash()
print("Using {0} hash".format(hash_type.upper()))
with open(hash_table_file, 'r') as hash_table_contents:
    for line in hash_table_contents.readlines():
        cut_line = line.split()
        hash_table.append([cut_line[0], cut_line[1]])

print("Loaded {0} hashes".format(len(hash_table)))
validations = 0
for hash_pair in hash_table:
    expected_hash = hash_pair[0]
    file_path = hash_pair[1].replace('*', '.\\')
    print('Checking', expected_hash, file_path)
    with open(str(file_path), 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            config_hash.update(data)
    Hash_Result = str.format(config_hash.hexdigest())
    if Hash_Result == expected_hash:
        print('OK')
        validations += 1
    config_hash = reset_hash()
print('Total files checked', len(hash_table))
print('Total files validated', validations)
print('Total files not validated', len(hash_table) - validations)
