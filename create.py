import os
import sys # Para manejo de I/O
import webbrowser # Para manejo de browser
from selenium import webdriver

webScrappingName = "https://github.com/login"
usr = "capereiro@gmail.com"
psw = "digital911.Com"

#  Browser driver name & path vars
# browserName = "chrome"

# Para utilizar en macbook 15
driver_path = "/Users/carlospereiro/Documents/SOFTWARE-DEVELOPMENT/DRIVERS/CHROME/chromedriver"
# Para utilizar en iMac
# driver_path = "/Users/carlos/Documents/SOFTWARE-DEVELOPMENT/DRIVERS/CHROME/chromedriver"

browser = webdriver.Chrome(executable_path=driver_path)
# browser = webdriver.Chrome(driver_path)
browser.get(webScrappingName)

# Para utilizar en iMac
# project_path = "/Users/carlos/Documents/SOFTWARE-DEVELOPMENT/PYTHON/initDevDeployment/"
# Para utilizar en macbook 15
project_path = "/Users/carlospereiro/Documents/SOFTWARE-DEVELOPMENT/CARLOS/PYTHON/initDevDeployment/"



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
    os.mkdir(project_path + folderName)

    # Scrapping
    # browser.open_new(webScrappingName)

    # python_button = browser.find_element_by_xpath("//*[@id='login_field']")[0]
    # python_button.click()

if __name__ == "__main__":
    create()

