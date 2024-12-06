import requests

class GetIPInfo:
    """Class to interact with the IPinfo API."""
    def __init__(self, api_key: str):
        self.api_key = api_key

    def fetch_ipinfo(self, ip: str) -> dict:
        """Fetch IP information from IPinfo API."""
        url = f"https://ipinfo.io/{ip}?token={self.api_key}"
        response = requests.get(url)
        data = response.json()

        # Extract relevant privacy flags
        flags = data.get('privacy', {})
        
        return {
            'Country': data.get('country'),
            'Region': data.get('region'),
            'City': data.get('city'),
            'Org': data.get('org'),
            'Hosting': flags.get('hosting'),
            'VPN': flags.get('vpn'),
            'Proxy': flags.get('proxy'),
            'Tor': flags.get('tor'),
            'Anonymizer': flags.get('anonymous')
        }