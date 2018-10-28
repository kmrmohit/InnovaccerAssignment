import requests
from bs4 import BeautifulSoup
import os,sys
from datetime import datetime
import month_num as mn

#the link provided by the above function is further scraped to find the details about that tv series
def getseriesdetails(link):
    details=""
    r = requests.get(link)
    c=r.content
    soup = BeautifulSoup(c,"html.parser")
    nextall = soup.find("div",{"class":"seasons-and-year-nav"})
    #print(nextall)
    nextall = nextall.find_all("a")
    for item in nextall:
        try:
            a = int(item.text)
            if (a>1000) :
                currentYear = datetime.now().year
                #print(currentYear)
                #print(a)
                if currentYear < a :
                    details="The next season begins in "
                    details+=str(a)
                    details+="."
                elif currentYear > a :
                    details="The show has finished streaming all its episodes.We will keep you updated!"
                else:
                    temp=nextall[0]
                    seasonlink = temp["href"]
                    #print(baselink+seasonlink)
                    rr = requests.get(baselink+seasonlink)
                    cc=rr.content
                    soupp = BeautifulSoup(cc,"html.parser")
                    nextalll = soupp.find_all("div",{"class":"airdate"})
                    #print(nextalll)
                    #print(len(nextalll[-1].text))
                    #print(nextalll[-2].text)
                    latestmon=datetime.now().month
                    latestday=datetime.now().day
                    for each in nextalll:
                        airtime = each.text.split()
                        try:
                            airtime[1]=mn.getmon(airtime[1])
                            airtime[0]=int(airtime[0])
                           
                            if(airtime[1]==datetime.now().month and airtime[0]>=datetime.now().day):
                                    latestday=airtime[0]
                                    latestmon=airtime[1]
                                    break
                                else:
                                    latestday=airtime[0]
                            elif(airtime[1]>datetime.now().month):
                                latestday=airtime[0]
                                latestmon=airtime[1]
                                break
                            else:
                                latestday=airtime[0]
                                latestmon=airtime[1]
                        except:
                            pass
                    try:
                        tempmon=latestmon
                        tempday=latestday
                        if latestmon in range(1,10):
                            latestmon = "0"+str(latestmon)
                        if latestday in range(1,10):
                            latestday = "0"+str(latestday)                        
                        ans=str(currentYear)+"-"+str(latestmon)+"-"+str(latestday)
                        if(tempmon<datetime.now().month or (tempmon==datetime.now().month and tempday<datetime.now().day)):
                            details="The show has finished streaming all its episodes.The last episode was aired on ";
                            details+=ans;
                        else:
                            details="Next episode airs on "+ans
                    except:
                        details="No Details Available"
        
                break
            else:
                pass
        except:
            pass
    return details
