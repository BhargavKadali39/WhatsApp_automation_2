import pywhatkit as pk
from time import sleep

def drinks_break():
  for x in range(7):
      sleep(1)
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
