import random
import subprocess
import time
import sys

address_file = sys.argv[1]
command_template = "~/Nominatim/build/nominatim search --query '{}' --format debug | grep -c '\. Search:'"
query_placeholder = '神奈川県幸区南加瀬3丁目8-33'
#num_addresses = 2

# 住所リストの読み込み
with open(address_file, 'r', encoding='utf-8') as file:
    selected_addresses = [line.strip() for line in file.readlines()]

# コマンドのクエリ部分を置換して実行
start_time = time.time()
results = []
for address in selected_addresses:
    command = command_template.format(address)
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL).decode("utf-8").strip()
        result = int(output.split("\n")[-1])
        #print(f'住所: {address}\t検索結果: {result}件')
        results.append(f'{address} {result}')
    except subprocess.CalledProcessError:
        results.append(f'{address} false')
        #print(f'住所: {address}\t検索結果の取得に失敗しました')
end_time = time.time()
elapsed_time = end_time - start_time
#print('処理が完了しました。')
with open('results.dat', 'w', encoding='utf-8') as file:
    file.write('\n'.join(results))
print(f"time: {elapsed_time}秒")
