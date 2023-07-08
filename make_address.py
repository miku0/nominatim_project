import random
import subprocess
import sys
address_file = '../mecab/address_list.txt'
num_addresses = int(sys.argv[1])
# read addresses
with open(address_file, 'r', encoding='utf-8') as file:
    addresses = [line.strip() for line in file.readlines()]

# choose addresses randomly
selected_addresses = random.sample(addresses, num_addresses)
with open(sys.argv[2], 'w', encoding='utf-8') as file:
    file.write('\n'.join(selected_addresses))
