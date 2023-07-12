import requests


def get_token():
    with open("sourse/token.txt") as file:
        token = file.read()
        return token


url = 'https://cloud-api.yandex.net/v1/disk/resources'
params = {"path": "/"}
headers = {"Authorization": "OAuth " + get_token()}

response = requests.get(url, headers=headers, params=params)

if __name__ == '__main__':
    print(response.status_code)
    if 200 <= response.status_code <= 300:
        print(f'Content : {response.content}')
        print(f'Text : {response.text}')
        data = response.json()
        print(f'JSON : {data}')

        url_d = data["_embedded"]["items"][2]["file"]
        requests.get(url_d)
