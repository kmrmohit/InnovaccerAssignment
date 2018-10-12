# InnovaccerAssignment
SDE-Intern(Platform) assignment project for Innovacer.

#problem-statement
Write a python script to send e-mail to the users regarding the status of their favourite tv series to prevent them from spoilers

#solution

TO run this script just copy all the files in a folder and run the finalproject.py file.(One must have python and other necessary modules installed in their system)

All the other files are supporting modules.

The config.py file has the email address and the email password(may be of any company like gmail,hotmailc etc.)

The connect_to_db.py file establishes the connection to the database on a server(may be your local host or online)

The initialise.py file is responsible for taking user input and storing them in the databse.

The mail.py file is responsible for sending e-mail to the reciever.The arguments have to be set accordingly.

The month_num.py file maps the string value of month name to numerical value(like jan to 1 and feb to 2)

The seriesdetails.py file gets the required message to be sent to the user about the details of a tv series.

The serieslink.py file gets the imdb link for a given tv series name as input.

The sql_ops.py file does all the mysql operations.
