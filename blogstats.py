import requests
import json
import datetime
import dateutil.parser
from os import path
from typing import List

articleStats = ""
statstxt = ""
dzoneid = "" # enter the user's Dzone ID here
devtoapikey = '' #enter the user's Dev.to API key here

statsTxtFilename = "blogstats.csv"
dzoneurl = "https://dzone.com/services/widget/article-listV2/list?author="+dzoneid+"&portal=all&sort=newest"
devtourl = "https://dev.to/api/articles/me"
devtoheaders = {
    'api-key': devtoapikey, # You have to put your own api-key here. How to get a api-key: https://docs.dev.to/api/#section/Authentication/api_key
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

#get Dev.to stats
devToJson = requests.get(devtourl, headers=devtoheaders).json() # Call the api to retrieve the statustics

for articleFromDev in devToJson:
	publishedObj = dateutil.parser.isoparse(articleFromDev['published_at'])
	publishedStr = datetime.datetime.strftime(publishedObj, "%d-%m-%Y %H:%M:%S")
	devtopublishedTxtStr = datetime.datetime.strftime(publishedObj, "%m/%d/%Y")
	devtotitle = articleFromDev['title']
	devtourl = articleFromDev['url']
	devtopageViews = articleFromDev['page_views_count']
	#reactions = articleFromDev['public_reactions_count']
	#comments = articleFromDev['comments_count']
	statstxtitem = "\""+devtotitle+"\""+","+devtopublishedTxtStr+",Dev.to,"+devtourl+","+str(devtopageViews)+"\n"
	statstxt = statstxt + statstxtitem
	statstxtitem = ""

#get Dzone.com stats
DzoneToJson = requests.get(dzoneurl).json() # Call the api to retrieve the statustics
for articlelist in DzoneToJson['result']['data']['nodes']:
	pubdate = articlelist['articleDate']
#	publishedStr = datetime.strptime(pubdate, "%Y-%m-%d")
#	publishedTxtStr = datetime.strftime(publishedObj, "%m/%d/%Y")
	title = articlelist['title']
	views = articlelist['views']
	articleLink = articlelist['articleLink']
	statstxtitem = "\""+title+"\""+","+pubdate+",dzone.com,"+articleLink+","+str(views)+"\n"
	statstxt = statstxt + statstxtitem
	statstxtitem = ""

statsFileTxt = open(statsTxtFilename, 'w') # Save the article stats to the statistics csv file
statsFileTxt.write(statstxt)
statsFileTxt.close()