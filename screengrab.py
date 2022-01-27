import sys
import time
import os
from PIL import Image
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

options = FirefoxOptions()
options.add_argument("--headless")

# Get the manifest
url_base = 'http://77.68.77.144/screens/'
i = 1

directory = os.fsencode('/var/www/html/screens')

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".html") or filename.endswith(".htm"):
        url = "{}{}".format(url_base, filename)
        i = filename.rsplit(".", 1)[0]

        # Initialise Selenium
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(800, 554)

        # Get screenshow
        driver.get(url)
        time.sleep(3)
        driver.get_screenshot_as_file("/home/greenminds-screengrab/{}.png".format(i))
        driver.quit()

        # Save to Apache root
        Image.open("/home/greenminds-screengrab/{}.png".format(i)).save("/var/www/html/{}.bmp".format(i))
        os.remove("/home/greenminds-screengrab/{}.png".format(i))
        img = Image.open("/var/www/html/{}.bmp".format(i)).convert('L')
        img.save("/var/www/html/{}.bmp".format(i))
        #i += 1
        driver.quit()
