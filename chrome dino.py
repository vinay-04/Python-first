import pyautogui,time
import PIL


def jump():
    pyautogui.keyDown('up')
    return
def collide(data):
   for x in range(620, 659):
       for y in range(222,270):
            if data[x,y] < 100:
                return True
   return False

def ss():
    img=PIL.ImageGrab.grab().convert('L')
    return img
if __name__ == '__main__':
    time.sleep(4)
    while True:
        img=ss()
        data=img.load()
        if collide(data):
            jump()

