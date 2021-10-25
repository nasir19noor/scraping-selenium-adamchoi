from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'chromedriver\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

# Clicl All Matches button
#all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="Home/Away"]')
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

for i in range(0, 5):
    dropdown = Select(driver.find_element_by_id('country'))
    dropdown.select_by_index(i)

    time.sleep(3)

    matches = driver.find_elements_by_tag_name('tr')

    date = []
    home_team = []
    score = []
    away_team = []

    for match in matches:
        date.append(match.find_element_by_xpath('./td[1]').text)
        home_team.append(match.find_element_by_xpath('./td[2]').text)
        score.append(match.find_element_by_xpath('./td[3]').text)
        away_team.append(match.find_element_by_xpath('./td[4]').text)

    df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team })
    df.to_csv(f'football_data_{i}.csv', index=False)
    print(df)
