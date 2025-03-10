import pandas
import datetime as dt
import random
import smtplib

# checking today's day and month
now = dt.datetime.now()
month = now.month
day = now.day


# getting the info from the data
with open("birthdays.csv") as file :
    df = pandas.read_csv(file)
birthday = (df[df.day == day])

name=""
mail=""
row_month=""
row_day=""
for index,row in birthday.iterrows():
    name=row["name"]
    mail=row.email
    row_month=row.month
    row_day=row.day
print(type(mail))
print(type(name))

# confirming the day and month
if day == row_day and row_month==month:


# picking letter
    letter_no = random.randint(1,3)
    placeholder = "[NAME]"
    with open(f"./letter_templates/letter_{letter_no}.txt") as data:
        letter=data.read()
    letter = letter.replace(placeholder,name)

    print(letter)

# sending mail
    my_email = "shahzaibkhalid1101@gmail.com"
    key = "vtuwsfiplzfrzyjl"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email , password=key)
        connection.sendmail(from_addr=my_email,
                            to_addrs=mail,
                            msg=f"Happy Birthday\n\n{letter}")
