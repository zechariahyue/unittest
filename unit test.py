import datetime
symbol = input("Enter Symbol: ") # Ask user for input 
if symbol.isalpha() == True and len(symbol) == 7 and symbol.isupper() == True: # Check for vaildity
  print("Valid Symbol") # Print Message
else:
  print("Invalid Symbol") # Print Message

try:
  chart_type = int(input("Enter Chart Type: ")) # Ask user for input
  if chart_type == 1 or chart_type == 2:  # Check for vaildity
    print("Valid Chart Type") # Print Message
  else:
    print("Invaild Chart Type")  # Print Message
except ValueError:
  print("Invaild Chart Type") # Print Message

try:
  time_series = int(input("Enter Time Series: ")) # Ask user for input
  if time_series > 0 and time_series < 5:  # Check for vaildity
    print("Valid Time Series") # Print Message
  else:
    print("Invaild Time Series")  # Print Message
except ValueError:
  print("Invaild Time Series") # Print Message

date_string = input("Enter start date in the format YYYY-MM-DD: ") # Ask user for input
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format) # Check for vaildity
  print("Vaild date format") # Print Message
except ValueError:
  print("Invaild date format, please enter in YYYY-MM-DD format") # Print Message

date_string = input("Enter end date in the format YYYY-MM-DD: ") # Ask user for input
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format) # Check for vaildity
  print("Vaild date format") # Print Message
except ValueError:
  print("Invaild date format, please enter in YYYY-MM-DD format") # Print Message