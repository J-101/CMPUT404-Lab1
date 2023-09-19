import requests

# print(requests.__version__)

# resp = requests.get("http://google.com")

# print(resp.text)

resp2 = requests.get("https://raw.githubusercontent.com/J-101/CMPUT404-Lab1/main/lab1.py")
print(resp2)