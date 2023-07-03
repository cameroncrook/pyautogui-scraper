import pyperclip
import pyautogui
import time
import bs4
from navigation.utility import *
from navigation.elements import elements, inspect_elements
from scraping.LI_scraping import *
from scraping.salesNav_scraping import *
from scraping.scraper_tools import *

def main():
    import json

    # Configuration:
    # ===================================
    username = ''
    password = ''

    dev_tools = True
    # ===================================

    # goal for today:
    # login and nav to all major areas
    # Use my account to go to connections page, get all urls, individually search each connection and get data.
    # If there is time, work on messaging page
    time.sleep(10)

    # search_url = 'https://www.linkedin.com/sales/search/people?query=(spellCorrectionEnabled%3Atrue%2CrecentSearchParam%3A(id%3A2869010156%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3AREGION%2Cvalues%3AList((id%3A103644278%2Ctext%3AUnited%2520States%2CselectionType%3AINCLUDED))))%2Ckeywords%3A%2522LinkedIn%2520Open%2520Networker%2522)&sessionId=TCKOBz%2FrSO2eBjZBx75dlA%3D%3D'
    # nav_url(search_url)

    move_mouse(500, 800)

# ===================================================================================================
# Navigation Functions
# ===================================================================================================

def open_chrome():
    move_mouse(164, 1052, click=True)

    time.sleep(2)
    pyautogui.typewrite('chrome', interval=.2)
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(2)
    move_mouse(870, 602, click=True)
    time.sleep(2)
    pyautogui.hotkey('win', 'up')
    time.sleep(2)

def nav_linkedin():
    
    print()

def login():
    print()

def nav_invitations():
    # goes to network page and then invitations page
    print()

def nav_connections(dev_tools: bool):
    # goes to network page and then invitations page
    if dev_tools == True:
        network_btn = inspect_elements['nav_network']
        connections_btn = inspect_elements['connections']
    else:
        network_btn = elements['nav_network']
        connections_btn = elements['connections']

    click_element(network_btn)
    delay(kind='load')
    click_element(connections_btn)
    delay(kind='load')

def nav_url(url):
    # enters url into search bar and presses enter
    pyperclip.copy(url)

    click_element(elements['top_search'])
    delay(kind='process')
    pyautogui.hotkey('ctrl', 'v')
    delay(kind='process')
    pyautogui.press('enter')

    delay(kind='load')

def nav_salesNav(dev_tools: bool):
    if dev_tools:
        click_element(inspect_elements['nav_salesNav'])
    else:
        click_element(elements['nav_salesNav'])

    delay(kind='load')

def get_salesNav_results(dev_tools: bool):
    # This function navigates through all the pages of a sales nav search and gets the data from each page
    if dev_tools == False:
        pyautogui.press('f12')
        dev_tools = True

    # Need to get data first then determine actions based on results
    html = get_html(dev_tools)

    result_data = get_lead_data(html)

    click_element(inspect_elements['profile_pic'])

    result_size = len(result_data) - 1
    for i in range(result_size):
        delay(kind='process')

        click_element(inspect_elements['next_btn'])

if __name__ == "__main__":
    main()

