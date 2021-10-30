from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from apscheduler.schedulers.background import BackgroundScheduler
import time 


admins = [444719991]
api_id = 1992772
api_hash = "70aa8c1a790a0495129aa0a0671f53f2"
app = Client("dsadsada", api_id=1992772, api_hash="70aa8c1a790a0495129aa0a0671f53f2")

activated = True
groups = [-1001690459076, -1001267673840, -1001405050167, -1001145116956, -1001205217457, -1001369710960, -1001182195056, -1001462247292, -1001162943678]
def job():
    for id in groups:
        app.send_message(id, "<b>💸 BITCOIN MINER 💸</b>\n\n<b>Vuoi minare Bitcoin? Vuoi fare un po' di soldi? Bene, leggi qui e scopri come fare.</b>\n\n<i>Oggi ti mostrerò come farmare bitcoin tramite un browser, CryptoTab. CryptoTab è un browser e un'applicazione per minare bitcoin in modo</i> <b>del tutto automatico</b> <i>mentre si naviga su internet.</i>\n\n<u>Potrai usare qualunque dispositivo, dal pc al tablet, smartphone!</u>\n\n<b>Sei pronto a guadagnare? Bene, scarica l'app da questo link!:</b> https://cryptotabbrowser.com/6953884")

scheduler = BackgroundScheduler()
scheduler.add_job(job, "interval", seconds=15)

scheduler.start()
app.run()