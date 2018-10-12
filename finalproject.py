import mail
import config
import initialise
import connect_to_db
import serieslink as sl
import seriesdetails as sd
import sql_ops as sql


#scraping links
sublinks = ["/list/ls021409819/","/list/ls051600015/?st_dt=&mode=detail&sort=release_date,desc&page=1","/search/title?languages=hi&title_type=tv_series&page=1&sort=release_date,desc&view=advanced&ref_=adv_nxt"]
baselink = "https://www.imdb.com"

#my database had two tables:appusers and linker
#appusers had two columns:user_id and tvseries
#linker had two columns:user_id and email
mydb = connect_to_db.connect()
mycursor = mydb.cursor()
initialise.takeuserdata(mycursor,mydb)
mycursor.execute("SELECT * FROM linker")
ans = mycursor.fetchall()
mycursor.execute("SELECT * FROM appusers")
allusers = mycursor.fetchall()
for item in ans:
    userid = item[0]
    message=""
    for users in allusers:
        if users[0]==userid:
            seriesname=users[1]
            temp=""
            for links in sublinks:
                serieslink = sl.getserieslink(baselink,links,seriesname)
                #print(serieslink)
                if(len(serieslink)>0):
                    serieslink = baselink+serieslink
                    seriesdetails = sd.getseriesdetails(serieslink)
                    temp=seriesdetails
                    break
            if(len(temp)==0):
                message+="TV Series: " + seriesname.upper() +"\n" + "Status: "
                temp="No Details Available"
                message+=temp
            else:
                message+="TV Series: " + seriesname.upper() +"\n" + "Status: "
                message+=temp
            message+="\n\n"
    
    subject="YOUR FAVOURITE SHOWS'S CURRENT STATUS"
    msg = message
    mail.send_email(subject,msg,item[1])

mycursor.close()
mydb.close()
