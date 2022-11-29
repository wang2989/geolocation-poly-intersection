import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

current_dir = os.path.abspath(__file__)

crash_stats_relative_path = '../../data/PIP_columbus_area.csv'
crash_stats_abs_path = os.path.abspath(os.path.join(current_dir, crash_stats_relative_path))

neighborhood_polygon_relative_path = '../../data/cleaned_polygon_geojson.json'
neighborhood_polygon_abs_path = os.path.abspath(os.path.join(current_dir, neighborhood_polygon_relative_path))

line_list_relative_path = '../data/{INSERT FILE NAME HERE}'
line_list_abs_path = os.path.abspath(os.path.join(current_dir, line_list_relative_path))

# open keplerGL
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://kepler.gl/demo")

# drop kepler datasets into browser
file_drop = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input.upload-button-input[type=file]"))
)
file_drop.send_keys(crash_stats_abs_path)

add_data_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".add-data-button"))
)
add_data_button.click()

additional_file_drop = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input.upload-button-input[type=file]"))
)
additional_file_drop.send_keys(neighborhood_polygon_abs_path)
