import os
import sys # Para manejo de I/O
from dotenv import load_dotenv
from github import Github # API github
# import webbrowser # Para manejo de browser
# from selenium import webdriver


##### Variable loading process #####
load_dotenv()

url = "https://github.com/login"
usr = os.getenv("USERNAME")
psw = os.getenv("PASSWORD")
project_path = os.getenv("FILEPATH")
driver_path = os.getenv("DRIVER_PATH")
##### End variable loading #####

def create():
    project_name = str(sys.argv[1])
    
    user = Github(usr, psw).get_user()
    repo = user.create_repo(project_name)
  
    print('----------------------------------------------------------------')
    print ("Welcome to setup folders for Python projects!")
    print('----------------------------------------------------------------')
    print("Succesfully created github repository: {}".format(project_name))


if __name__ == "__main__":
    create()