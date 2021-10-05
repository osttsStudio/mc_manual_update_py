import os
import sys
import time
import zipfile
import logging
import traceback
import urllib.request
from urllib import request
from configparser import ConfigParser

if os.path.exists('error.log'):
    os.remove('error.log') # del old log file

logging.basicConfig(filename='error.log',level=logging.DEBUG,format="%(asctime)s - %(pathname)s - %(message)s",datefmt="%Y/%m/%d %H:%M:%S")

os.system("") # fixd print's color bug in Win10

# load local config
con = ConfigParser()
con_path = os.path.join(os.path.abspath('.'),'config.ini') # config.ini--local config file name
con.read(con_path)

Con_res = os.getcwd() + "./config_new.ini" # config_new.ini--server config file name
bat_res = os.getcwd() + "/.minecraft/update.bat" # a bat file for updating itself and config, and supports deleting unnecessary files
Url_server = con.get('url','server')
Con_url = Url_server + "/config.ini" # config file url

try:
    request.urlretrieve(Con_url,Con_res)

except:
    logging.debug(traceback.format_exc())

try:
    if not os.path.exists(con_path):
        print("\033[1;31;40m配置文件config.ini不存在，请联系管理员。\033[0m")
        input("Press Enter to exit.")
        os.remove('config_new.ini')
        sys.exit('config file not found')

except:
    logging.debug(traceback.format_exc())

con_server = ConfigParser()
con_server_path = os.path.join(os.path.abspath('.'),'config_new.ini') # config_new.ini--server config file name
con_server.read(con_server_path)
Ver_local = con.get('ver','version')
Ver_server = con_server.get('ver','version')

try:
    if int(Ver_local) == int(Ver_server):
        print("""\n\033[5;36;40m目前已是最新版本，如有疑问请联系管理员。\033[0m\n""")
        os.remove('config_new.ini')
        sys.exit('It is the latest version.')

except:
    logging.debug(traceback.format_exc())

try:
    if int(Ver_local) != int(Ver_server):

        print("\n\033[5;36;40m下载中，请等待。\033[0m\n")

        def report(blocknum, blocksize, totalsize):
            readsofar = blocknum * blocksize
            if totalsize > 0:
                percent = readsofar * 1e2 / totalsize
                s = "\r%5.1f%% %*d / %d" % (percent, len(str(totalsize)), readsofar, totalsize)
                sys.stderr.write(s)
                if readsofar >= totalsize:
                    sys.stderr.write("\n")
            else: # total size is unknown
                sys.stderr.write("read %d\n" % (readsofar,))

        Zip_url = Url_server + "/files/update.zip"
        urllib.request.urlretrieve(Zip_url,"./update.zip",report)
        
        Unzip = zipfile.ZipFile("./update.zip", mode='r')
        for names in Unzip.namelist():
            Unzip.extract(names, './.minecraft')  # unzip to .minecraft
        Unzip.close()

        time.sleep(2)
        os.remove('update.zip')
        os.remove('config_new.ini')
        os.system(bat_res)
        sys.exit('update is successful')

except:
    logging.debug(traceback.format_exc())