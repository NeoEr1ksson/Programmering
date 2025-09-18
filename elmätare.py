import datetime

start_year =input("Vilket start år: ")
start_month =input("Vilket start month: ")
start_day =input("Vilket start day: ")

end_year =input("Vilket slut år: ")
end_month =input("Vilket slut månad: ")
end_day =input("Vilket slut day: ")

start_year = int(start_year)
start_month = int(start_month)
start_day = int(start_day)

end_year = int(end_year)
end_month = int(end_month)
end_day = int(end_day)



start_date = datetime.datetime(start_year,start_month,start_day)
end_date = datetime.datetime(end_year,end_month,end_day) 

days = (end_date - start_date).days

print("khw kost")

kwh_prize = input()
kwh_prize = float(kwh_prize)

print("khw")
khw=input()
khw = int(khw)

print("dagsavgift")
Dagsavgift=input()
Dagsavgift = int(Dagsavgift)

print(f"Kostnaden blir: {(Dagsavgift * days + khw * kwh_prize) * 1.25}")