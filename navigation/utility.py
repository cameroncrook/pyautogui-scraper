import pyautogui
import pyperclip
import time
import random
from navigation.elements import elements, inspect_elements

# ===================================================================================================
# Utility Functions
# ===================================================================================================
def get_html(dev_tools: bool):
    # add some delays in here
    if dev_tools == False:
        pyautogui.press('f12')

        delay(kind='process')
        pyautogui.hotkey('ctrl', 'c')
        delay(kind='process')

        html = pyperclip.paste()

        pyautogui.press('f12')
    else:
        click_element(inspect_elements['inspect_body'])

        delay(kind='process')

        pyautogui.hotkey('ctrl', 'c')
        delay(kind='process')

        html = pyperclip.paste()

    return html

def get_url():
    click_element('top_search')

    time.sleep(.5)
    pyautogui.hotkey('ctrl', 'c')

    time.sleep(.5)
    url = pyperclip.paste()

    return url

def bezier_curve(points, num_samples):
    import numpy as np
    from scipy.special import comb

    t = np.linspace(0, 1, num_samples)
    n = len(points) - 1
    curve_x = np.zeros(num_samples)
    curve_y = np.zeros(num_samples)

    for i in range(n + 1):
        curve_x += comb(n, i) * (1 - t)**(n - i) * t**i * points[i][0]
        curve_y += comb(n, i) * (1 - t)**(n - i) * t**i * points[i][1]

    return curve_x, curve_y

def move_mouse(x, y, click=False):

    # Define the control points for the Bézier curve
    points = get_intermediate_points((x, y))

    # Generate intermediate points along the curve
    num_samples = random.randint(10,60)
    curve_x, curve_y = bezier_curve(points, num_samples)

    # Move the mouse sequentially through the intermediate points
    duration = 0.1  # Adjust this value to control the speed of movement
    for x, y in zip(curve_x, curve_y):
        pyautogui.moveTo(x, y, duration=duration)

    if click == True:
        delay(kind='clicking')
        pyautogui.click()

def get_intermediate_points(ending_cords: tuple):
    current_position = pyautogui.position()

    intermediate_points = [(current_position.x, current_position.y)]

    x = current_position.x
    y = current_position.y

    for i in range(2):
        if x > ending_cords[0]:
            x = random.randint(ending_cords[0], x)
        else:
            x = random.randint(x, ending_cords[0])

        if y > ending_cords[1]:
            y = random.randint(ending_cords[1], y)
        else:
            y = random.randint(y, ending_cords[1])
            

        intermediate_points.append((x, y))

    intermediate_points.append(ending_cords)

    return intermediate_points

def click_element(element):
    x = random.randint(element[0][0], element[1][0])
    y = random.randint(element[0][1], element[1][1])

    move_mouse(x, y, click=True)

def scroll_feed():
    x = random.randint(elements['feed'][0][0], elements['feed'][1][0])
    y = random.randint(elements['feed'][0][1], elements['feed'][1][1])

    repetition = random.randint(1,5)

    move_mouse(x, y)
    
    for i in range(repetition):
        scroll_distance = random.randint(500, 5000)

        total_scrolled = 0
        scrolling = True
        while scrolling:
            pyautogui.scroll(-100)
            time.sleep(.5)

            total_scrolled 

            if total_scrolled > scroll_distance:
                scrolling = False

def keyboard_type(text):
    for char in text:
        pyautogui.write(char)
        delay(kind='typing')

def delay(kind='none'):
    num = 0

    if kind == 'typing':
        num = random.uniform(0.1, 0.5)
        num = round(num, 3)
    elif kind == 'clicking':
        num = random.uniform(0.5, 2.0)
        num = round(num, 3)
    elif kind == 'load':
        num = random.uniform(4.0, 8.0)
        num = round(num, 3)
    elif kind == 'process':
        num = random.uniform(1.0, 2.5)
        num = round(num, 3)
    else:
        num = random.uniform(2.0, 5.0)
        num = round(num, 3)

    time.sleep(num)

def scroll(distance=0):
    # This function takes a choses distance and splits it up into smaller scroll incriments
    test_dist = random.randint(-500, -100)
    
    scrolling = True
    total_scroll = 0
    while scrolling:
        pyautogui.scroll(test_dist)

        total_scroll += test_dist

        response = input('continue? ')

        if response == 'q':
            scrolling = False
        else:
            test_dist = random.randint(-500, -100)

    print(total_scroll)

# add scrolling and typing functions
# add ranomized movements