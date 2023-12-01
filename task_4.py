import requests
from PIL import Image
from io import BytesIO
from pprint import pprint

api_key = 'MqYnTKmtSbPeLFI8lr5l6j6zXwxmVLPRC6V99dsiqjAST4B4ksz8migD'


def search_image(query):
    url = 'https://api.pexels.com/v1/search'
    headers = {
        'Authorization': api_key
    }
    params = {
        'query': query, 'per_page': 1
    }

    # Executing a query and getting results
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    # pprint(data)

    image_url = data['photos'][0]['src']['original']

    # Uploading a photo
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))

    image.save(f'{query}_photo.jpg')

    image.show()


if __name__ == "__main__":
    search_query = input("Enter a keyword to search for a photo: ")
    search_image(search_query)
