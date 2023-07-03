import pyautogui

def main():
    # This program is to determine the cordinates of an element and add to navigation/elements.py
    # Get cordinates of top left and bottom right of element
    response = input('Continue [c], Quit[q]: ')
    working = True
    while working:
        print(pyautogui.position())

        response = input('Continue [c], Quit[q]: ')

        if response.lower() == 'q':
            working = False

if __name__ == "__main__":
    main()