# WebScraping Project

#problem-statement

Write a python script to send e-mail to the users regarding the status of their favourite tv series to prevent them from spoilers

#solution

TO run this script just copy all the files in a folder and run the finalproject.py file.(One must have python and other necessary modules installed in their system).Before that ensure that config.py file has your email-address and its password and also lesssecureapps has been turned ON in your google account preferences(for checking that visit this:https://myaccount.google.com/lesssecureapps). Also ensure that connect_to_db.py file has the correct details filled up.For connecting to my database, one can email me on kcallingkarthi@gmail.com

All the other files are supporting modules.

The config.py file has the email address and the email password(may be of any company like gmail,hotmailc etc.) of the sender.

The connect_to_db.py file establishes the connection to the database on a server(may be your local host or an online service provider)

The initialise.py file is responsible for taking user input and storing them in the databse.

The mail.py file is responsible for sending e-mail to the reciever.The arguments have to be set accordingly.

The month_num.py file maps the string value of month name to numerical value(like jan to 1 and feb to 2)

The seriesdetails.py file gets the required message to be sent to the user about the details of a tv series.

The serieslink.py file gets the imdb link for a given tv series name as input.

The sql_ops.py file does all the mysql operations.
