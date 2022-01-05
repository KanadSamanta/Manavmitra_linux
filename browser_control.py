import time, os, sys

with open(os.path.join(sys.path[0], "PID.txt"), "w+") as PID:
    PID.write(str(os.getpid()))
    PID.close()


def browser_control(taburl, set_window_position_x=51, set_window_position_y=0, set_window_size_x=700,
                    set_window_size_y=550, time_to_run=40 * 60):
    from selenium import webdriver
    browser = webdriver.Firefox()
    browser.set_window_position(set_window_position_x, set_window_position_y)
    browser.set_window_size(set_window_size_x, set_window_size_y)
    browser.get(taburl)
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    time.sleep(time_to_run)
    browser.close()



