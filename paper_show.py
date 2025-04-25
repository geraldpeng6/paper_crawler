from flask import Flask, render_template, request, jsonify, url_for, redirect
import csv
import hashlib
import threading
import time
import os

app = Flask(__name__)

CSV_FILE = 'data.csv'
STATE_FILE = 'data_state.csv'

# 全局变量来存储收藏状态
favorites = []
hash_value = ""

# 读取CSV文件并存储数据
def read_csv():
    with open(CSV_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# 计算CSV文件的哈希值
def calculate_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# 读取哈希值和收藏状态
def read_state():
    global hash_value, favorites
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, mode='r', encoding='utf-8') as file:
            state = [line.strip().split(',') for line in file.readlines()]
            hash_value = state[0][0]
            favorites = [bool(int(x)) for x in state[0][1:]]
    else:
        hash_value = calculate_hash(CSV_FILE)
        favorites = [False] * len(read_csv())

# 写入哈希值和收藏状态
def write_state():
    global hash_value, favorites
    favorites_str = ','.join(map(str, map(int, favorites)))
    with open(STATE_FILE, mode='w', encoding='utf-8') as file:
        file.write(f"{hash_value},{favorites_str}\n")

# 定期保存状态的后台线程
def save_state_periodically(interval):
    while True:
        time.sleep(interval)
        write_state()

# 首页路由
@app.route('/', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    data = read_csv()
    start = (page - 1)
    end = start + 1
    current_page_data = [(row, favorites[i]) for i, row in enumerate(data[start:end])]
    next_page = url_for('index', page=page + 1) if (start + 1) < len(data) else None
    prev_page = url_for('index', page=page - 1) if page > 1 else None
    return render_template('index.html', data=current_page_data, next_page=next_page, prev_page=prev_page)

# 收藏文献路由
@app.route('/favorite', methods=['POST'])
def favorite():
    item_id = request.form.get('item_id')
    global favorites
    data = read_csv()
    index = next((i for i, x in enumerate(data) if x.get('Title') == item_id), None)
    if index is not None:
        favorites[index] = not favorites[index]
        write_state()  # 更新文件
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})

# 启动定期保存状态的后台线程
threading.Thread(target=save_state_periodically, args=(60,)).start()

# 运行应用
if __name__ == '__main__':
    read_state()  # 初始化状态
    app.run(debug=True)