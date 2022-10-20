import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, user_input):
    headers = {
        'Authorization': """Bearer {token}""".format(token = token),
     }
    long_url = {"long_url": user_input}
    response = requests.post("""{url}/v4/shorten""".format(
        url = user_input), headers = headers, json = long_url)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, user_input):
    headers = {
        'Authorization': f"Bearer {token}",
     }
    params = (
        ('unit', 'month'),
        ('units', '-1'),
     )
    disassembled_url = urlparse(user_input)
    net_loc = disassembled_url.netloc
    path = disassembled_url.path
    response = requests.get("""https://api-ssl.bitly.com/v4/bitlinks/
{net_loc{path}/clicks/summary""".format(net_loc = net_loc, path = path),
headers = headers, params = params)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']

    return clicks_count


def is_bitlink(token, user_input):
    headers = {
        'Authorization': """Bearer {token}""".format(token = token),
     }
    disassembled_url = urlparse(user_input)
    net_loc = disassembled_url.netloc
    path = disassembled_url.path
    response = requests.get("""https://api-ssl.bitly.com/v4/bitlinks/
{net_loc}{path}""".format(net_loc=net_loc, path=path), headers=headers)
    return response.ok


def main():

    load_dotenv()
    parser = argparse.ArgumentParser('Введите ссылку:')
    parser.add_argument("link", help='')
    args = parser.parse_args()
    user_input = args.link
    token = os.environ["BITLY_TOKEN"]
    if is_bitlink(token, user_input):
        print('По вашей ссылки прошли:',
              count_clicks(token, user_input), 'раза', end='\n')
    else:
        print('Битлинк', shorten_link(token, user_input))


if __name__ == "__main__":
    main()



