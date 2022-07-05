from bs4 import BeautifulSoup
import requests
def download(url):
    cookies = {
        '_ga': 'GA1.2.1852638767.1651515736',
        'PHPSESSID': 'jkb9jlhl7hkmstvk5b8rhqcgah',
    }

    headers = {
        'authority': 'www.bestmp3converter.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://www.bestmp3converter.com',
        'referer': 'https://www.bestmp3converter.com/',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'type': 'mp3',
        'search_txt': url,
    }

    response = requests.post('https://www.bestmp3converter.com/models/convertProcess.php', cookies=cookies, headers=headers, data=data)
    soup = BeautifulSoup(response.content , 'html.parser')
    soup = soup.find_all('option')
    data = {}

    for i in soup:
        
        z = i.get('data-link')
        size = z.split('/')
        size = size[6]
        data[size] = z

    return data

