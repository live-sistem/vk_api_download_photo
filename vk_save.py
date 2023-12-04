import requests, json, time, os
import re
import urllib.request


VK_USER_ID = 237723232
VK_TOKEN = ""
linkDir = "/Users/admin/Desktop/dev_project/ApiVk/images/"
#Запрос на сервер для доcтупа к фотографиям (JSON)
def get_foto_data(offset=0, count=200):
	api = requests.get("https://api.vk.com/method/photos.getAll", params={
		'access_token': VK_TOKEN,
		'owner_id': VK_USER_ID,
		'offset': offset,
		'count': count,
		'photo_sizes': 0,
		'v': 5.131,
	})
	return json.loads(api.text)
	

#бота с массивом (JSON)
def get_foto():
	data = get_foto_data()
	count_foto = data["response"]["count"]
	i = 0
	count = 200
	Photos = []
	suum = []
	NameLinkDir = []
	while i <= count_foto:
		if i != 0:
			data = get_foto_data(offset=i, count=count)
		for files in data["response"]["items"]:
			# проходимся по всем размерам файла и создаём массив всех возможных размеров
			for WriteHeight in files["sizes"]:
				suum.append(WriteHeight["height"])
			# Сохраняем нужную ссылку на файл с максимальный разришением
			urlLink = files["sizes"][suum.index(max(suum))]["url"]
		# Преобразуем имя файла через url
			UpdaelLink = urlLink.split("/")[-1]
			NameIMG = UpdaelLink.split("?")[0]

				#Информация для мониторинга
			# Добовляем в массив Photos име файла для мониторига
			Photos.append(NameIMG)
			print("-----------")
			# print("Сколько всего фото в альбоме", count_foto)
			# print("Массив размеров одной фоки :Height: ", suum)
			# print("Максимальный размер одной фоки:", max(suum))
			print("Ссылка на фото:URL: ", urlLink)
			# Обнуляем массив возможныйх размеров файла что бы внести новые
			# Скачиваем файл и сохроняем по указанной директории по названию указанного в переменной NameIMG
			urllib.request.urlretrieve(urlLink, '/Users/admin/Desktop/dev_project/ApiVk/images/' + NameIMG)	
			time.sleep(4)
			if os.path.exists(linkDir + NameIMG):
				print("файл найден____" ,NameIMG)
			else:
				print("файл не найден")
				print("check logs")
				logs = open('URL_link_ERROR.txt', 'w')
				logs.write(urlLink)
				logs.close
			suum = []	
		print("сколько было совершино итераций", i/50, "без диления i: ",i )
		i += count
	print(len( Photos), "чилсо означает сколько всего имён добавиловсь в массив",)
	# for root, dirs, files in os.walk("C:/Users/admin/Desktop/dev_project/ApiVk/images/"):  
	# 	for filename in files:
	# 		NameLinkDir.append(filename)
	# print("Сколько было запросов: ", len(Photos))
	# print("Сколько скачалось: ",len(NameLinkDir))
	# print(type(Photos))
	# print(type(NameLinkDir))
	# if len(NameLinkDir) == len(Photos):
	# 	print("Скачались все фотографии")
	# else:
	# 	for OneIndex in Photos:
	# 		if not OneIndex in NameLinkDir:
	# 			print(OneIndex)
def main():
	get_foto()

if __name__ == "__main__":
	main()