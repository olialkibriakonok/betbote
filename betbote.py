import requests
import re
import time
import sys
from colorama import Fore, init
from tqdm import tqdm
import random
import argparse

init(autoreset=True)

BANNER = f"""
{Fore.GREEN}██████╗ ███████╗████████╗ ██████╗  ██████╗ ███████╗███████╗
{Fore.GREEN}██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗╚════██║██╔════╝
{Fore.GREEN}██████╔╝█████╗     ██║   ██████╔╝██║   ██║   ██╔══╝ █████╗  
{Fore.GREEN}██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║   ██║    ██╔══╝  
{Fore.GREEN}██████╔╝███████╗   ██║   ██████╔╝╚██████╔╝   ██║    ███████╗
{Fore.GREEN}╚═════╝ ╚══════╝   ╚═╝   ╚═════╝  ╚═════╝    ╚═╝    ╚══════╝
{Fore.GREEN}--------------------------------------------------------------
{Fore.GREEN}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
{Fore.CYAN}Tool Owner - Olial Kibria Konok
"""

EXPECTED_OWNER_TEXT = "Tool Owner - Olial Kibria Konok"

def check_owner_text():
    """Checks if the Tool Owner text has been altered."""
    if EXPECTED_OWNER_TEXT != "Tool Owner - Olial Kibria Konok":
        raise ValueError(f"{Fore.RED}❌ Error: Tool owner text has been altered!")
    else:
        print(f"{Fore.GREEN}✔️ Tool is valid.")

HEROKU_API_URL = "https://api.heroku.com/account"

HEADERS_TEMPLATE = {
    "Accept": "application/vnd.heroku+json; version=3",
    "Authorization": "Bearer {}",
}

MAX_RETRIES = 5

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.64 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
]

def extract_api_key(line):
    """Extracts API key from both formats:
       1. Heroku API KEY  ->      8d684795-2b95-4d62-aa2b-8fdf99678b37
       2. 8d684795-2b95-4d62-aa2b-8fdf99678b37"""
    match = re.match(r"(Heroku API KEY\s+->\s+)?([a-f0-9\-]+)", line.strip())
    if match:
        return match.group(2)  
    return None

def check_key(api_key):
    """Checks the validity of a Heroku API key and returns the full details if valid."""
    headers = {k: v.format(api_key) if "{}" in v else v for k, v in HEADERS_TEMPLATE.items()}
    headers["User-Agent"] = random.choice(USER_AGENTS) 

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(HEROKU_API_URL, headers=headers, timeout=10)

            if response.status_code == 200:
                data = response.json()
                email = data.get("email", "Unknown")
                user_id = data.get("id", "Unknown")
                
                return True, f"VALID: Email: {email}, ID: {user_id}, Full Key: {api_key}, Endpoint: {HEROKU_API_URL}"
            elif response.status_code == 401:
                return False, f"{Fore.RED}❌ Unauthorized - Invalid API key"
            elif response.status_code == 403:
                return False, f"{Fore.RED}❌ Forbidden - Access Denied"
            elif response.status_code == 404:
                return False, f"{Fore.RED}❌ Not Found - Endpoint Issue"
            elif response.status_code == 429:
                return False, f"{Fore.RED}❌ Rate Limit Exceeded"
            else:
                return False, f"{Fore.YELLOW}⚠️ Unexpected Error - Status Code: {response.status_code}"

        except requests.RequestException as e:
            print(f"{Fore.YELLOW}Attempt {attempt}/{MAX_RETRIES} failed. Retrying...")
            time.sleep(2 ** attempt)
    return False, f"{Fore.RED}❌ Network Error - Max Retries Exceeded"

def show_help():
    """Displays help instructions."""
    print(f"""
{Fore.CYAN}Usage: python validate_heroku_keys.py [options]

{Fore.GREEN}Options:
    {Fore.YELLOW}--help      {Fore.WHITE}Show this help message

{Fore.MAGENTA}This tool validates Heroku API keys by checking if they are authorized to access Heroku services.
It will attempt up to 5 retries for any failed network requests.
""")

def validate_api_keys(file_location):
    """Validates the API keys from the provided file.""" 
    try:
        print(BANNER)
        check_owner_text()

        with open(file_location, "r") as file:
            lines = file.readlines()

        total_keys = len(lines)
        print(f"{Fore.GREEN}Found {total_keys} keys to process.\n")

        valid_keys = []
        with tqdm(total=total_keys, desc="Validating API Keys", ncols=100, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} {elapsed}") as pbar:
            for i, line in enumerate(lines, start=1):
                api_key = extract_api_key(line.strip())  
                if not api_key:
                    print(f"{Fore.RED}[{i}/{total_keys}] ❌ INVALID FORMAT: {line.strip()}")
                    pbar.update(1)
                    continue

                print(f"{Fore.YELLOW}[{i}/{total_keys}] 🔄 Validating API Key: {api_key[:8]}...")  # Partial display of key
                is_valid, details = check_key(api_key)

                if is_valid:
                    print(f"{Fore.GREEN}[{i}/{total_keys}] ✅ {details}")
                    valid_keys.append(api_key)
                else:
                    print(f"{Fore.RED}[{i}/{total_keys}] ❌ {details}")

                pbar.update(1)

        print(f"\n{Fore.GREEN}Validation completed. {len(valid_keys)} keys are valid.")
        print(f"{Fore.RED}Invalid keys have been discarded.")

    except FileNotFoundError:
        print(f"{Fore.RED}❌ Error: The specified file path does not exist.")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Heroku API keys.")
    parser.add_argument("--file", type=str, required=True, help="File containing Heroku API keys.")
    
    args = parser.parse_args()
    validate_api_keys(args.file)
