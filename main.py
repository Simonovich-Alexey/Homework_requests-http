import requests


def search_superhero(url_super, *superheroes_search):
    response_super = requests.get(url_super)
    if 200 <= response_super.status_code <= 300:
        data = response_super.json()
        superheroes = []
        for i in data:
            if i['name'] in superheroes_search:
                name_superheroes = i['name']
                intelligence_superheroes = i['powerstats']['intelligence']
                superheroes.append({'name': name_superheroes, 'intelligence': intelligence_superheroes})
        superheroes_sorted = sorted(superheroes, key=lambda x: x['intelligence'], reverse=True)
        return f"Самый умный супергерой: {superheroes_sorted[0]['name']}"


def get_token_disc():
    with open("sourse/token.txt") as file:
        token = file.read()
        return token


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        file_name = file_path.split('/')
        params = {'path': '/' + file_name[-1]}
        headers = {"Authorization": "OAuth " + self.token}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        try:
            url = data['href']
            with open(file_path, 'rb') as f:
                requests.post(url, files={'file': f})
            print(f"{file_name[-1]} ----------> disc")
        except KeyError:
            print('Файл с таким именем есть на диске')


if __name__ == '__main__':

    print(search_superhero("https://akabab.github.io/superhero-api/api/all.json", "Hulk", "Captain America", "Thanos"))

    path_to_file = 'file_to_disc/36182.jpg'
    uploader = YaUploader(get_token_disc())
    result = uploader.upload(path_to_file)
