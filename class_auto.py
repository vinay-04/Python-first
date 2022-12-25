# import datetime,pyautogui

# """
# def signin():
#     pyautogui.press('win')
#     pyautogui.typewrite('teams')
#     pyautogui.keyDown('enter')
#     pyautogui.sleep(4.5)
#     pyautogui.write('8633vinay@gyanbharati.onmicrosoft.com',interval=0.01)
#     pyautogui.sleep(0.5)
#     sg = pyautogui.locateCenterOnScreen('\codes\images\signin.png')
#     pyautogui.click(sg)
# """

# def join():
#     pyautogui.press('win')
#     pyautogui.typewrite('teams')
#     pyautogui.press('enter')
#     pyautogui.sleep(2)
#     loc1 = pyautogui.locateCenterOnScreen('\codes\images\join#.png', confidence=0.8)
#     pyautogui.click(loc1)
#     pyautogui.sleep(1)
#     mic = pyautogui.locateCenterOnScreen( '\codes\images\mic.png')
#     pyautogui.click(mic)
#     pyautogui.sleep(1)
#     loc2 = pyautogui.locateCenterOnScreen('\codes\images\join!.png', confidence=0.9)
#     pyautogui.click(loc2)

# """

# if sign_in == 'yes':
#     signin()
#     pyautogui.sleep(15)
#     cal = pyautogui.locateCenterOnScreen('\codes\images\Teamscalendar.png')
#     pyautogui.click(cal)
#     square = pyautogui.locateCenterOnScreen('\codes\images\square.png')
#     pyautogui.click(square)
#     pyautogui.sleep(1)
#     pyautogui.hotkey('win','d')
#     signin_time=str(datetime.datetime.now().strftime("%H:%M:%S"))

# """
# # sign_in=pyautogui.prompt("Want to sign in: ")

# ct=pyautogui.prompt("Enter the class time: ")
# # lv_cls=pyautogui.prompt("Want to leave class: ")

# # signin_time = ''

# while True:
#     pyautogui.sleep(0.75)
#     t=datetime.datetime.now()
#     d=datetime.timedelta(seconds=5.5)
#     p=t+d
#     cut=p.strftime('%H:%M:%S')

#     if ct == cut:
#         break

# join()

# # if lv_cls == 'yes':
# #     leave():

# # if sign_in == 'yes':
# #     pyautogui.alert(text="Signed in at: " + signin_time +"\nJoined at: " + datetime.datetime.now().strftime("%H:%M:%S"), title="Class automation", button='OK')
# # else:

# pyautogui.alert("Joined at: " + datetime.datetime.now().strftime("%H:%M:%S"), title="Class automation", button='OK')


# import pyautogui
# end = pyautogui.locateCenterOnScreen('H:\codes\images\end.png', confidence=9)
# while True:
#     p = pyautogui.locateCenterOnScreen('H:\codes\images\check.png', confidence=9)
#     if p == None:
#         continue
#     else:
#         pyautogui.click(end)
#         break


import pyautogui
while True:
    p = pyautogui.locateCenterOnScreen('\codes\images\end.png', confidence=8)
    if p == None:
        print('not op')
    else:
        print('op')
        break
