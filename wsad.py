# import numpy as np
# import cv2
# import pyautogui

# pyautogui.sleep(2)
# for i in range(50):
#     pyautogui.sleep(0.2)
#     pyautogui.write("yo gujzz")
#     pyautogui.press('enter')


# from random import randrange as rand
# from time import sleep


# def print_string(current_string, expected_character):
#     while True:
#         some_random_character = rand(0, 127)
#         print("\r" + current_string + chr(some_random_character), end="")

#         if chr(some_random_character) == expected_character:
#             break


# my_string = "Hello World"
# current_str = ""
# for letter in my_string:
#     print_string(current_str, letter)
#     current_str += letter


# import requests
# import pyautogui

# url = "https://type.fit/api/quotes"

# op = []

# response = requests.get(url)
# q = response.json()

# for i in range(50):
#     l = q[i]
#     op.append(l['text'])

# pyautogui.sleep(2)

# for i in op:
#     pyautogui.sleep(0.01)
#     pyautogui.write(i)
#     pyautogui.press('enter')


# import requests, pyautogui

# response = requests.get('https://random-word-api.herokuapp.com/word?number=50')
# lst = response.json()
# pyautogui.sleep(2)
# for i in lst:
#     pyautogui.write(i)
#     pyautogui.press('enter')

# word = 'free'
# response = requests.get('https://api.datamuse.com/words?rel_rhy=' + word)
# lst = response.json()
# for i in lst:
#     if i == lst[-1]:
#         print(i["word"])yo gujzz

#         break
#     else:
#         print(i["word"], end=', ')


# img = cv2.imread("images\\_test.jpg")

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.medianBlur(gray, 5)
# edges = cv2.adaptiveThreshold(
#     gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
# color = cv2.bilateralFilter(img, 9, 250, 250)
# cartoon = cv2.bitwise_and(color, color, mask=edges)
# cv2.imshow("image", img)
# cv2.imshow("edges", edges)
# cv2.imshow("cartoon", cartoon)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import vlc
# import pafy
# import urllib.request

# url = "https://www.youtube.com/watch?v=IZOuSCkZr7k"
# video = pafy.new(url)
# best = video.getbest()
# playurl = best.url
# ins = vlc.Instance()
# player = ins.media_player_new()

# code = urllib.request.urlopen(url).getcode()
# if str(code).startswith('2') or str(code).startswith('3'):
#     print('Stream is working')
# else:
#     print('Stream is dead')

# Media = ins.media_new(playurl)
# Media.get_mrl()
# player.set_media(Media)
# player.play()

# good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
# while str(player.get_state()) in good_states:
#     print('Stream is working. Current state = {}'.format(player.get_state()))

# print('Stream is not working. Current state = {}'.format(player.get_state()))
# player.stop()


# import requests

# data = ['Request URL': 'https://discord.com/api/v9/channels/744151714684207154/messages',
#         'Request Method': 'POST',
#         'Status Code': '200,
#         'Remote Address': '162.159.136.232:443',
#         'Referrer Policy': 'strict-origin-when-cross-origin']
# response = requests.post(data).text
# print(response)
