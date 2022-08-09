from datetime import datetime 

current_date = datetime.now()
print(current_date.strftime("%d"))
print(current_date.strftime("%m"))
print(current_date.strftime("%Y"))
print(current_date.strftime("GMT+3"))
print(current_date.strftime("%d-%m-%Y"))
print(current_date.strftime("%I"))
print(current_date.strftime("%H"))

print()

%d : jour(01 a 31)
%m : mois(01 a 12)
%Y : annee(ex:2022) - %y(00a 99)             
%H
