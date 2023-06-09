# Python Multiple checksum checker

This little script was made because I needed a tool to check multiple files SHA1 hashes with the help of a SHA1 table.
This tool probably works if your table looks like this :

| hash1 | file path            |

| hash2 | another file path    |

| hash3 | wow again a file path|


It reads the checksum from the file extension of the table, reads the contents expecting the first part to be the expected hash, while the second is the path.
It loops in the lines and gets the checksum from the path, calculates the hash and compares it to the expected hash.

# Usage

`checksum_checker.py <path to the table file>`
If the paths in the hash table file are relative, make sure to put the script in the correct folder.
