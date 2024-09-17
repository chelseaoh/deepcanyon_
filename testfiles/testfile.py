from datetime import datetime

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

dateandtime = get_datetime()
file_path = f'/home/deepcanyonnrs/{dateandtime}.jpg'

print("file path for capture:", file_path)