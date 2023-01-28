# Step 3
# Get a list as input with strings that contains certain possible employee numbers 
# write the validate employee numbers into result list.
# For a valid employess number:
# 1. Exactly 6 digits.
# 2. With any possible prefix/subfix characters.

import re

res_list = []
pattern = '(?!000000)(?:^|\D)(\d{6})(?!\d)'
input_list = [
    "000000",
    "00001d",
    "9999911",
    "12345",
    "van123473",
    "100003",
    "van-d122333",
    "-909090-dan",
    "910101-van453",
    "2342",
    "fsdfg432",
    "232fsdf",
    "sfdsfsdfs",
    "van-123456-van",
    "sdf1234234d",
    "",
    " ",
    "sdf001122dddddd",
    "0987654321",
    "01234567890",
    "%$#980*(",
    "@#$876540",
    "+",
    "00011"
]

def find_employee(input_list):
    for i in input_list:
        res = re.search(pattern, i)
        if res:
            res_list.append(i)
    return res_list

print("The hostnames with a valid employee number are :\n", find_employee(input_list))
