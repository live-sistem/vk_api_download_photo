import requests, json, time, os
import re
import urllib.request
from threading import Thread

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
	try:
		return response_jsons['response']['count']
	except:
		print(response_jsons['error'])

def test_api_json(response_json):
	try:
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
	except:
		return False

def download(response_count_max, filepath):
		suum = []
		app = "/"
		i = 0 
		for files in response_count_max['response']['items']:
			for WriteHeight in files['sizes']:
				suum.append(WriteHeight["height"])
			i=i+1

			Url_IMG = files["sizes"][suum.index(max(suum))]["url"]
			sizing_img = files["sizes"][suum.index(max(suum))]["width"]

			Update_Url_IMG = Url_IMG.split("/")[-1]
			NameIMG = Update_Url_IMG.split("?")[0]
			try:
				urllib.request.urlretrieve(Url_IMG, filepath + app + NameIMG)
				time.sleep(2)
				if os.path.exists(filepath + app + NameIMG):
					print("файл найден_" , NameIMG)
				else:
					print("файл не найден_", NameIMG)
					logs = open('logs.txt', 'w')
					logs.write(Url_IMG + '\n' )
					logs.close
			except:
				logs = open('logs.txt', 'w')
				logs.write("urllib.error.URLError",Url_IMG + '\n' )
				logs.close
			suum = []
		return i

# def brain():
# 	while dow != 2179:
# 	test.response_json = test.url_api(dow, "10", VK_USER_ID, VK_TOKEN)

# 	with open('response.json', 'w') as file:
# 		json.dump(test.response_json, file)
		
# 	dow = test.download(test.response_json, i)
# 	i = dow
# 	print(dow)

