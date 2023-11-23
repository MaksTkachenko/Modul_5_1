import requests
import time

locale_date_now = time.localtime()  # current time
date_string = time.strftime("%Y%m%d", locale_date_now)


def get_exchange_rates(valuta_1, valuta_2, total):

    try:
        r_1 = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valuta_1}&date={date_string}&json')
        r_2 = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valuta_2}&date={date_string}&json')

        info_val_1 = r_1.json()
        info_val_2 = r_2.json()

        cc_val_1 = info_val_1[0]['cc']
        rate_val_1 = info_val_1[0]['rate']

        cc_val_2 = info_val_2[0]['cc']
        rate_val_2 = info_val_2[0]['rate']

        convert = (total * rate_val_1) / rate_val_2
        print(f"{total} {cc_val_1} = {round(convert, 2)} {cc_val_2}")

    except Exception as ex:
        print(ex)


def main():
    print("Example of currency names: USD, EUR, CAD, UAH, PLN, AUD, JPY, ZAR...")
    val_1 = input("Enter the currency you want to sell: ")
    val_2 = input("Enter the currency you want to buy: ")
    total = float(input("Enter the amount you want to convert: "))
    get_exchange_rates(val_1, val_2, total)


if __name__ == '__main__':
    main()
