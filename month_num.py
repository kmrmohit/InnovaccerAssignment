#this method calculates the numeric order of a month between 1 to 12, given the input in string data type
def getmon(month):
    mp={"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"july":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12}
    month = month.lower()
    month = month.replace(".","")
    num = mp[month]
    return num
