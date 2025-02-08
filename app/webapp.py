from flask import Flask, render_template, request, jsonify
import threading
import time
import socket
import sqlite3
from utils import init_db
app = Flask(__name__)

# 初始化数据库
init_db()
# 端口扫描函数
def scan_port(ip, start_port, end_port, results, progress):
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                status = "Open"
            else:
                status = "Closed"
            results.append(f"Port {port}: {status}")
            progress[0] += 1
        except Exception as e:
            results.append(f"Port {port}: Error - {str(e)}")
        finally:
            sock.close()
   # 扫描接口
@app.route('/scan', methods=['POST'])
def start_scan():
    ip = request.form['ip']
    start_port = int(request.form['start_port'])
    end_port = int(request.form['end_port'])

    results = []
    progress = [0]  #用于进度条

    # 启动多线程进行端口扫描
    threads = []
    for port in range(start_port, end_port + 1, 10):  # 每次扫描10个端口
        t = threading.Thread(target=scan_port, args=(ip, port, min(port+9, end_port), results, progress))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return jsonify({"status": "done", "results": results, "progress": progress[0]})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)