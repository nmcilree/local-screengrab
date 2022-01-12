import time
import os
import requests
from PIL import Image
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

options = FirefoxOptions()
options.add_argument("--headless")

# Get the manifest
url = 'http://77.68.77.144/greenminds/manifest.json'
response = requests.get(url)
manifest = response.json()
i = 1
for item in manifest:
    # Initialise Selenium
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(800, 554)

    # Get screenshow
    print(item['url'])
    driver.get(item['url'])
    time.sleep(2)
    driver.get_screenshot_as_file("/home/greenminds-screengrab/{}.png".format(i))
    driver.quit()
    # Save to Apache root
    Image.open("/home/greenminds-screengrab/{}.png".format(i)).save("/var/www/html/{}.bmp".format(i))
    os.remove("/home/greenminds-screengrab/{}.png".format(i))
    i += 1
    driver.quit()

