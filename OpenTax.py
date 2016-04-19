#!/usr/bin/env python3

def FedNeedToFile(FilingStat, Dec31Age, MyGrossIncome, SpouseDec31Age=0):
  if FilingStat == "Single" and Dec31Age < 65 and MyGrossIncome >= 10,300:
    return True
  elif FilingStat == "Single" and Dec31Age >= 65 and MyGrossIncome >= 11,850:
    return True
  elif FilingStat == "FilingJointly" and Dec31Age < 65 and SpouseDec31Age < 65 and MyGrossIncome >= 20,600:
    return True
  elif FilingStat == "FilingJointly" and Dec31Age >= 65 and SpouseDec31Age >= 65 MyGrossIncome >= 23,000:
    return True
  elif FilingStat == "FilingJointly" and Dec31Age >= 65 and SpouseDec31Age < 65 MyGrossIncome >= 21,800:
    return True
  elif FilingStat == "FilingJointly" and Dec31Age < 65 and SpouseDec31Age >= 65 MyGrossIncome >= 21,800:
    return True
  elif FilingStat == "FilingSeperately" and MyGrossIncome >= 3,950:
    return True
  elif FilingStat == "HeadofHouse" and Dec31Age < 65 and MyGrossIncome >= 13,050:
    return True
  elif FilingStat == "HeadofHouse" and Dec31Age >= 65 and MyGrossIncome >= 14,600:
    return True
  elif FilingStat == "Widow" and Dec31Age < 65 and MyGrossIncome >= 16,100:
    return True
  elif FilingStat == "Widow" and Dec31Age >= 65 and MyGrossIncome >= 17,300:
    return True
  return False
  
def FedIncomeTaxPercent(FilingStat, MyGrossIncome):
  if FilingStat == "Single" and MyGrossIncome >= 1 and MyGrossIncome <= 9,225:
    return 10
  elif FilingStat == "Single" and MyGrossIncome >= 9,226 and MyGrossIncome <= 37,450:
    return 15
  elif FilingStat == "Single" and MyGrossIncome >= 37,451 and MyGrossIncome <= 90,750:
    return 25
  elif FilingStat == "Single" and MyGrossIncome >= 90,751 and MyGrossIncome <= 189,300:
    return 28
  elif FilingStat == "Single" and MyGrossIncome >= 189,301 and MyGrossIncome <= 411,500:
    return 33
  elif FilingStat == "Single" and MyGrossIncome >= 411,501 and MyGrossIncome <= 413,200:
    return 35
  elif FilingStat == "Single" and MyGrossIncome > 413,200:
    return 39.6
  elif MyGrossIncome >= 1 and MyGrossIncome <= 18,450 and FilingStat == "FilingJointly" or FilingStat == "Widow":
    return 10
  elif MyGrossIncome >= 18,451 and MyGrossIncome <= 74,900 and FilingStat == "FilingJointly" or FilingStat == "Widow":
    return 15
  elif MyGrossIncome >= 74,901 and MyGrossIncome <= 151,200 and FilingStat == "FilingJointly" or FilingStat == "Widow":
    return 25
  elif MyGrossIncome >= 151,201 and MyGrossIncome <= 230,450 and FilingStat == "FilingJointly" or FilingStat == "Widow":
    return 28
  elif MyGrossIncome >= 230,451 and MyGrossIncome <= 411,500 and FilingStat == "FilingJointly" or FilingStat == "Widow":
    return 33
  elif MyGrossIncome <= 464,850 and FilingStat == "FilingJointly" or FilingStat == "Widow":
    return 35
  elif FilingStat == "FilingJointly" and MyGrossIncome > 464,850:
    return 39.6
  elif FilingStat == "HeadofHouse" and MyGrossIncome >= 1 and MyGrossIncome <= 13,150:
    return 10
  elif FilingStat == "HeadofHouse" and MyGrossIncome >= 13,151 and MyGrossIncome <= 50,200:
    return 15
  elif FilingStat == "HeadofHouse" and MyGrossIncome >= 50,201 and MyGrossIncome <= 129,600:
    return 25
  elif FilingStat == "HeadofHouse" and MyGrossIncome >= 129,601 and MyGrossIncome <= 209,850:
    return 28
  elif FilingStat == "HeadofHouse" and MyGrossIncome >= 209,851 and MyGrossIncome <= 411,500:
    return 33
  elif FilingStat == "HeadofHouse" and MyGrossIncome >= 411,501 and MyGrossIncome <= 439,200:
    return 35
  elif FilingStat == "HeadofHouse" and MyGrossIncome > 439,200:
    return 39.6
  elif FilingStat == "FilingSeperately" and MyGrossIncome >= 1 and MyGrossIncome <= 9,225:
    return 10
  elif FilingStat == "FilingSeperately" and MyGrossIncome >= 9,226 and MyGrossIncome <= 37,450:
    return 15
  elif FilingStat == "FilingSeperately" and MyGrossIncome >= 37,451 and MyGrossIncome <= 75,600:
    return 25
  elif FilingStat == "FilingSeperately" and MyGrossIncome >= 75,601 and MyGrossIncome <= 115,225:
    return 28
  elif FilingStat == "FilingSeperately" and MyGrossIncome >= 115,226 and MyGrossIncome <= 205,750:
    return 33
  elif FilingStat == "FilingSeperately" and MyGrossIncome >= 205,751 and MyGrossIncome <= 232,425:
    return 35
  elif FilingStat == "FilingSeperately" and MyGrossIncome > 232,425:
    return 39.6

def FedCalculateIncomeTax(FilingStat, MyGrossIncome)
  return MyGrossIncome * FedIncomeTaxPercent(FilingStat, MyGrossIncome) / 100

def FilingStatNumberToString(FilingStatNumber):
  sn = FilingStatNumber
  if sn == 1:
    return "Single"
  elif sn == 2:
    return "FilingJointly"
  elif sn == 3:
    return "FilingSeperately"
  elif sn == 4:
    return "HeadofHouse"
  elif sn == 5:
    return "Widow"
  elif sn > 1 or sn > 5:
    return False

def Main():
  print("Please enter the number assigned to your filing status:")
  print("")
  print("1: Single")
  print("2: Married Filing Jointly")
  print("3: Married Filing Separately")
  print("4: Head of Household")
  print("5: Qualifying Widow(er)")
  print("")
  FilingStatNumber = int(input("Enter Number: "))
  FilingStat = FedStatNumberToString(FilingStatNumber)
  print("Please enter your gross income:")
  MyGrossIncome = int(input("Enter Number: "))
  print("Please enter your age in years on December 31st:")
  Dec31Age = int(input("Enter Number: "))
  if FilingStat == "FilingJointly":
    print("Please enter the age of your spouse in years on December 31st")
    SpouseDec31Age = int(input("Enter Number: "))
  else:
    SpouseDec31Age = int(0)
  print("Federal Income Tax:")
  print("$" + str(FedCalculateIncomeTax(FilingStat, MyGrossIncome))
  if FedNeedToFile(FilingStat, Dec31Age, MyGrossIncome, SpouceDec31Age):
    print("And you need to file taxes")
  else:
    print("But you don't need to file taxes")
Main()
  
