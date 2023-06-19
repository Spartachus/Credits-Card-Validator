def cardchecker(card_num):
  if card_num[0] == 4 and len(card_num) == 16:
    validity = "Visa Card"
  elif card_num[0] == 5 and len(card_num) == 16:
    validity = "Master Card"
  elif card_num[0] == 3:
    if card_num[1] == 4 or card_num[2] == 7:
      if len(card_num) == 15:
        validity = "American Express"
  elif card_num[0] == 6 and len(card_num) == 16:
    validity = "Discover Card"
  else:
    validity = "Invalid Card Number"
  return validity

usr_num = input("Enter Your Card Number:\n")
print(len(usr_num))
print(cardchecker(usr_num))
