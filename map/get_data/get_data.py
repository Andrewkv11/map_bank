import csv
import requests

cookies = {
    # your cokkies
    'user_region_id': '396',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://www.banki.ru/banks/bank/sberbank/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
}


def main():
    response = requests.get(
        'https://www.banki.ru/widget/ajax/bank_objects_by_filter.json?region_id[]=396&bank_id[]=322&type[]=office&type[]=branch&type[]=atm&limit=236',
        cookies=cookies,
        headers=headers,
    )

    all_data = response.json()['data']

    bank_atm_file = open('get_data/bank_atm.csv', 'w')
    writer_atm = csv.writer(bank_atm_file)
    writer_atm.writerow(['latitude', 'longitude', 'address'])

    bank_office_file = open('get_data/bank_office.csv', 'w')
    writer_office = csv.writer(bank_office_file)
    writer_office.writerow(['latitude', 'longitude', 'address'])

    for elem in all_data:
        latitude = elem['latitude']
        longitude = elem['longitude']
        address = elem['address']
        if elem['type'] == 'atm':
            writer_atm.writerow([latitude, longitude, address])
        if elem['type'] == 'office':
            writer_office.writerow([latitude, longitude, address])


if __name__ == '__main__':
    main()

