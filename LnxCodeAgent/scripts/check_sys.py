import psutil

def get_disk_usage():
    disk = psutil.disk_usage('/')
    free_gb = (disk.free / 1024**3)
    return free_gb

def get_memory_usage():
    memory = psutil.virtual_memory()
    free_gb = (memory.available / 1024**3)
    return free_gb

if __name__ == "__main__":
    print(f"Свободное место на диске: {get_disk_usage()} ГБ")
    print(f"Свободная оперативная память: {get_memory_usage()} ГБ")