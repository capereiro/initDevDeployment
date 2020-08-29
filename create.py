import os
import sys # Para manejo de I/O
import webbrowser # Para manejo de browser
from selenium import webdriver
from dotenv import load_dotenv
from github import Github # API github


##### Variable loading process #####
load_dotenv()

url = "https://github.com/login"
usr = os.getenv("USERNAME")
psw = os.getenv("PASSWORD")
project_path = os.getenv("FILEPATH")
driver_path = os.getenv("DRIVER_PATH")
##### End variable loading #####

browser = webdriver.Chrome(executable_path=driver_path)

def create():
    project_name = str(sys.argv[1])
    # browser = webbrowser.get(browserName)
    
    browser.get(url)
    user = Github(usr, psw).get_user()
    repo = user.create_repo(project_name)
    ##### Folder management #####
    # os.mkdir(project_path + folderName)

    print('-----------------------------------')
    print ("Welcome to setup folders for Python projects!")
    # url = "http://" + str(sys.argv[2])
    print('-----------------------------------')
    print('Path project: ' + project_path)
    print('Creating project folder: ' + project_name + ' Ok')
    print('-----------------------------------')


if __name__ == "__main__":
    create()