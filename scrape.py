from . import serieslink as sl
from . import seriesdetails as sd

#scraping links
sublinks = ["/list/ls021409819/","/list/ls051600015/?st_dt=&mode=detail&sort=release_date,desc&page=1","/search/title?languages=hi&title_type=tv_series&page=1&sort=release_date,desc&view=advanced&ref_=adv_nxt"]
baselink = "https://www.imdb.com"

def link(seriesname):
    temp=""
    message=""
    for links in sublinks:
        serieslink = sl.getserieslink(baselink,links,seriesname)
        #print(serieslink)
        if(len(serieslink)>0):
            serieslink = baselink+serieslink
            print(serieslink)
            seriesdetails = sd.getseriesdetails(serieslink)
            temp=seriesdetails
            break
    if(len(temp)==0):
        message+= "Status: "
        temp="No Details Available"
        message+=temp
    else:
        message+= "Status: "
        message+=temp
    return message

