from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\Daryl\Documents\geckodriver\geckodriver.exe')
browser.get('http://localhost:8000')
assert 'Django' in browser.title