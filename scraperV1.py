import pyperclip
import pyautogui
import time
import bs4
from navigation.utility import *
from navigation.elements import elements, inspect_elements
from scraping.LI_scraping import *
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

    # pyautogui.press('f12')
    # dev_tools = True

    # delay(kind='process')
    # nav_connections(dev_tools)

    # connections_html = get_html(dev_tools)

    # connections_data = get_connections_data(connections_html)

    # delay()

    # print(json.dumps(connections_data, indent=4))

    # for connection in connections_data:
    #     profile_url = connections_data[connection]['profile_url']
    #     if 'https://www.linkedin.com' not in profile_url:
    #         profile_url = 'https://www.linkedin.com' + profile_url

    # nav_url('https://www.linkedin.com/in/tanner-crook/')

    profile_html = get_html(dev_tools)

    profile_data = get_profile_data(profile_html)

    print(profile_data)



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

def mouse_maintenance():
    response = input('Continue [c], Quit[q]: ')
    while response != 'q':
        print(pyautogui.position())

        response = input('Continue [c], Quit[q]: ')

if __name__ == "__main__":
    main()

