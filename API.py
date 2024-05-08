import requests
import webbrowser

# Ваш API ключ от Яндекс Геокодера
API_KEY = '91b59a1d-6bec-4669-a7eb-207b47db0092'


def get_geocode_info(address_or_coordinates, api_key):
    geocoder_api_server = "https://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": api_key,
        "geocode": address_or_coordinates,
        "format": "json"
    }
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        toponym_coordinates = toponym["Point"]["pos"]
        try:
            toponym_postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
        except KeyError:
            toponym_postal_code = "Почтовый индекс не найден"
        return toponym_address, toponym_coordinates.replace(' ', ','), toponym_postal_code
    else:
        return None, None, None


def show_map(coordinates):
    map_api_server = "https://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": coordinates,
        "z": "10",
        "l": "map",
        "pt": f"{coordinates},pm2dgl"
    }
    response = requests.get(map_api_server, params=map_params)
    if response:
        map_url = response.url
        webbrowser.open(map_url)


address, coordinates, postal_code = get_geocode_info('Саратов, Лисина, 6, 157', API_KEY)
if address and coordinates:
    print(f'Адрес: {address}\nКоординаты: {coordinates}\nПочтовый индекс: {postal_code}')
    show_map(coordinates)
else:
    print("Не удалось получить информацию.")



# Токен доступа к Яндекс Диску
token = 'y0_AgAAAABiDQqKAAu_zAAAAAEEMW-hAAB8n97KUi5I-L4VAulh0TmAyY5uXA'

# Создание заголовков для запроса
headers = {
    "Authorization": f"OAuth {token}"
}

# Создание папки
create_folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
params = {"path": "Название_вашей_папки"}
response = requests.put(create_folder_url, headers=headers, params=params)

if response.status_code == 201:
    print("Папка успешно создана")
else:
    print(f'Ошибка: {response.status_code} ({response.reason})')
