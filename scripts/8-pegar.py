from pynput.keyboard import Key, Controller
keyboard = Controller()
keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release('v')
keyboard.release(Key.ctrl)