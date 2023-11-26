# import time
#
# import requests
#
# #
# # urls = 'http://api.open-notify.org/iss-now.json'
# #
# # response = requests.get(urls)
# #
# # if response.status_code == 200:
# #     print(response.text)
# # else:
# #     print("error")
#
#
# # url = 'http://numbersapi.com/'
# # find = '43'
# # response = requests.get(url + find)
# #
# # if response.status_code == 200:
# #     print(response.text)
#
#
# API_URL = 'https://api.telegram.org/bot'
# TOKEN = '6871019854:AAFJ-IWN1a-KdDyOb21tVcjUttAxbgOT2gE'
# TEXT = 'Test update'
# max_counter = 100
#
# offset = -2
# count = 0
# while count < max_counter:
#     print('attemp= ', count)
#     updates = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={offset+1}').json()
#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
#     time.sleep(1)
#     count += 1
#
#
#
#
