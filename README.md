# YouTube Autoplay Selenium Script

This project is a Python-based script that uses Selenium WebDriver to automate the process of visiting a YouTube video and automatically playing it. The script can repeatedly open the video in a browser, play it for a set duration, and then close the browser. It's a useful tool for automating video views or testing purposes.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Future Enhancements](#future-enhancements)

## Overview
This project leverages the power of Selenium to automate YouTube video views. The script opens a specific YouTube URL, plays the video for 30 seconds, and repeats the process. This can be useful for testing, automated views, or other applications where automation is needed for YouTube.

## Prerequisites
To run this script, ensure you have the following installed:
- Python 3.x
- Google Chrome (or any other browser of your choice)
- ChromeDriver (compatible with your version of Chrome)
- Selenium Python module

### Other Dependencies
- XLaunch for Linux users to provide GUI support on headless servers.
- `pip` to manage Python packages.

## Installation
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Install the required Python packages:
    ```bash
    pip install selenium
    ```

3. Download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads), and place it in `/usr/local/bin` or a directory of your choice. Make sure it is executable:
    ```bash
    chmod +x /path/to/chromedriver
    ```

4. Set up `XLaunch` for GUI applications on Linux:
    - Set the environment variable for display:
    ```bash
    export DISPLAY=:0
    ```

## Usage
1. Open the `main.py` script in your editor to configure the YouTube video URL:
    ```python
    url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
    ```

2. Run the Python script:
    ```bash
    python main.py
    ```

The script will open a Chrome window, navigate to the YouTube URL, play the video for 30 seconds, and close the browser. It will repeat the process in an infinite loop.

### Script Features
- **Autoplay:** Automatically starts the video upon opening the URL.
- **Looping:** Reopens the browser after playing the video for 30 seconds.
- **Error Handling:** The script attempts to recover from common errors, such as network issues or browser failures.

### Example
Here’s how the script runs:
```bash
Opening https://www.youtube.com/watch?v=YOUR_VIDEO_ID
Video autoplay started...
Playing video for 30 seconds...
Closing browser...
Reopening video...


Features
Autoplay Video: The script automatically starts playing the YouTube video using JavaScript, simulating a spacebar press or direct play function.
Looping Mechanism: After playing the video for a set time (30 seconds), the script closes the browser and reopens it to start the process again.
Error Handling: The script gracefully handles issues, such as browser crashes or network failures, by retrying up to three times with different configurations.
Future Enhancements
Proxy Support: We plan to implement the use of rotating proxies to make each session appear unique, simulating traffic from different locations.
GUI Interface with Tkinter: A user-friendly GUI will be built using Tkinter, allowing non-technical users to run the script with ease and customize options, such as video URL, duration, and the number of loops.
Contributions
Feel free to submit pull requests or open issues if you'd like to contribute to this project!

License
This project is licensed under the MIT License.

perl
Copy code

### How to Save and Push This File:
1. Open your terminal and navigate to your project directory.
2. Create and open the `README.md` file with Vim:
    ```bash
    vim README.md
    ```
3. Press `i` to enter *Insert Mode*.
4. Paste the `README.md` content into the Vim editor.
5. Press `Esc` to exit *Insert Mode*.
6. Type `:wq` and hit `Enter` to save and close the file.
7. Commit and push your changes to GitHub:
    ```bash
    git add README.md
    git commit -m "Add README file"
    git push
    ```

Your `README.md` file should now be formatted and ready for your GitHub repository.
