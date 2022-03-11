# import keyboard  # using module keyboard
# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('8'):  # if key 'q' is pressed
#             print('You Pressed A Key!')
#             break  # finishing the loop
#     except:
#         print('You Pressed ANOTHER Key!')
#         break  # if user pressed a key other than the given key the loop will break

import keyboard
while True:
    if keyboard.is_pressed('w'):
        print('W')
    elif keyboard.is_pressed('s'):
        print('S')
    elif keyboard.is_pressed('a'):
        print('A')
    elif keyboard.is_pressed('d'):
        print('D')
    elif keyboard.is_pressed('Esc'):
        break
