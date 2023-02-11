from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(url):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source)
    title = soup.find('span', attrs={"id": "productTitle"}).text.strip()
    price = soup.find(
        'span', attrs={"class": "a-price-whole"}).text.strip().replace(",", "")
    driver.quit()
    return (title, price)
