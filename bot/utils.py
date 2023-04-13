from selenium.webdriver.common.action_chains import ActionChains

def mouseover_coordinates(driver, offset_from_element, coordinates):
    """Locate items with coordinates"""
    # Chain actions
    actions = ActionChains(driver)
    # Initial coordinates
    base_coordinates = driver.find_element(offset_from_element[0], offset_from_element[1])
    xi, yi = base_coordinates.location["x"], base_coordinates.location["y"]
    # Offset from base coordinates
    actions.move_to_element_with_offset(base_coordinates, -xi, -yi)
    # Move and click to located point
    actions.move_by_offset(coordinates[0], coordinates[1]).click()
    # Do all the above
    actions.perform()