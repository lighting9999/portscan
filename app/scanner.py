import nmap
import asyncio

nm = nmap.PortScanner()

def port_scan(host, ports):
    return nm.scan(hosts=host, arguments=f'-p {ports}')

def ping_scan(host):
    return nm.scan(hosts=host, arguments="-sn")
    
async def run_port_scan(host, ports):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, port_scan, host, ports)

async def run_ping_scan(host):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, ping_scan, host)