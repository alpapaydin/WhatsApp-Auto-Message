import pywhatkit as kit
import datetime
import codecs
from csv import reader
from csv import DictReader
text_file = codecs.open("mesaj.txt", "r", "utf-8")
mesaj = text_file.read()
text_file.close()
with open('telno.csv', 'r+') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        try:
            print(row['Telno'])
            kit.sendwhatmsg(row['Telno'], mesaj, datetime.datetime.now().hour,datetime.datetime.now().minute+1, tab_close=True)
        except:
            pass
