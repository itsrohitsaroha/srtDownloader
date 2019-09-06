from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


def createBrowser(val):
	browser =None
	if(val == 1):
		ffprofile = webdriver.FirefoxProfile()
		ffprofile.set_preference("dom.webnotifications.enabled", False)
		browser=webdriver.Firefox(ffprofile)
	elif(val ==2):
		print("CHROME")

	return browser


def playlistLink(s,page):
	overview = page.find_all('a', {'class' :'style-scope ytd-playlist-video-renderer'})

	listt = []

	for over in overview:
		x = over.get('href')
		if(x != None):
			x="https://www.youtube.com"+x
			listt.append(x)

	return listt

def EndOfBrowser(browser):
	SCROLL_PAUSE_TIME = 2
	# Get scroll height
	last_height = browser.execute_script("return document.body.scrollHeight")
	
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")		 
	return 


def srtDownload(url,browser):

	browser.get("https://keepvid.com/?url="+url)
	
	EndOfBrowser(browser)
	page = BeautifulSoup(browser.page_source,'lxml')
	overview = page.find('a', {'class' :'btn btn-outline btn-sm subtitle-a'})
		
	x = overview.get('href')
	if(x != None):
		browser.get(x)
		print("[+] Done URL = "+url)
	else:
		print("[-] subtitle not found URL = " + url)
	return 

def playlist(string):
	temp =string.split("list=")
	url = "https://www.youtube.com/playlist?list="
	if(len(temp) >1):
		url = url + temp[1]

	browser.get(url)
	page = BeautifulSoup(browser.page_source,'lxml')

	finalList = playlistLink(url,page)

	return finalList




def main(browser):
	string  = str(input())
	finalList=[string]
	if "list=" in string:
		finalList = playlist(string)

	for e in finalList:
		if("watch" in e):
			srtDownload(e,browser)
		else:
			print("[---] invalid URL" + e)



browser = createBrowser(1)
main(browser)

browser.quit()
