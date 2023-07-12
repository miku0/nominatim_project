def process_dat_files(base_file, comparison_files, output_file):
    data = {}

    # Load base file data
    with open(base_file, 'r') as file:
        for line in file:
            line = line.strip()
            key, value = line.rsplit(' ', 1)
            if value.lower() == 'false':
                value = False
            else:
                value = int(value)
            data[key] = [value]

    # Compare with other files
    for file_path in comparison_files:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                key, value = line.rsplit(' ', 1)
                if value.lower() == 'false':
                    value = False
                else:
                    value = int(value)
                if key in data:
                    if data[key][0] is False or value is False:
                        data[key].append(value)
                    else:
                        data[key].append(data[key][0] - value)

    # Generate output file
    with open(output_file, 'w') as file:
        for key, values in data.items():
            file.write(f'{key} {" ".join(str(value) for value in values)}\n')

# file path
base_file = 'results_normal.dat'
comparison_files = ['results1.dat', 'results2.dat', 'results3.dat']
output_file = 'comparison.dat'

process_dat_files(base_file, comparison_files, output_file)
