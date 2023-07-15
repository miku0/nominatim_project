import subprocess
import sys
import time
import csv

address_file = sys.argv[1]
# read addresses
with open(address_file, 'r', encoding='utf-8') as file:
    addresses = [line.strip() for line in file.readlines()]

# run the command of query
results = []

def run_nominatim_search(address):
    #command = f'/usr/local/bin/nominatim search --query "{address}"'
    command = f'~/Nominatim/build/nominatim search --query "{address}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def count_search_results(addresses):
    for address in addresses:
        output = run_nominatim_search(address)
        result_count = output.count('{')
        results.append(result_count)
        #print(f'Address: {address}, Result Count: {result_count}')
        #print(results)

def write_to_csv(address, result_count):
    filename = 'result1_with_count.csv' if result_count == 0 else 'result2_without_count.csv'

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([address, result_count])

start_time = time.time()
count_search_results(addresses)
# speed
end_time = time.time()
elapsed_time = end_time - start_time
print(f"time: {elapsed_time}sec.")

for addr, count in zip(addresses, results):
    write_to_csv(addr, count)
