import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def calendar(year:int, month:int)->None:
 """
 Imprime um calendário específico de algum ano e mês especificados.
 
 Args:
  year (int): Ano que se deseja obter o calendário. O valor máximo é 
  9999 e o valor mínimo é 1.
  month (int): Mês do ano de que se deseja obter o calendário. O valor 
  máximo é 12 e o valor mínimo é 1.
 
 Returns:
  None: Não retorna nada.
 
 Version:
  1.0.0
 
 Copyright:
  (c) 2024 Copyright, Siael Alves
 """
 if year == 0:
  print("O ano não pode ser igual a 0 (zero).")
  return

 if year > 9999:
  print("O ano não pode ser maior que 9999.")
  return
 
 if month == 0:
  print("O mês não pode ser igual a 0 (zero).")
  return
 
 if month > 12:
  print("O mês não pode ser maior que 12.") 
  return

 date = datetime.date(year, month, 1)

 firstDay:int = date.min.day 
 lastday:int = date.max.day
 year:int = date.year
 monthName:str = date.strftime("%B")

 if year > 100:
  header:str = f"{monthName} de {year}"
 else:
  header:str = f"{monthName} do ano {year}"

 divisory:str = f"=================================================="
 weekDays:str = f"D\tS\tT\tQ\tQ\tS\tS"
 
 print(header)
 print(divisory)
 print(weekDays)

 for week in range(0, 5):
  empty:str = ""

  for tab in range(0, date.weekday() + 1):
   if (week == 0) or (date.weekday() > 0) or (date.weekday() < 6):
    empty = empty + "\t"


  for day in range(firstDay, firstDay + 7):
   day = day + (week * 7)

   if day == firstDay:
    print(f"{empty}", end="")
   
   if day == lastday:
    break
   
   actual = datetime.date(year, month, day)

   if actual.weekday() == 6:
    print(f"")

   print(f"{day}\t", end="")

   if day == lastday:
    break

 print("")

calendar(101, 13)