# -*- coding: utf-8 -*-
import nekos
import requests
while 1==1:
  url = nekos.img('neko')
  dir1 = "/content/drive/MyDrive/Cat/SFW"
  list1 = os.listdir(dir1)
  number_files = len(list1)
  name_file = str(number_files)
  if number_files > 1000:
    sys.exit()
  else:
    print('Downloading..')
    print('Hold Tight!')
    filename = ("nsfw." + name_file + ".jpg")
    r = requests.get(url)
    open(filename, 'wb').write(r.content)
    print('Done!')
    print('     ')