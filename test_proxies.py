from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import os
import time
import random
import requests
from selenium.webdriver.common.keys import Keys  # To send keyboard events

# Set DISPLAY for XLaunch
os.environ["DISPLAY"] = "192.168.146.168:0"

# Set ChromeDriver path
service = Service('/usr/local/bin/chromedriver')

# Function to fetch proxy list from the Webshare API
def fetch_proxies():
    token = "dtsjyabki9zq0fncawvlicw7typx74k0bxzxjmzk"  # Replace with your actual token
    url = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25"

    headers = {
        "Authorization": f"Token {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            proxies_data = response.json()
            # Construct proxy details with authentication
            proxies = [{
                'address': f"{proxy['proxy_address']}:{proxy['port']}",
                'username': proxy['username'],
                'password': proxy['password']
            } for proxy in proxies_data['results'] if proxy['valid']]
            return proxies
        else:
            print(f"Failed to fetch proxies, status code: {response.status_code}")
            return []

    except Exception as e:
        print(f"Error fetching proxies: {e}")
        return []

# Function to get a random proxy from the fetched list
def get_random_proxy(proxies):
    return random.choice(proxies)

# Function to autoplay the video
def autoplay_video(driver):
    try:
        # Scroll to the video element to ensure visibility
        driver.execute_script("window.scrollTo(0, 50);")  # Scroll down a bit

        # Wait until the video element is available, retry up to 5 times
        for _ in range(5):
            video_element = driver.execute_script("return document.querySelector('video')")
            if video_element:
                print("Video element found. Attempting to play...")
                driver.execute_script("document.querySelector('video').play();")
                print("Video should be playing...")
                break  # Exit if video is found and played
            else:
                print("Video element not found. Skipping autoplay.")
                time.sleep(1)  # Wait a bit before retrying
    except Exception as e:
        print(f"Error in autoplay script: {e}")

# Main loop to play the video repeatedly
while True:
    try:
        # Fetch a list of proxies from the API
        proxies = fetch_proxies()

        if not proxies:
            print("No proxies available, exiting...")
            break

        # Retry mechanism for selecting proxies
        retries = 3  # Number of retries for proxy failures
        success = False

        for attempt in range(retries):
            proxy = get_random_proxy(proxies)
            proxy_str = f"http://{proxy['username']}:{proxy['password']}@{proxy['proxy_address']}:{proxy['port']}"
            print(f"Attempt {attempt + 1}/{retries}, Using proxy: {proxy_str}")

            # Initialize Chrome options with the proxy
            chrome_options = Options()
            chrome_options.binary_location = "/usr/bin/google-chrome"  # Full path to Chrome
            chrome_options.add_argument("--no-sandbox")  # Required for some Linux distributions
            chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--remote-debugging-port=9222")
            chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")
            chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")  # Allow autoplay without user gesture
            chrome_options.add_argument("--mute-audio")  # Mute the audio (optional)

            # Set up proxy authentication
            proxy_str = f"http://{proxy['username']}:{proxy['password']}@{proxy['address']}"
            chrome_options.add_argument(f'--proxy-server={proxy_str}')  # Set the proxy with authentication

            driver = None  # Ensure driver is initialized

            try:
                # Start Chrome
                driver = webdriver.Chrome(service=service, options=chrome_options)
                url = "https://www.youtube.com/watch?v=OGAOAQJBlls"
                print(f"Opening {url}")
                driver.get(url)

                # Wait for the page to load completely
                time.sleep(5)

                # Autoplay the video
                autoplay_video(driver)

                # Wait for some seconds while the video plays
                time.sleep(30)  # Increased to wait for a longer duration before reopening
                success = True
                break  # Exit retry loop if successful

            except Exception as e:
                print(f"Proxy {proxy['address']} failed: {e}")
                if driver:
                    driver.quit()

        if not success:
            print("All proxy attempts failed, exiting...")
            break

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the driver quits before reopening the video
        if 'driver' in locals():
            print("Closing browser...")
            driver.quit()

        # Wait for a short period before restarting (optional)
        time.sleep(5)
        print("Reopening video...")

