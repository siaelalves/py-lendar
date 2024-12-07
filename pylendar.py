import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def calendar(year:int, month:int)->int|str:
 """
 Obtém uma string que representa um calendário de algum ano e mês 
 especificado que pode ser impresso na tela.
 
 ## Args:
  year (int): Ano que se deseja obter o calendário. O valor máximo é 
  9999 e o valor mínimo é 1.
  month (int): Mês do ano de que se deseja obter o calendário. O valor 
  máximo é 12 e o valor mínimo é 1.
 
 ## Returns:
  str: Retorna uma string que contém o mês, ano e dias da semana do ano 
  e mês especificados.

  int: Retorna um integer negativo que representa um erro específico 
   conforme a lista abaixo:
   - -1 se o ano for igual a 0 (zero);
   - -2 se o ano for maior que 9999;
   - -3 se o mês for igual a 0 (zero);
   - -4 se o mês for maior que 12;
 
 ## Version:
  1.0.0
 
 ## Copyright:
  (c) 2024 Copyright, Siael Alves
 """
 if year == 0:
  print("O ano não pode ser igual a 0 (zero).")
  return -1

 if year > 9999:
  print("O ano não pode ser maior que 9999.")
  return -2
 
 if month == 0:
  print("O mês não pode ser igual a 0 (zero).")
  return -3
 
 if month > 12:
  print("O mês não pode ser maior que 12.") 
  return -4

 calendarStr:str = ""
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
 
 calendarStr += f"{header}\n"
 calendarStr += f"{divisory}\n"
 calendarStr += f"{weekDays}\n"

 for week in range(0, 5):
  empty:str = ""

  for tab in range(0, date.weekday() + 1):
   if (week == 0) or (date.weekday() > 0) or (date.weekday() < 6):
    empty = empty + "\t"


  for day in range(firstDay, firstDay + 7):
   day = day + (week * 7)

   if day == firstDay:
    calendarStr += f"{empty}"
   
   if day == lastday:
    break
   
   actual = datetime.date(year, month, day)

   if actual.weekday() == 6:
    calendarStr += f"\n"

   calendarStr += f"{day}\t"

   if day == lastday:
    break

 calendarStr += f"\n"
 return calendarStr