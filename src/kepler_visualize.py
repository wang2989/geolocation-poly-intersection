import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

current_dir = os.path.abspath(__file__)

# Creating absolute paths for data to visualize
crash_stats_relative_path = '../../data/cleaned_crash_stats.csv'
crash_stats_abs_path = os.path.abspath(os.path.join(current_dir, crash_stats_relative_path))

points_in_poly_list_relative_path = '../../data/PIP_columbus_area.csv'
points_in_poly_list_abs_path = os.path.abspath(os.path.join(current_dir, points_in_poly_list_relative_path))

neighborhood_polygon_relative_path = '../../data/user_defined_polygon.json'
neighborhood_polygon_abs_path = os.path.abspath(os.path.join(current_dir, neighborhood_polygon_relative_path))

line_list_relative_path = '../data/{INSERT FILE NAME HERE}'
line_list_abs_path = os.path.abspath(os.path.join(current_dir, line_list_relative_path))


# Creating absolute paths for reports to visualize
poly_intersection_relative_path = '../../reports/polygon-polygon-intersection-v1.html'
poly_intersection_abs_path = os.path.abspath(os.path.join(current_dir, poly_intersection_relative_path))

pip_relative_path = '../../reports/point-in-polygon.html'
pip_abs_path = os.path.abspath(os.path.join(current_dir, pip_relative_path))


# Creating absolute path for comparison graphs
concat_graphs_relative_path = '../../test/graphs/concat_graphs.png'
concat_graphs_abs_path = os.path.abspath(os.path.join(current_dir, concat_graphs_relative_path))


# open keplerGL
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Open point-in-polygon report
driver.get("file://" + poly_intersection_abs_path)

# Open polygon-polygon intersection v1 report
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")
driver.get("file://" + pip_abs_path)

# Open line simplification report

# Open comparison images
driver.execute_script("window.open('about:blank','fourthtab');")
driver.switch_to.window("fourthtab")
driver.get("file://" + concat_graphs_abs_path)

# Open keplerGL for data visualization
driver.execute_script("window.open('about:blank','fifthtab');")
driver.switch_to.window("fifthtab")
driver.get("https://kepler.gl/demo")

# drop kepler datasets into browser
# adding raw crash stats
file_drop = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input.upload-button-input[type=file]"))
)
file_drop.send_keys(crash_stats_abs_path)

# adding neighborhood polygons
add_data_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".add-data-button"))
)
add_data_button.click()

additional_file_drop = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input.upload-button-input[type=file]"))
)
additional_file_drop.send_keys(neighborhood_polygon_abs_path) # 

# adding filtered points in the designated poly
add_data_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".add-data-button"))
)
add_data_button.click()

additional_file_drop = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input.upload-button-input[type=file]"))
)
additional_file_drop.send_keys(points_in_poly_list_abs_path)
