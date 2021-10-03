# WhatsApp_automation_2
WhatsApp automation using python module.

This repo shows how to automate most of your works in WhatsApp.

The name of the module is pywhatkit and this is the command to install it 

    pip install pywhatkit
    
This module is one of my favorites and the reason behind is that,
using this single module we can just throw away some small module that I've previously used, like [wikipedia](https://github.com/BhargavKadali39/Wikipedia-in-pyton).
External modules like google search, YouTube topic searching, text to handwriting and much more!!

        pywhatkit.sendwhats_image(phone_no="+91xxxxxxxxxx",img_path='D:/your_path' , caption="yo sup",print_wait_time=True,tab_close=True)
        
Here give the phone number of the recipient with country code(ex +91 for india)
img_path The image you want to send to the person,
caption is the text message,
Set wait time here to delay the message to your requirements.(wait time applies after you run the code)
tab_close keep this True if you want no additional WhatsApp tab left after sending the message!

