from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждём, пока исчезнет надпись "Loading..."
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.ID, "loading"))
    )

    # Теперь все изображения загружены. Берём третью картинку (индекс 2)
    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) >= 3:
        third_img_src = images[2].get_attribute("src")
        print(third_img_src)
    else:
        print("Меньше трёх изображений")
finally:
    driver.quit()