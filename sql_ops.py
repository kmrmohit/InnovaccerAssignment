#this method inserts data into the mysql database
#data is a tuple that has two values in it.First is the user_id and second is the name of the tvseries liked by the user
#any insertion and deletion takes place through explicit call through mysql commands
#my database had two tables:appusers and linker
#appusers had two columns:user_id and tvseries
#linker had two columns:user_id and email
def insert_to_db(mycursor,mydb,data):
    sqlformulains = "INSERT INTO appusers (user_id,tvseries) VALUES (%s,%s)"
    mycursor.execute(sqlformulains,data)
    mydb.commit()
    return

#below two methods deletes data from the database in case the user wants to update its preferences or withdraw from the service
def delete_from_db(mycursor,mydb,uid):
    sqlformuladel ="DELETE FROM appusers WHERE user_id = "
    sqlformuladel += '"'
    sqlformuladel += uid
    sqlformuladel += '"'
    mycursor.execute(sqlformuladel)
    sqlformuladel ="DELETE FROM linker WHERE user_id = "
    sqlformuladel += '"'
    sqlformuladel += uid
    sqlformuladel += '"'
    mycursor.execute(sqlformuladel)
    mydb.commit()
    return

def delete_from_appusers(mycursor,mydb,uid,seriesname):
    sqlformuladel ="DELETE FROM appusers WHERE user_id = "
    sqlformuladel += '"'
    sqlformuladel += uid
    sqlformuladel += '"'
    sqlformuladel += 'and '
    sqlformuladel += 'tvseries = '
    sqlformuladel += '"'
    sqlformuladel += seriesname
    sqlformuladel += '"'
    mycursor.execute(sqlformuladel)
    mydb.commit()

#this method is for getting the count of row or the number of users in the database
def get_rows(mycursor,mydb):
    mycursor.execute("SELECT * FROM linker")
    ans = mycursor.fetchall()
    n = len(ans)
    return n
