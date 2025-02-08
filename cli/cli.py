import socket
import threading
import argparse
import sqlite3
import time
from loading import show_loading_animation

# 端口扫描函数
def scan_port(ip, port, results, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        if result == 0:
           results.append(f"Port {port}: Open")
        sock.close()
    except Exception as e:
        results.append(f"Port {port}: Error - {str(e)}")

# 端口扫描（多线程）
def start_scan(ip, start_port, end_port, timeout=1, bar_style=1):
    results = []
    threads = []

    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")

    # 启动加载动画（支支持自定义样式）
    loading_thread = threading.Thread(target=show_loading_animation, args=(bar_style,))
    loading_thread.start()

for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port, results, timeout))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
      # 停止加载动画
    global loading
    loading = False
    loading_thread.join()

    print("\nScan complete!")
    for result in results:
        print(result)
      return results

# 结果存入 SQLite
def save_results(ip, results):
    conn = sqlite3.connect("../scanner_history.db")
    cursor = conn.cursor()
    cursor.execute ('''CREATE TABLE IF NOT EXISTS scan_history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ip TEXT,
                        port INTEGER,
                        status TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    for result in results:
    port_status = result.split(": ")
        cursor.execute("INSERT INTO scan_history (ip, port, status) VALUES (?, ?, ?)", (ip, port_status[0], port_status[1]))

    conn.commit()
    conn.close()   
    # 命令行参数解析
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="命令行端口扫描工具（功能与 Web 版一致）")
    parser.add_argument("ip", help="目标 IP 地址")
    parser.add_argument("start_port", type=int, help="起始端口")
    parser.add_argument("end_port", type=int, help="结束端口")
    parser.add_argument("--timeout", type=int, default=1, help="端口扫描超时时间（秒）")
    parser.add_argument("--bar_style", type=int, default=1, help="加载动画样式（1-3）")
    parser.add_argument("--save", action="store_true", help="是否保存扫描结果到数据库")

    args = parser.parse_args()
    scan_results = start_scan(args.ip, args.start_port, args.end_port, args.timeout, args.bar_style)

    if args.save:
    save_results(args.ip, scan_results)
        print("\n扫描结果已保存到数据库！")