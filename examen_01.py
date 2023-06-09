import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome()
driver.maximize_window()
#1 Se connecter au site
driver.get("https://videotron.com/")
time.sleep(3)
#2 Trouver le nombre d’images sur le site et l’afficher dans la console
images = driver.find_elements(By.XPATH,"//img")
print("le nombre total d’images sur le site: ", len(images))
#3 Afficher la valeur de l’attribut 'alt' des images du site
for img in images:
    alt = img.get_attribute("alt")
    print("Alt value: ", alt + "\t")
#4 Trouver le nombre de liens sur le site et l’afficher dans la console
liens = driver.find_elements(By.TAG_NAME,"a")
print("le nombre total de liens sur la page est: ",len(liens))
#5 Trouver le nombre de liens dans la section 'footer' du site et l’afficher dans la console.
footers = driver.find_elements(By.XPATH, "//footer")
for footer in footers:
    links_in_footer = footer.find_elements(By.TAG_NAME, "a")
print("le nombre de liens dans la section 'footer': ", len(links_in_footer))
#6 Récupérer la valeur de l’attribut 'href'de chaque lien dans la section 'footer' du site et l’afficher dans la console.
for x in links_in_footer:
    href = x.get_attribute("href")
    print("href value: ", href + "\t")
driver.quit()