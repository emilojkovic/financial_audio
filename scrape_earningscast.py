from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
url = 'https://earningscast.com/calls?ajax=true&ajax_render=latest&page={0}'
f = open('download_urls.txt', 'w')

for i in range(2405):
    driver.get(url.format(i))
    content = driver.find_elements_by_class_name("mp3_present")
    audio_links = []

    for j in range(1, len(content), 2):
        audio_links.append(content[j].get_attribute('href'))


    for audio_link in audio_links:
        driver.get(audio_link)
        f.write(driver.find_element_by_link_text("Download").get_attribute('href') + "\n");
    
    print("Page {0} completed.".format(i))

print("Done!")
f.close()
driver.close()


