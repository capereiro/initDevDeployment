import os
import sys # Para manejo de I/O
import webbrowser # Para manejo de browser
from selenium import webdriver

url = "https://github.com/login"
usr = "capereiro@gmail.com"
psw = "digital911.Com"

#  Browser driver name & path vars
# browserName = "chrome"

# Para utilizar en macbook 15
# driver_path = "/Users/carlospereiro/Documents/SOFTWARE-DEVELOPMENT/DRIVERS/CHROME/chromedriver"
# Para utilizar en iMac
driver_path = "/Users/carlos/Documents/SOFTWARE-DEVELOPMENT/DRIVERS/CHROME/chromedriver"

browser = webdriver.Chrome(executable_path=driver_path)
# browser = webdriver.Chrome(driver_path)
# browser.get(webScrappingName)

# Para utilizar en iMac
project_path = "/Users/carlos/Documents/SOFTWARE-DEVELOPMENT/PYTHON/initDevDeployment/"
# Para utilizar en macbook 15
# project_path = "/Users/carlospereiro/Documents/SOFTWARE-DEVELOPMENT/CARLOS/PYTHON/initDevDeployment/"



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


    browser.find_element_by_xpath("/html/body/div[1]/header/div[6]/details/summary").click()
    browser.find_element_by_xpath("/html/body/div[1]/header/div[6]/details/details-menu/a[1]").click()

    

if __name__ == "__main__":
    create()

