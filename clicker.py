from pynput import mouse
import time
import pyautogui

rodando = True
pausado = False

def on_click(x, y, button, pressed):
    global rodando, pausado
    if pressed:
        if button == mouse.Button.middle:
            print("pausado - botão do meio do mouse")
            pausado = not pausado
        elif button == mouse.Button.right:
            print("parou")
            rodando = False
            return False

listener = mouse.Listener(on_click=on_click)
listener.start()

while rodando:
    if pausado == False:
        pyautogui.click()
        time.sleep(0.01)

listener.join()