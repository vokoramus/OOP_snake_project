import keyboard


def keyboard_listener():
    keys = ['w', 's', 'a', 'd', 'Esc']
    for k in keys:
        if keyboard.is_pressed(k):
            return k
