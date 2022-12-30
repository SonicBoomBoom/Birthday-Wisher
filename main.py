import csv
import datetime
import pywhatkit

def sendMsg(n):
    n = '+91' + n
    pywhatkit.sendwhatmsg(n, 'Happy Birthday', 12, 00)
    pass

with open('data.csv') as F:
    cr = csv.reader(F, delimiter=',')
    for i in cr:
        name = i[1]
        birthday = i[2]
        whatsapp = i[3]
        today = datetime.datetime.now().strftime('%d-%b')
        if birthday==today:
            sendMsg(whatsapp)

