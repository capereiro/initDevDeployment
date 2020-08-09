import os
import sys # Para manejo de I/O
import webbrowser # Para manejo de browser
from selenium import webdriver

# Browser driver name & path vars
# browserName = "chrome"

driver_path = "/Users/carlos/Documents/SOFTWARE-DEVELOPMENT/DRIVERS/CHROME/chromedriver"
browser = webdriver.Chrome(executable_path=driver_path)
# browser = webdriver.Chrome(driver_path)
browser.get('https://github.com/login')

project_path = "/Users/carlos/Documents/SOFTWARE-DEVELOPMENT/PYTHON/initDevDeployment/"
webScrappingName = "https://github.com/login"

usr = "capereiro@gmail.com"
psw = "digital911.Com"





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

