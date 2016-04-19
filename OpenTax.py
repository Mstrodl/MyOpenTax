#!/usr/bin/env python3
print("************************************************************************")
print("*                                                                      *")
print("*  6. Disclaimer of Warranty                                           *")
print("*  -------------------------                                           *")
print("*                                                                      *")
print("*  Covered Software is provided under this License on an "as is"       *")
print("*  basis, without warranty of any kind, either expressed, implied, or  *")
print("*  statutory, including, without limitation, warranties that the       *")
print("*  Covered Software is free of defects, merchantable, fit for a        *")
print("*  particular purpose or non-infringing. The entire risk as to the     *")
print("*  quality and performance of the Covered Software is with You.        *")
print("*  Should any Covered Software prove defective in any respect, You     *")
print("*  (not any Contributor) assume the cost of any necessary servicing,   *")
print("*  repair, or correction. This disclaimer of warranty constitutes an   *")
print("*  essential part of this License. No use of any Covered Software is   *")
print("*  authorized under this License except under this disclaimer.         *")
print("*                                                                      *")
print("************************************************************************")
print("")
print("************************************************************************")
print("*                                                                      *")
print("*  7. Limitation of Liability                                          *")
print("*  --------------------------                                          *")
print("*                                                                      *")
print("*  Under no circumstances and under no legal theory, whether tort      *")
print("*  (including negligence), contract, or otherwise, shall any           *")
print("*  Contributor, or anyone who distributes Covered Software as          *")
print("*  permitted above, be liable to You for any direct, indirect,         *")
print("*  special, incidental, or consequential damages of any character      *")
print("*  including, without limitation, damages for lost profits, loss of    *")
print("*  goodwill, work stoppage, computer failure or malfunction, or any    *")
print("*  and all other commercial damages or losses, even if such party      *")
print("*  shall have been informed of the possibility of such damages. This   *")
print("*  limitation of liability shall not apply to liability for death or   *")
print("*  personal injury resulting from such party's negligence to the       *")
print("*  extent applicable law prohibits such limitation. Some               *")
print("*  jurisdictions do not allow the exclusion or limitation of           *")
print("*  incidental or consequential damages, so this exclusion and          *")
print("*  limitation may not apply to You.                                    *")
print("*                                                                      *")
print("************************************************************************")
print("")
print("If you agree to these terms as well as the terms in LICENSE, please enter 'I understand the lack of warranty'")
warranty = input("Enter text: ")
if warranty == "I understand the lack of warranty":
  print("Thank you! Starting MyOpenTax now!")
else:
  print("Exiting because the user doesn't understand the lack of warranty ;-(")
  exit()

def FedNeedToFile(FilingStat, Dec31Age, MyGrossIncome, SpouseDec31Age=0, SelfEmploymentNetEarnings=0, GotPremiumCred=False):
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
  elif GotPremiumTaxCred:
    return True
  elif SelfEmploymentNetEarnings >= 400:
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

#def FedCheckTaxCredits(FilingStat, MyGrossIncome):
#    EITC = FedCheckEITC()

#def FedCheckEITC(FilingStat, Dec31Age, SpouseDec31Age, MonthsInCountry, SpouseMonthsInCountry, ValidSocialSecurity, SpouseValidSocialSecurity, DependentOnOthersTaxReturn, SpouseDependentOnOthersTaxReturn):
#  if FilingStat == "FilingJointly" and Dec31Age >= 25 and Dec31Age < 65 and MonthsInCountry > 6 and SpouseMonthsInCountry > 6 and ValidSocialSecurity and SpouseValidSocialSecurity and not DependentOnOthersTaxReturn and not SpouseDependentOnOthersTaxReturn:
#    return True
#  if FilingStat == "Single" and 

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
  print("Please enter your net earnings from self-employment (income minus expenses) (if applicable. Otherwise, enter 0)")
  SelfEmploymentNetEarnings = int(input("Enter Number: "))
  print("Do you have marketplace health insurance and have received advanced payments for the premium tax credit?")
  GotPremiumCred = input("Enter Y or N: ")
  if GotPremiumCred = "Y":
    GotPremiumCred = True
  else:
    GotPremiumCred = False
  print("Federal Income Tax:")
  print("$" + str(FedCalculateIncomeTax(FilingStat, MyGrossIncome))
  print("")
  if FedNeedToFile(FilingStat, Dec31Age, MyGrossIncome, SpouceDec31Age, SelfEmploymentNetEarnings, GotPremiumCred):
    print("* You need to file a tax return")
  else:
    print("* You don't need to file a federal tax return, BUT you may want to:")
    print(" - To get your tax withholdings back
    print(" - To get refundable credits you qualify for, like the  Earned Income Credit, the Additional Child Tax Credit, or the American Opportunity Credit")
Main()
  
