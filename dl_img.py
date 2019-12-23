import urllib.request
import time

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + ".jpg"
    urllib.request.urlretrieve(url, full_path)

url = "https://data.goteborg.se/TrafficCamera/v1.0/CameraImage/83a5905d-7889-4bae-bd6d-0a7e67f4f6af/6"
file_name = "6_Drottningtorget"
frame = 0

last_get = time.monotonic()
while True:
    current = time.monotonic()
    if current - last_get >= 60.0:
        last_get = current
        dl_jpg(url, "images/", file_name+str(frame))
        """ print(f"Frame: {frame}") """
        frame += 1
