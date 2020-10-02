import requests
import urllib.parse
import os


class TelegramBot:
    def __init__(self):
        self.tkn = os.environ.get('token')
        self.id = os.environ.get('telegram_id')

    def send_it(self, info, link):
        txt = urllib.parse.quote(info + link)
        url1 = "https://api.telegram.org/bot" + self.tkn + f"/sendMessage?chat_id={self.id}&text=" + txt
        requests.get(url1)     
        print("Message Sent")


if __name__ == '__main__':
    bot = TelegramBot()
    bot.send_it("Checking bot", "\nwww.google.co.in")
