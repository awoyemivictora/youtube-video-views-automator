from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.webdriver.common.keys import Keys  # To send keyboard events

# Set DISPLAY for XLaunch
os.environ["DISPLAY"] = "192.168.146.168:0"

# Set ChromeDriver path
service = Service('/usr/local/bin/chromedriver')

# Function to autoplay the video
def autoplay_video(driver):
    try:
        # Scroll to the video element to ensure visibility
        driver.execute_script("window.scrollTo(0, 50);")  # Scroll down a bit

        # Wait until the video element is available, retry up to 5 times
        for _ in range(5):
            video_element = driver.execute_script("return document.querySelector('video')")
            if video_element:
                print("Video element found. Sending space bar to play video.")
                # Click on the video element to give it focus
                video_element.click()

                # Send spacebar key to play/pause the video
                video_element.send_keys(Keys.SPACE)

                # Alternatively: Use JS play method if space doesn't work
                driver.execute_script("document.querySelector('video').play();")
                print("Video should be playing...")
                break
            else:
                print("Video element not found. Retrying...")
                time.sleep(1)
    except Exception as e:
        print(f"Error in autoplay script: {e}")

# Main loop to play the video repeatedly
while True:
    try:
        # Initialize Chrome options
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/google-chrome"  # Full path to Chrome
        chrome_options.add_argument("--no-sandbox")  # Required for some Linux distributions
        chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")
        chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")  # Allow autoplay without user gesture
        chrome_options.add_argument("--mute-audio")  # Mute the audio (optional)

        # Start Chrome
        driver = webdriver.Chrome(service=service, options=chrome_options)
        url = "https://www.youtube.com/watch?v=OGAOAQJBlls"
        print(f"Opening {url}")
        driver.get(url)

        # Wait for the page to load completely
        time.sleep(5)

        # Autoplay the video
        autoplay_video(driver)

        # Wait for 30 seconds while the video plays
        time.sleep(30)

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
