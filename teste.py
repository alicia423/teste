# system_monitor.py
import psutil
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    
    # CPU
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_freq = psutil.cpu_freq()
    
    print("=" * 50)
    print("CPU")
    print("=" * 50)
    print(f"Frequência: {cpu_freq.current:.0f} MHz")
    for i, percent in enumerate(cpu_percent):
        bar = "█" * int(percent / 2)
        print(f"Core {i}: [{bar:<50}] {percent}%")
    
    # RAM
    ram = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    print("\n" + "=" * 50)
    print("MEMÓRIA")
    print("=" * 50)
    print(f"RAM: {ram.used / 1024**3:.1f} GB / {ram.total / 1024**3:.1f} GB ({ram.percent}%)")
    print(f"Virtual: {swap.used / 1024**3:.1f} GB / {swap.total / 1024**3:.1f} GB ({swap.percent}%)")
    
    # Disco
    disk = psutil.disk_usage('C:\\')
    disk_io = psutil.disk_io_counters()
    
    print("\n" + "=" * 50)
    print("DISCO")
    print("=" * 50)
    print(f"Usado: {disk.used / 1024**3:.1f} GB / {disk.total / 1024**3:.1f} GB ({disk.percent}%)")
    print(f"Leitura: {disk_io.read_bytes / 1024**2:.1f} MB")
    print(f"Escrita: {disk_io.write_bytes / 1024**2:.1f} MB")
    
    # Top processos
    print("\n" + "=" * 50)
    print("TOP 5 PROCESSOS")
    print("=" * 50)
    for proc in sorted(psutil.process_iter(['name', 'cpu_percent', 'memory_percent']), 
                      key=lambda p: p.info['cpu_percent'], reverse=True)[:5]:
        print(f"{proc.info['name'][:30]:<30} CPU: {proc.info['cpu_percent']:>5.1f}% RAM: {proc.info['memory_percent']:>5.1f}%")
    
    time.sleep(2)
