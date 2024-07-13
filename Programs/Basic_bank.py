num = 246810
pin = 7887
bal = 50000
limit = 3
otp = [96946,34632,62503,99885,59065,33054,36833,68381,17209,20445,39452,91641,65812,85207,78451,96521]
print("***********  welcome to RS bank  ***********")
for i in range(3):
    num_1 = int(input("\nEnter your account number : "))

    if num_1 == num :
        pin_1 = int(input("\nEnter your account pin : "))

        if pin_1 == pin :
            print("\nyour account balance is : Rs.",bal)

            while True :
                print("\n1. credit amount to your account")
                print("2. debit amount from your account")
                print("3. transaction amount from your account")

                choice = int(input("\nEnter your choice (1/2/3) : "))
                if choice in (1,2,3):

                    if choice == 1 :
                        credit = int(input("\nEnter amount you are going to credit : Rs."))
                        chance = 3
                        for a in range(3) :
                            print("\notp is sent to your phone number : xxxxxx9283 ")
                            otp_s = otp.pop()
                            print("\nOTP for trancting amount Rs.",credit,"from yoor account : XXX810 is",otp_s)
                            otp_c = int(input("\nEnter the otp : "))

                            if otp_c == otp_s :
                                print("\nCorrect otp")
                                print("\nRs.",credit,"is credited suceffuly")
                                bal += credit
                                print("\nyour current bank balance is :",bal)
                                next = input("\nAre you going to transaction amount (y/n) : ")
                                if next == "y" :
                                    limit = 3
                                    chance = 3
                                    for i in range(3):
                                        t_num = input("\nEnter tranction account number (6 digit) : ")
                                        tot = 0
                                        
                                        for i in t_num:
                                            tot += 1
                                        digit = int(tot)
                                        if digit == 6:                     
                                            t_amount = int(input("\nEnter amount you are going to transact : Rs."))
                                            if t_amount < bal:
                                                for a in range(3) :
                                                    print("\notp is sent to your phone number : xxxxxx9283 ")
                                                    otp_s = otp.pop()
                                                    print("\nOTP for trancting amount Rs.",t_amount,"from yoor account : XXX810 is",otp_s)
                                                    otp_c = int(input("\nEnter the otp : "))

                                                    if otp_c == otp_s :
                                                        print("\nCorrect otp")
                                                        print("\nRs.",t_amount,"is transacted suceffuly")                                        
                                                        bal -= t_amount
                                                        print("\nyour current bank balance is : Rs.",bal)
                                                        print("\nThank you")
                                                        break
                                                    else:
                                                        chance -= 1
                                                        if chance > 0 :
                                                            print("\nWrong otp")
                                                            print(f"\nyou have only {chance} attempts")
                                                        if chance == 0 :
                                                            print("\nwrong otp")
                                                            print("\nYour account has blocked for 24 Hours")
                                                            break
                                                break   
                                        
                                            else:
                                                print("\nyour transaction amount is : Rs.",t_amount," and this is more than your bank balance : Rs.",bal)
                                                            
                                        else:
                                            limit -= 1
                                            print("\nEnter correct 6-digit account number but you entered",digit,"digit account number")
                                            if limit > 0 :
                                                print("\nyou have only",limit,"atempt")
                                            if limit == 0:
                                                print("\nyour bank account has locked for 24Hours")
                                                break
                                    break

                                else:
                                    print("\nThank you")
                                    break            

                            else:
                                chance -= 1
                                if chance > 0 :
                                    print("\nWrong otp")
                                    print(f"\nyou have only {chance} attempts")
                                if chance == 0 :
                                    print("\nwrong otp")
                                    print("\nYour account has blocked for 24 Hours")
                                    break

                    
                        break

                    if choice == 2 :
                        debit = int(input("\nEnter amount you are going to debit : Rs."))
                        chance = 3
                        
                        if debit < bal:
                            for a in range(3) :
                                print("\notp is sent to your phone number : xxxxxx9283 ")
                                otp_s = otp.pop()
                                print("\nOTP for debiting Rs.",debit,"from yoor account : XXX810 is",otp_s)
                                otp_c = int(input("\nEnter the otp : "))

                                if otp_c == otp_s :
                                    print("\nCorrect otp")
                                    print("\nRs.",debit,"is debited suceffuly")
                                    bal -= debit
                                    print("\nyour current bank balance is : Rs.",bal)
                                    print("\nThank you")
                                    break
                                else:
                                    chance -= 1
                                    if chance > 0 :
                                        print("\nWrong otp")
                                        print(f"\nyou have only {chance} attempts")
                                    if chance == 0 :
                                        print("\nwrong otp")
                                        print("\nYour account has blocked for 24 Hours")
                            break
                                
                        else:
                            print("\nyour's debit amount is : Rs.",debit,"and this is more than your bank balance : Rs.",bal)
                            
                    if choice == 3 :
                        limit = 3
                        chance = 3
                        for i in range(3):
                            t_num = input("\nEnter tranction account number (6 digit) : ")
                            tot = 0
                            
                            for i in t_num:
                                tot += 1
                            digit = int(tot)
                            if digit == 6:                     
                                t_amount = int(input("\nEnter amount you are going to transact : Rs."))
                                if t_amount < bal:
                                    for a in range(3):
                                        print("\notp is sent to your phone number : xxxxxx9283 ")
                                        otp_s = otp.pop()
                                        print("\nOTP for trancting amount Rs.",t_amount,"from yoor account : XXX810 is",otp_s)
                                        otp_c = int(input("\nEnter the otp : "))

                                        if otp_c == otp_s :
                                            print("\nCorrect otp")
                                            print("\nRs.",t_amount,"is transacted suceffuly")                                        
                                            bal -= t_amount
                                            print("\nyour current bank balance is : Rs.",bal)
                                            print("\nThank you")
                                            break
                                        else:
                                            chance -= 1
                                            if chance > 0 :
                                                print("\nWrong otp")
                                                print(f"\nyou have only {chance} attempts")
                                            if chance == 0 :
                                                print("\nwrong otp")
                                                print("\nYour account has blocked for 24 Hours")
                                                break
                                    break
                                else:
                                    print("\nyour transaction amount is : Rs.",t_amount," and this is more than your bank balance : Rs.",bal)
                                                        
                            else:
                                limit -= 1
                                print("\nEnter correct 6-digit account number but you entered",digit,"digit account number")
                                if limit > 0 :
                                    print("\nyou have only",limit,"atempt")
                                if limit == 0:
                                    print("\nyour bank account has locked for 24Hours")
                                    break
                        break        



                else:
                    print("\nwrong choice")
                    print("\nEnter a correct chhoice")
            
                
            break    
                
        else:
            print("\nWrong pin")
            limit -=1
            if limit > 0 :
                print("\nyou have only",limit,"atempt")
            if limit == 0:
                print("\nyour bank account has blocked for 24Hours")
                        
        
    else:
        limit -=1
        print("\nwrong account number")
        if limit > 0 :
            print("\nyou have only",limit,"atempt")
        if limit == 0:
            print("\nyour bank account has locked for 24Hours")
            
