def get_valid_amount(prompt):
    while True:
        text=input(prompt)
        try:
            value=float(text)
        except:
            print("Please enter a number.")
            continue

        if value<=0:
            print("Amount must be more than zero.")
        else:
            return value

def get_valid_date(prompt):
    while True:
        date_text=input(prompt)
        if len(date_text)!=10:
            print("use format YYYY-MM-DD")
            continue

        if date_text[4]!="-"or date_text[7]!="-":
            print("use the format YYYY-MM-DD.")
            continue

        year=date_text[0:4]
        month=date_text[5:7]
        day=date_text[8:10]

        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            print("Year, Month and Day must be numbers.")
            continue

        year=int(year)
        month=int(month)
        day=int(day)

        if month<1 or month>12:
            print("Month must be between 1 and 12")
            continue

        if day<1 or day>31:
            print("Day must be between 1 and 31.")
            continue

        return date_text
    

def get_valid_year(prompt):
    while True:
        text=input(prompt)
        if text.isdigit() and len(text)==4:
            return int(text)
        else:
            print("enter a 4-digit year (e.g. 2007).")


def get_valid_month(prompt):
    while True:
        text=input(prompt)
        if text.isdigit():
            month=int(text)
            if 1<= month <=12:
             return month  
            
        print("Enter a month number between 1 and 12.")