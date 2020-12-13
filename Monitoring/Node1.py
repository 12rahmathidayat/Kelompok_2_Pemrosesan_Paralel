import psutil
import netiface as ni

psutil.cpu_percent()
ni.ifaddresses('enp0s3')
cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().used/psutil.virtual_memory().total
tx_current = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_sent
rx_current = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_recv
ip = ni.ifaddresses('enp0s3')[ni.AF_INET[0]['addr']

print("IP\t:",ip)
print(f"CPU\t: {psutil.cpu_percent(interval=1)}%")
print(f"Memory\t: {round((memory * 100), 2)}%")
print(f"Tx\t: {tx_current} bytes")
print(f"Rx\t: {rx_current} bytes")
print()
