import pywhatkit as pk
from time import sleep

def drinks_break():
  for x in range(7):
      sleep(1)
      print(7-x,end=' sec remaining\n')


pk.sendwhats_image(phone_no="+91xxxxxxxxxx",img_path='D:/your_path' , caption="yo sup",print_wait_time=True,tab_close=True)

drinks_break()

search_key = str(input('Enter search keyword for youtube video '))
pk.playonyt(search_key)
