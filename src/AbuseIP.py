import requests

class AbuseIP:
    """Class to interact with the AbuseIPDB API."""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.abuseipdb.com/api/v2/check"

    def fetch_abuse_data(self, ip: str) -> dict:
        """Fetch abuse information from AbuseIPDB API."""
        headers = {
            'Key': self.api_key,
            'Accept': 'application/json'
        }
        params = {'ipAddress': ip, 'maxAgeInDays': 90}
        response = requests.get(self.base_url, headers=headers, params=params)
        data = response.json()
        
        return {
            'AbuseIPDB_Score': data['data']['abuseConfidenceScore'],
            'Total_Reports': data['data']['totalReports']
        }