import requests
from bs4 import BeautifulSoup
import os,sys
from datetime import datetime


#this method is responsible for web scraping and finding the imdb link for the tvseries which we are searching for
def getserieslink(baselink,s,seriesname):
    serieslink=""
    while 1==1 :
        #print(baselink+s)
        r = requests.get(baselink+s)
        c=r.content
        soup = BeautifulSoup(c,"html.parser")
        try:
            nextall = soup.find_all("div",{"class":"lister-item mode-detail"})
            for item in nextall:
                next1 = item.find_all("h3",{"class":"lister-item-header"})[0]
                temp=next1.find("a").text
                #print(temp.lower())
                #print(temp.lower())
                if(temp.lower() == seriesname.lower()):
                    href = next1.find_all("a")[0]
                    href = href["href"]
                    serieslink=href
            if(len(serieslink)>0):
                break
            else:
                
                    nextpage = soup.find("div",{"class":"list-pagination"})
                    #print(nextpage)
                    nextpage = nextpage.find_all("a")[1]
                    #print(nextpage["href"])
                    if(nextpage["href"] != "#"):
                        s=nextpage["href"]
                    else:
                        break
               
                    
        except:
            nextall = soup.find_all("div",{"class":"lister-item mode-advanced"})
            for item in nextall:
                next1 = item.find_all("h3",{"class":"lister-item-header"})[0]
                temp=next1.find("a").text
                #print(temp.lower())
                #print(temp.lower())
                if(temp.lower() == seriesname.lower()):
                    href = next1.find_all("a")[0]
                    href = href["href"]
                    serieslink=href
                    break
            if(len(serieslink)>0):
                break
            else:
                nextpage = soup.find("div",{"class":"nav"})
                #print(nextpage)
                try:
                    nextpage = nextpage.find_all("a")
                    temp=nextpage[0]
                    if(temp.text.lower()=="next"):
                        s=temp["href"]
                        break
                    else:
                        temp=nextpage[1]
                        if(temp.text.lower()=="next"):
                            s=temp["href"]
                            break
                        else:
                            temp=nextpage[2]
                            if(temp.text.lower()=="next"):
                                s=temp["href"]
                                break
                            else:
                                break
                    s="/search/title"+s
                except:
                    break
    return serieslink
