import random
import subprocess
import sys
address_file = '../mecab/address_list.txt'
num_addresses = int(sys.argv[1])
# 住所リストの読み込み
with open(address_file, 'r', encoding='utf-8') as file:
    addresses = [line.strip() for line in file.readlines()]

# ランダムに住所を選択
selected_addresses = random.sample(addresses, num_addresses)
with open(sys.argv[2], 'w', encoding='utf-8') as file:
    file.write('\n'.join(selected_addresses))
