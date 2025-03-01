import time
from rich.progress import track

for i in track(range(20), description="Processing..."):
    print(i)
    time.sleep(1)