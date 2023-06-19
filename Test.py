import requests

def main():
    res = requests.get('https://github.com/corincerami/mars-photo-api')
    print(res.json())

main()