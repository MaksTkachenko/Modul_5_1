import requests

# Виконання GET-запиту
response = requests.get('https://www.w3schools.com/python/default.asp')

# Перевірка статусу відповіді
if response.status_code == 200:
    # Виконання вмісту відповіді
    print(response.text)
else:
    print('Помилка запиту:', response.status_code)
