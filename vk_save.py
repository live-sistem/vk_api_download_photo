import requests, json, time, os
import re
import urllib.request
from dotenv import load_dotenv
# from main import ExampleApp

CD_DIR = os.getenv('CD_DIR')

def url_api(dow, count, VK_USER_ID, VK_TOKEN):
	try:
		api = requests.get("https://api.vk.com/method/photos.getAll", params={
			'access_token': VK_TOKEN,
			'owner_id': VK_USER_ID,
			'offset': dow,
			'count': count,
			'photo_sizes': 0,
			'v': 5.131,
		})
		return json.loads(api.text)
	except:
		return False
	# return api, json.loads(api.text)

def info_max_count(response_jsons):
	js = response_jsons
	return js['response']['count']

def test_api(response_json):
	suum = []
	i = 0 
	Mass_full_name = []
	for files in response_json['response']['items']:
		for WriteHeight in files['sizes']:
			suum.append(WriteHeight["height"])
		i=i+1

		Url_IMG = files["sizes"][suum.index(max(suum))]["url"]
		sizing_img = files["sizes"][suum.index(max(suum))]["width"]	

		Update_Url_IMG = Url_IMG.split("/")[-1]
		NameIMG = Update_Url_IMG.split("?")[0]
		print("размер ", sizing_img, "Название ", NameIMG)
	return i

def download(response_json):
	# try:
		suum = []
		i = 0 
		Mass_full_name = []
		for files in response_json['response']['items']:
			for WriteHeight in files['sizes']:
				suum.append(WriteHeight["height"])
			# тут нужно подумать как считать фотографии по одной и отправлять через return 
			# тут должно i = 1
			i=i+1
			Url_IMG = files["sizes"][suum.index(max(suum))]["url"]

			sizing_img = files["sizes"][suum.index(max(suum))]["width"]
			Update_Url_IMG = Url_IMG.split("/")[-1]
			NameIMG = Update_Url_IMG.split("?")[0]

			print("-", "NAME: ", NameIMG, " ",sizing_img, " ", "URL :" ,Url_IMG, )
			time.sleep(1)
			Mass_full_name.append(NameIMG)
			suum = []
		return i
			# urllib.request.urlretrieve(Url_IMG, CD_DIR + NameIMG)
			# time.sleep(1)
			# if os.path.exists(CD_DIR + NameIMG):
			# 	print("файл найден____" ,NameIMG)
			# else:
			# 	print("файл не найден")
			# 	print("check logs")
			# 	logs = open('URL_link_ERROR.txt', 'w')
			# 	logs.write(Url_IMG + '\n')
			# 	logs.close
			# 	with1 = open('test.txt', 'w')
			# 	for index in Mass_full_name:
			# 		with1.write(index + '\n')
			# 	print("OK")
	# except:
	# 	return False	

# def brain():
# 	while dow != 2179:
# 	test.response_json = test.url_api(dow, "10", VK_USER_ID, VK_TOKEN)

# 	with open('response.json', 'w') as file:
# 		json.dump(test.response_json, file)
		
# 	dow = test.download(test.response_json, i)
# 	i = dow
# 	print(dow)

