from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import functions, types
import xlrd
import csv

# Create Client Object
# api_id = '1426688'
# api_hash = '93393d94fc104d23eb65865a587c80bd'
# phone = '+85510400229'

api_id = '1426688'
api_hash = '93393d94fc104d23eb65865a587c80bd'
phone = '+85510400229'

# Login
client = TelegramClient(phone, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

# create workbook to save user contact
async def createUserContact():
    loc = "Book1.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    row = 1

    with open("members-" + 'import-contact' + ".csv", "w",
              encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(['username', 'user id', 'access hash', 'name'])

        for i in range(sheet.nrows):
            if i != 0:
                # add user to contact
                phoneNum = str(int(sheet.cell_value(i, 2)))
                firstName = sheet.cell_value(i, 1)
                lastName = sheet.cell_value(i, 0)
                contact = await InputPhoneContact(client_id=0, phone=phoneNum, first_name=str(firstName), last_name=str(lastName))
                result = client(ImportContactsRequest([contact]))
                usersDic = result.__dict__['users']
                col = 0
                if len(usersDic) > 0:
                    username = usersDic[0].__dict__["username"]
                    chatID = usersDic[0].__dict__["id"]
                    accessHash = usersDic[0].__dict__["access_hash"]
                    name = str(usersDic[0].__dict__["first_name"]) + ' ' + str(usersDic[0].__dict__["last_name"])
                    print(username, chatID, accessHash, name)
                    writer.writerow([username, chatID, accessHash, name])

createUserContact()