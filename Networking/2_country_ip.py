"""
Country from IP Lookup - Enter an IP address and find the country that IP is registered in.

https://github.com/karan/Projects
"""

from json import load
from urllib.request import urlopen

GOOGLE = "142.250.190.100"

def get_country(ip_address: str) -> str:
    url = f"http://ipinfo.io/{ip_address}/json"
    data = load(urlopen(url))
    return data['country']

print(get_country(GOOGLE))