import os
import sys # Para manejo de I/O
import webbrowser # Para manejo de browser
from selenium import webdriver
from dotenv import load_dotenv

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
    # browser = webbrowser.get(browserName)
    print('-----------------------------------')
    print ("Welcome to setup folders for Python projects!")
    folderName = str(sys.argv[1])
    # url = "http://" + str(sys.argv[2])
    print('-----------------------------------')
    print('Path project: ' + project_path)
    print('Creating project folder: ' + folderName + ' Ok')
    print('-----------------------------------')
    
    ##### Folder management #####
    # os.mkdir(project_path + folderName)

    login_site(url, usr, psw)
 

def login_site(url, usr, psw):
    ##### Web Login Process #####
    # Openning the browser in the correct site
    browser.get(url)
    # Login process
    browser.find_element_by_xpath("//*[@id='login_field']").send_keys(usr)
    browser.find_element_by_xpath("//*[@id='password']").send_keys(psw)
    browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").click()
    ##### End Web Login Process #####

    ##### Create Github proyect #####
    browser.find_element_by_xpath("/html/body/div[1]/header/div[6]/details/summary").click()
    browser.find_element_by_xpath("/html/body/div[1]/header/div[6]/details/details-menu/a[1]").click()

    # No avancé mas porque aprendí lo que necesitaba
    ##### End create Github proyect #####
    

if __name__ == "__main__":
    create()