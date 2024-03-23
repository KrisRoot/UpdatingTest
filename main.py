import requests

current_version = int(open('version.txt').readlines()[0].rstrip())

print(f"Version: {current_version}")

