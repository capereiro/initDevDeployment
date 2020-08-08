import os
import sys # Para manejo de I/O
import webbrowser # Para manejo de browser

# from selenium import web

browserName = "chrome"
path = ""
# browser = webdriver.Chrome()
# browser.get('http://github.com/login')

def create():
    browser = webbrowser.get(browserName)
    print ("hello world from create().py")
    folderName = str(sys.argv[1])
    url = "http://" + str(sys.argv[2])
    print('folderName: ' + folderName)
    print('wwwSite: ' + url)
    browser.open_new(url)



if __name__ == "__main__":
    create()

