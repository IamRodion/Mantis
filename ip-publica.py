import requests
import logger

def get_my_ip(): # This function returns the public IP address of the machine.
    CHECK_IP_URL = 'http://checkip.amazonaws.com'
    try:
        TIMEOUT = 5
        ip = requests.get(CHECK_IP_URL, timeout=TIMEOUT).text.strip()
        return ip
    except requests.exceptions.Timeout as e:
        logger.error("Timeout error: %s", e)
        ip = None
        return ip
    except requests.exceptions.RequestException as e:
        logger.error("Request error: %s", e)
        ip = None
        return ip

get_my_ip()
