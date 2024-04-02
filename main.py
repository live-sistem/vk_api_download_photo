import requests, json, time, os, sys 
from vk_save import url_api, download, info_max_count, test_api_json
# from dotenv import load_dotenv
import tempfile, base64, zlib
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
from pywinauto import Desktop
import tempfile, base64, zlib
import threading
import keyboard
import webbrowser

# load_dotenv()

# input_id = os.getenv('VK_USER_ID')
# input_token = os.getenv('VK_TOKEN')
value_var = 0
entry = None

def token():
    oauth = webbrowser.open('https://oauth.vk.com/authorize?client_id=51636410&display=page&redirect_uri=https://ouath.vk.com/blank.html&scope=photos&response_type=token&v=5.131')

    global entry 
    entry = ttk.Entry()
    entry.pack(anchor=NW, padx=6, pady=6, fill=X)

    btn = ttk.Button(text="Ok", command=check_all_Photos)
    btn.pack(anchor=CENTER)

def check_all_Photos():
    # global input_token
    # global input_id
    link_ent_1 = entry.get()
    if link_ent_1 != None:
        try:
            link_ent_2 = link_ent_1.split("/")[-1]
            link_ent_3 = link_ent_2.split("#")[-1]

            link_ent_token1 = link_ent_3.split("&")[0]
            link_ent_token = link_ent_token1.split('=')[-1]

            link_ent_id1 = link_ent_3.split("&")[-1]
            link_ent_id = link_ent_id1.split('=')[-1]

            input_id = link_ent_id
            input_token = link_ent_token
            
            label_input_id_token = ttk.Label(text=(('id:'),input_id))
            label_input_id_token.pack(anchor=NW, padx=6, pady=6)
            
            process_1 = threading.Thread(target=process_one,  args=(input_id, input_token))
            process_1.start()
            
        except:
            showinfo(title="Erorr", message="error validator2")
    else:
        showinfo(title="Erorr", message="error validator1")
    

def process_one(input_id, input_token):
    response_count_1 = url_api(0, 1, input_id, input_token)
    response_jsons = test_api_json(response_count_1)

    if response_jsons != False:
        max_count = info_max_count(response_count_1)
        label_max_count_photos = ttk.Label(text=(('Фото:'), max_count))
        label_max_count_photos.pack(anchor=NW, padx=6, pady=6)

        btn_select_ = ttk.Button(text="Выбрать", command=lambda:btn_download(input_id, input_token, max_count))
        btn_select_.pack(side=BOTTOM)
        
    else:
        showinfo(title="Erorr", message="Токен Устарел")

def btn_download(input_id, input_token, max_count):
    offset = 0
    process_2 = threading.Thread(target=process_two, args=(input_id, input_token, max_count, offset))
    process_2.start()

def process_two(input_id, input_token, max_count, offset):
    filepath = 'C:/Users/LORD2/Pictures/img_vk'
    btn_exit_ = ttk.Button(text="Завершить",)
    btn_exit_.pack(side=BOTTOM)
    if filepath != "":
        label_save_file = ttk.Label(text=filepath)
        label_save_file.pack(side=BOTTOM)

        for i in range(max_count):
            print(i)
            response_count_max = url_api(offset, 1, input_id, input_token)
            download_img = download(response_count_max, filepath)
            offset += 1
            if keyboard.is_pressed('q'):
                continue
            else:
                if download_img == 1:
                    value_var = offset / max_count * 100
                    progressbar.configure(value = round(value_var))
                    progressbar.update()
                    print(offset)
                else:
                    showinfo(title="Info", message="Ошибка-2")
                    break
        print(offset)
        return filepath
    else:
        print("Директория не выбрана")
    


if __name__ == '__main__':        
    root = Tk()
    root.title("DEV")
    root.geometry("400x300")

    progressbar = ttk.Progressbar(orient="horizontal", variable=value_var)
    progressbar.pack(side=BOTTOM, fill=X, padx=6, pady=6 )

    btn_response_link = ttk.Button(text="TOKEN", command=token) # создаем кнопку из пакета ttk
    btn_response_link.pack(anchor="se")

    root.mainloop()