import nmap
import asyncio
import logging

# 初始化 Nmap 扫描器
nm = nmap.PortScanner()

# 配置日志
logging.basicConfig(filename="scanner.log", level=logging.INFO)

async def run_scan(host: str, ports: str = None, scan_type: str = "tcp", custom_args: str = ""):
    """
    执行端口扫描或 OS 检测
    :param host: 目标主机
    :param ports: 需要扫描的端口（可选）
    :param scan_type: 扫描类型（tcp/udp/os）
    :param custom_args: 自定义 Nmap 参数
    :return: 扫描结果
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, scan, host, ports, scan_type, custom_args)

def scan(host, ports, scan_type, custom_args):
    """
    Nmap 扫描逻辑
    """
    try:if scan_type == "tcp":
            args = f"-p {ports}" if ports else "-p 1-65535"
        elif scan_type == "udp":
            args = f"-sU -p {ports}" if ports else "-sU"
        elif scan_type == "os":
            args = "-O"
        else:
            args = custom_args  # 用户自定义参数

        logging.info(f"Scanning {host} with args: {args}")
        result = nm.scan(hosts=host, arguments=args)
        return result
    except Exception as e:
        logging.error(f"Error scanning {host}: {str(e)}")
        return {"error": str(e)}
