from telethon.sync import TelegramClient
import datetime
import pandas as pd

api_id = 29510164
api_hash = '13ba10af013cc4fe7e9160ce31d61adc'

chats = ['MEMBER SERVICE KKM CUKK','@CT_support']


client =  TelegramClient('test', api_id, api_hash)


df = pd.DataFrame()


for chat in chats:
    with TelegramClient('name', api_id, api_hash) as client:
        for message in client.iter_messages(chat, offset_date=datetime.date(2023, 7, 1) , reverse=True):
            print(message)
            data = { "group" : chat, "sender" : message.sender_id, "text" : message.text, "date" : message.date}

            temp_df = pd.DataFrame(data, index=[1])
            df = df._append(temp_df)

df['date'] = df['date'].dt.tz_localize(None)

df.to_excel("D:\\python\\telescrap\\grup_MEMBER SERVICE KKM CUKK & CT ITSO_{}.xlsx".format(datetime.date.today()), index=False)
