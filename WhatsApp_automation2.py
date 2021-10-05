# This repo have some flaws please help us fix it if you found any.

import pywhatkit as pk
from time import sleep

def drinks_break():
  for x in range(7):
      sleep(1.1)
      print(7-x,end=' sec remaining\n')

pk.sendwhats_image(phone_no="+91xxxxxxxxxx",img_path='D:/your_path' , caption="yo sup",print_wait_time=True,tab_close=True)

drinks_break()

yt_search_key = str(input('Enter search keyword for youtube video '))
pk.playonyt(yt_search_key)

drinks_break()

google_search_key = str(input('Enter search keyword for google '))

pk.search(google_search_key)

drinks_break()

info_search_key = str(input('Enter search keyword for relevant information '))

pk.info(info_search_key)

drinks_break()

pk.image_to_ascii_art(r"Enter your path here")
print('Check the folder where this program is save for a ascii file that resembles the given pic!')

drinks_break()

my_writing = input('Enter data here that you want to be displayed as handwriting. (you can use slash n and other commands for tab space and new line etc)')
pk.text_to_handwriting(my_writing)
print('Check the folder where this program is save for a ascii file that resembles the given pic!')

