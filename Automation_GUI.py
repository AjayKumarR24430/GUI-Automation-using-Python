import pyautogui
import time

#PYAUTOGUI.SIZE() 
# FUNCTION:
#This function doesn’t need any parameter. 
# It returns coordinates of the cursor as the program starts.
print(pyautogui.size())

#PYAUTOGUI.DISPLAYMOUSEPOSITION() 
# FUNCTION:
# This function also doesn’t need any parameter. 
# It returns the real-time cursor location along with the RGB value of the window.

pyautogui.displayMousePosition()

# PYAUTOGUI.MOVETO() 
# FUNCTION:
# It moves the cursor from the initial point to the set coordinates in the 
# given duration. This function takes three parameters:
# pyautogui.moveTo(x_coordinate,y_coordinate, duration=’time_in_seconds’)

pyautogui.moveTo(852, 1043, duration = 1)

# PYAUTOGUI.CLICK() FUNCTION:
# It first moves the cursor to the defined coordinate and click as per given the number of clicks. This function takes five parameters:

# pyautogui.click(x = x_coordinate, y = yoordinate, clicks = num_of_clicks,
  # interval = secs_between_clicks, button = 'left')

pyautogui.click(x = 852,
  y = 1043,
  clicks = 1,
  interval = 0.5, button = 'left')

pyautogui.moveTo(423, 73, duration = 1)
pyautogui.click(x = 423,
  y = 73,
  clicks = 1,
  interval = 0.6, button = 'left')
pyautogui.write('weather in Delhi', interval=0.3)
pyautogui.press('enter')
time.sleep(3)

#hello world
pyautogui.moveTo(315, 1058, duration = 1)
pyautogui.click(x = 315,
  y = 1058,
  clicks = 1,
  interval = 0.5, button = 'left')
pyautogui.write('notepad', interval=0.2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write("Hello world!, Welcome to GUI automation!", interval=0.2)
pyautogui.keyDown('ctrl') # hold ctrl key
pyautogui.press('s') # press s key
pyautogui.keyUp('ctrl') # release ctrl key
time.sleep(3)
pyautogui.write('sample.txt', interval=0.4)
pyautogui.press('enter')  # press the Enter key
time.sleep(3)

# MAKING A RECTANGULAR SPIRAL IN MS PAINT
pyautogui.moveTo(315, 1058, duration = 1)
pyautogui.click(x = 315,
  y = 1058,
  clicks = 1,
  interval = 0.5, button = 'left')
pyautogui.write('Paint', interval = 0.3)
pyautogui.press('enter')  # press the Enter key
time.sleep(3)
pyautogui.moveTo(159, 260, duration = 1)
pyautogui.click()
distance = 400
while distance > 10:
    pyautogui.dragRel(distance, 0, duration = 0.2)
    distance = distance - 20
    pyautogui.dragRel(0, distance, duration = 0.2)
    pyautogui.dragRel(-distance, 0, duration = 0.2)
    distance = distance - 20
    pyautogui.dragRel()
    pyautogui.dragRel(0, -distance, duration = 0.2)

time.sleep(5)

# PYAUTOGUI.ALERT(‘ALERT_TEXT’):
# This function displays an alert box wo wod!a
# cith the alert provided in the alert_text.

pyautogui.alert('Your programme is being paused click OK to continue')

# PYAUTOGUI.CONFIRM()
# This function creates a message box with an OK and a Cancel option.

pyautogui.confirm('Your programme is being paused click  OK to continue and Cancel to exit.')

# PYAUTOGUI.PROMPT():
# This function creates a message box with a text field and OK and Cancel Buttons.

pyautogui.prompt('Please write the feedback here.')