import pandas as pd
import json

from src.AbuseIP import AbuseIP
from src.GetIPInfo import GetIPInfo
import pandas as pd


pd.set_option('display.max_columns', None)  
pd.set_option('display.width', 1000)        
pd.set_option('display.max_colwidth', None) 


with open('config/config.json') as config_file:
    config = json.load(config_file)

def process_ips(ip_list: list, ipinfo_obj: GetIPInfo, abuseip_obj: AbuseIP) -> list:
    """
    Process a list of IP addresses by fetching data from both APIs.
    
    Parameters:
    ip_list (list): A list of IP addresses to process.
    ipinfo_obj (GetIPInfo): Instance of GetIPInfo class.
    abuseip_obj (AbuseIP): Instance of AbuseIP class.
    
    Returns:
    list: A list of dictionaries containing the combined results from both APIs.
    """
    results = []
    for ip in ip_list:
        ipinfo_data = ipinfo_obj.fetch_ipinfo(ip)
        abuseipdb_data = abuseip_obj.fetch_abuse_data(ip)
        
        result = {
            'IP': ip,
            **ipinfo_data,
            **abuseipdb_data
        }
        results.append(result)
    return results

def clean_ips(ip_list):
    """
    Removes the port from IP addresses if present, keeping everything before the last colon.

    Args:
        ip_list (list): List of IP addresses with or without ports.

    Returns:
        list: List of IP addresses without ports.
    """
    cleaned_ips = []
    for ip in ip_list:
        if ':' in ip:  
            ip = ip.rsplit(':', 1)[0]  
        cleaned_ips.append(ip)
    return cleaned_ips

def main():
    ip_list = [
        "8.8.8.8"
    ]

    # Option 2: Read IPs from a CSV file (uncomment the next line)
    df = pd.read_csv('data/ip_list.csv',header=None)
    #ip_list_csv = df[0].tolist()  
    #print(clean_ips(ip_list_csv))
    ipinfo_obj = GetIPInfo(config['IPINFO_API_KEY'])
    abuseip_obj = AbuseIP(config['ABUSEIPDB_API_KEY'])
    
    results = process_ips(ip_list_csv , ipinfo_obj, abuseip_obj)
    df = pd.DataFrame(results)
    print(df)


if __name__ == "__main__":
    main()
