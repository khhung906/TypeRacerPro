from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from cfg import cfg

class Bot():
    def __init__(self, drive_path, speed):
        self.driver = webdriver.Chrome(drive_path)
        self.driver.get(cfg['site']) 
        self.time_per_word = 60/(speed*8)
        

    def run(self):
        # click enter game
        self.start_game()
        # get the passage for typing
        passage = self.get_pasage()
        # type the passage into input box
        self.type_race(passage)

        time.sleep(30)
        self.driver.close()

    def start_game(self):
        wait = WebDriverWait(self.driver, 10)
        start_btn = wait.until(EC.element_to_be_clickable((By.XPATH, cfg['start_xpath'])))
        start_btn.click()

    def get_pasage(self):
        wait = WebDriverWait(self.driver, 10)
        passage = wait.until(EC.presence_of_element_located((By.XPATH, cfg['passage_xpath'])))
        passage = passage.text
        return passage.split()

    def type_race(self, passage):
        def type_word(key):
            element.send_keys(key)
        
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, cfg['type_xpath'])))
        for word in passage[:-1]:
            print(word)
            for w in [*word, Keys.SPACE]:
                type_word(w)
                time.sleep(self.time_per_word)

        print(passage[-1])
        for w in passage[-1]:
            type_word(w)
    