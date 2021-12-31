# num=1
# while num<=100:
#     if num%3==0:
#         print("nav")
#     if num%7==0:
#         print("gurukul")
#     if (num%3==0 and num%7==0):
#         print("navgurukul")
#     else:
#         print(num)
#     num=num+1

#########################################

# total=0
# count=50
# while count>40:
#     a=int(input())
#     total=total+a
#     count=count-1
# print(total)
#
######################################
# bina multiple kiye bina multiple krna 
# g=0
# c=0
# a=int(input())
# b=int(input())
# while c<a:
#     g=g+b
#     c=c+1
# print(g)
#############################################
#
#b=0
#a=1
#while b<10:
#    b=a/2
#    print(a)
#    a=a+1         
##################################################
# counter=156
# while counter>146:
# 	b=(counter-146)-11
# 	counter=counter-1
# 	print(-b)
################################################
# d=0
# a=int(input("kitni baar input le"))
# while a>0:
# 	b=int(input())
# 	a=a-1
# 	d=d+b
# print(d)
##############################################3
# a=int(input())
# for i in range(1,a):
# 	for j in range(1,i+1):
# 		print ("*",end="")
# 	print("")

#####################################333
# a=int(input())
# for i in range (a,0,-1):
# 	for j in range (1,i+1):
# 		print("*",end="")
# 	print("")	
####################################3
# a=int(input())
# for i in range (1,a):
# 	for k in range (1,a-1):
# 		print("",end="")
# 	for j in range (1,i+1):	
# 		print("*",end="")
# 	print("")

########################################33


# a=int(input())
# b=0
# while b<a:
# 	print(""*(a-b-1)+"*"*(b+1))
# 	b+=1

#############################################################


# a=int(input())
# for i in range(a):
# 	print(""*(a-i-1)+"*"*(i+1))


###############################################
# a=int(input())
# b=1
# c=b+a
# for i in range(a):
# 	print(""*c,"*"*b)
# 	b=b+1
# 	c=c+1

####################################################3

# num=20
# while num<=100:
# 	if num%2==0:
# 		print(num)
# 	num+=1


############################################
# num=1
# while num<=100:
# 	if num%7==0:
# 		print(num)
# 	num+=1


###############################################
# sum=0
# num=12
# while num<=421:
# 	sum=sum+num
# 	print(num)
# 	num+=1
# print(sum)


###############################################################3
# sum=0
# num=30
# while num<=420:
# 	if num%8==0:
# 		print(num)
# 		sum=sum+num
# 	num+=1
# print(sum)

#######################################


# sum=0
# num=1
# while num<=48:
# 	print(num)
# 	sum=sum+num
# 	num+=1
# print(sum)
#####################################
# sum=0
# a=1
# while a<=11:
# 	b=int(input())
# 	sum=sum+b
# 	a+=1
# print(sum)
# if sum%5==0:
# 	print("5 k multiple h")
# else:
# 	print("nhi hai")

#################################################33


# a=1
# while a<=100:
# 	if a%2==0:
# 		print(a)
# 	else:
# 		print(-a)
# 	a+=1

##############################################

##guessing game

# num=5
# a=1
# while a<=6:
# 	b=int(input("1 se 10 k beech m no. guess kro:"))
# 	if b==num:
# 		print("congratulation")
# 		break
# 	a+=1
# if a==7:
# 	print("users ne koi no. guess nhi kra")

##############################################################3      guessing game    


# num=5
# a=1
# while a<=10:
# 	b=int(input("1 se 10 k beech m no. guess kro:"))
# 	if b<num:
# 		print("aapka number chhota he ")
# 	elif b>num:
# 		print("aapka number bda he")
# 	else:
# 		print("aap game jeet gye")
# 		print("congratulation")
# 		break
# 	a+=1
# if a==11:
# 	print("users ne koi no. guess nhi kra")s

# ###########################################
                                                   #bina multiple kiye bina multiple krna 

# g=0
# c=0
# a=int(input())
# b=int(input())
# while c<a:
# 	g=g+b
# 	c=c+1
# print(g)


################################################################

# c = 0
# d = 1

# while c < 3:
#     c = c + 1
#     d = d * c
#     print("Loop Ke Andar", c, d)
# else:
#     print ("Loop Ke Bahar", c, d )



#############################################################

# n = 6
# s = 0
# i = 1

# while i <= n:
#     s = s + i
#     i = i + 1

# print(s)


####################################################3           prime number 
# num=int(input())
# i = 2
# while (i<num):
#     if (num%i == 0):
#         print(num, 'is not a prime number')
#         break
#     i = i + 1
# else:
#    	print(num, 'is a prime number')

########################################################

# n=int(input())
# count = 0
# i=1
# while (i<=n):
# 	if (n%i==0):
# 		count=count+1
# 	i=i+1
# if (count==2):
# 	print("prime number")
# else:
# 	print("not number")

############################################333

# i = 0
# while(i<5):
#     j = 0
#     while(j<5): #loop2
#         if (j > 3): 
#             break 
#         else:
#             print ("*") 
#         j = j + 1    
#     print ('')
#     i = i + 1
 


##########################################################          bugs   




# x = 0
# while(x<7):
#     if (x == 3 or x==5):
#         x = x + 1
#         continue
#     print(x)
#     x = x + 1 


#########################################################

# index = 1
# while(index < 10):
# 	print(index)
# 	index = index + 1


##################################################

# sum=0
# i = 1
# while(i <= 140):
#     if(i % 3 == 0):
#     	sum = sum + i
#     i = i + 1
# print(sum) 


##########################################################

# i=0
# while(i<10):
# 	j = 0
# 	while(j<=5):
# 		print(j)
# 		j = j + 1
# 	i = i + 1
 



############################################################      positive negetive number    
# i = 0
# num = int(input("Enter your number:- "))
# while(i <= num):
#     if(num >0):
#         print(num," is positive")
#         break
#     elif(num<0):
#     	print(num,"is negetive")
#     else :
#         print(num,"zero")
#     i = i + 1
# if num<0:
# 	print("negetive")

#  ###############################################################      lenth nikalna



# num= int(input())
# count=0
# while num!=0:
# 	num//=10
# 	count+=1
# print("total digit are",count)


#####################################################################

#                                                                            # fibonacci  
# n=int(input())
# x=0
# y=1
# z=0
# while z<=n:
# 	print(z)
# 	x=y
# 	y=z
# 	z=x+y



######################################################################



# num=int(input())
# if(num==2 or num ==3):
# 	print("prime number")
# elif (num%2==0 or num%3==0 or num%5==0):
# 	print("not prime number")
# else:
# 	print("prime")
#######################
#
#################################################################################


# print("wel-come to punjab nation bank ")
# pin=input("enter your correct four digit password:")
# balance=10000
# if len(pin)==4:
# 	print("correct password")
# 	b=1
# 	while b==1:
# 		choice=int(input('''please choose an option: 
# 			1-withdraw,
# 			2-deposit,
# 			3-check balance, 
# 			4-exit:'''))
# 		if choice==1:
# 			withdraw=float(input('''select your amount:-
# 				1 withdraw 500,
# 				2 withdraw 1000,
# 				3 withdraw 1500,
# 				4 withdraw 2000,or
# 				(enter your amount)'''))
# 			if withdraw==1:
# 				balance=balance-500
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 			elif withdraw==2:
# 				balance=balance-1000
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 			elif withdraw==3:
# 				balance=balance-1500
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 			elif withdraw==4:
# 				balance=balance-2000
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 			else:
# 				balance=balance-withdraw
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 		elif choice==2:
# 			deposit=float(input('''select your amount:-
# 				1 deposit 500,
# 				2 deposit 1000,
# 				3 deposit 1500,
# 				4 deposit 2000,or
# 				(enter your amount)'''))
# 			if deposit==1:
# 				balance=balance+500
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 			elif deposit==2:
# 				balance=balance+1000
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 			elif deposit==3:
# 				balance=balance+1500
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 			elif deposit==4:
# 				balance=balance+2000
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 			else:
# 				balance=balance+deposit
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 		elif choice==3:
# 			print(balance)
# 		elif choice==4:
# 			print("good bye")
# 			break
# 		print("do you use the atm press y/n ")
# 		c=input()
# 		if c=="y":
# 			print("SWIPE THE CARD")
# 		else:
# 			print("good bye")
# 			break
# else:
# 	print("wrong password")









########################################################################################################

# print("wel-come to punjab nation bank ")
# pin=input("enter your correct four digit password:")
# balance=10000
# if len(pin)==4:
# 	print("correct password")
# 	b=1
# 	while b==1:
# 		choice=int(input('''please choose an option: 
# 			1-withdraw,
# 			2-deposit,
# 			3-check balance, 
# 			4-exit:'''))
# 		if choice==1:
# 			withdraw=float(input('''select your amount:-
# 				1 withdraw 500,
# 				2 withdraw 1000,
# 				3 withdraw 1500,
# 				4 withdraw 2000,or
# 				(enter your amount)'''))
# 			if withdraw==1:
# 				balance=balance-500
# 				print("successfull withdraw 500 ")
# 				print("current balance:$",balance)
# 			elif withdraw==2:
# 				balance=balance-1000
# 				print("successfull withdraw 1000 ")
# 				print("current balance:$",balance)
# 			elif withdraw==3:
# 				balance=balance-1500
# 				print("successfull withdraw 1500 ")
# 				print("current balance:$",balance)
# 			elif withdraw==4:
# 				balance=balance-2000
# 				print("successfull withdraw 2000 ")
# 				print("current balance:$",balance)
# 			else:
# 				balance=balance-withdraw
# 				print("successfull withdraw",withdraw)
# 				print("current balance:$",balance)
# 		elif choice==2:
# 			deposit=float(input('''select your amount:-
# 				1 deposit 500,
# 				2 deposit 1000,
# 				3 deposit 1500,
# 				4 deposit 2000,or
# 				(enter your amount)'''))
# 			if deposit==1:
# 				balance=balance+500
# 				print("successfull deposit 500")
# 				print("current balance:$",balance)
# 			elif deposit==2:
# 				balance=balance+1000
# 				print("successfull deposit 1000 ")
# 				print("current balance:$",balance)
# 			elif deposit==3:
# 				balance=balance+1500
# 				print("successfull deposit 1500 ")
# 				print("current balance:$",balance)
# 			elif deposit==4:
# 				balance=balance+2000
# 				print("successfull deposit 2000 ")
# 				print("current balance:$",balance)
# 			else:
# 				balance=balance+deposit
# 				print("successfull deposit",deposit)
# 				print("current balance:$",balance)
# 		elif choice==3:
# 			print(balance)
# 		elif choice==4:
# 			print("good bye")
# 			break
# 		print("do you use the atm press y/n ")
# 		c=input()
# 		if c=="y":
# 			print("SWIPE THE CARD")
# 		else:
# 			print("good bye")
# 			break
# else:
# 	print("wrong password")



#num=[17,59,18,19,20,1,2,4,56,76,7,5,46,36,56,89,98,8,890,8,9]
#prime=[]
#even=[]
#odd=[]
#for i in range(2,len(num)):
#    if num[i]>1 and i in num:
#        for j in range(2,i):
#            if i%j==0:
#                break
#        else:
#            prime.append(i)
#for i in num:
#    if i%2==0:
#        even.append(i)
#    else:
#        odd.append(i)
#print(prime)
#print(even)
#print(odd)
#
#
##############################################################

#num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
#prime=[]
#odd=[]
#even=[]
#a=1
#while a<len(num):
#    if num[a]%2==0:
#        even.append(num[a])
#    else:
#        odd.append(num[a])
#        if num[a]>1:
#            if(num[a]%3!=0 and num[a]%5!=0 and num[a]%7!=0):
#                prime.append(num[a])
#    if num[a]==2 or num[a]==3 or num[a]==5 or num[a]==7:
#        prime.append(num[a])
#
#        
#    a+=1
#    
#print(prime,"prime")
#print(odd,"odd")
#print(even,"even")
####################################################################################################

#num=[45,67,89,1,2,
#3,4,5,6,7,8,9,10,11,12,45,7,9,89,55,13,14,15,16,17,18,19,20]
#prime=[]
#odd=[]
#even=[]
#a=1
#while a<len(num):
#    if num[a]%2==0:
#        even.append(num[a])
#    else:
#        odd.append(num[a])
#    a+=1
#for i in num:
#    for j in range(2,i):
#        if i%j==0:
#            break
#    else:
#        if i==1:
#            continue
#        prime.append(i)    
#print(prime,"prime")
#print(odd,"odd")
#print(even,"even")
#############################################################  maxxxx     maxxxxx  


#a=[1,105,90,7,6,54,100,2,3,4,5,95,6]
#d=a[0]
#for i in a:
#    if i>d:
#        d=i
#print(d)
############################################################  MINIMUM  #############

#a=[1,105,90,7,6,54,100,2,3,4,5,95,6]
#d=a[0]
#for i in a:
#    if i<d:
#        d=i
#print(d)






####################################################  second max    ############3
#num=[200,10,80,90,105,10000,7,6,1000,500,54,100,2,3,4,5,95,6]
#total=num[2:]
#if num[0]>num[1]:
#    s=num[0]
#    s1=num[1]
#else:
#    s=num[1]
#    s1=num[0]
#for i in total:
#    if i>s1:
#        if i>s:
#            s1=s
#            s=i
#        else:
#            s1=i
#print(s1)
#    
#




#############################################  second max    ############3
#num=[200,10,80,90,105,10000,7,6,1000,500,54,100,2,3,4,5,95,6]
#total=num[2:]
#if num[0]>num[1]:
#    s=num[0]
#    s1=num[1]
#else:
#    s=num[1]
#    s1=num[0]
#for i in total:
#    if i>s1:
#        if i>s:
#            s1=s
#            s=i
#        else:
#            s1=i
#print(s1)
#    
###############################################################odddd    eveeen   prrimeeee


# num=[45,67,89,1,2,3,4,5,6,7,8,9,10,11,12,45,7,9,289,89,55,13,14,15,16,17,18,19,20]
# prime=[]
# odd=[]
# even=[]
# a=1
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         if i==1:
#             continue
#         prime.append(i)          
# print(prime,"prime")
# print(odd,"odd")
# print(even,"even")

###################################################################################


# number=[54,21,65,48,65]
# b=0
# for i in number:
#     b=b+1
# print(b)


# num=[56,25,36,48,87,54]
# b=0
# for i in num:
#     if i>20 and i<40:
#         b=b+1
#         print(i)
# print(b)




# num=[25,65,41,70,23,56]
# num.sort()
# print(num[-1])


# num=[25,65,41,70,23,56]
# num=max(num)
# print(num)


# num=[45,5,6,8,66,92,5,54]
# num.sort()
# print(num[-2])


###########################################################################

# a=0
# i=10
# while i>0:
#     print("enter numbeer")
#     b=int(input())
#     a=a+b
#     i=i-1
# print("average is",a/1)

#######################################################333    reverse     reverse  


#pl=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
#a=1
#rev_rse=[]
#for i in(pl):
#    rev_rse.append(pl[-a])
#    a+=1
#print(rev_rse)
################################################################    palindrome   


#x=["n","subh","i","t","i","hh","n"]
#y=[]
#a=1
#for i in x:
#    if x[-a]==i:
#        y.append(x[-a])
#    a+=1
#if x==y:
#    print("palindrome")
#else:
#    print("not palindrome")        
#####################################################################
# x=["n","k","t","i","n"]
#y=[]
# for i in range(len(x)):
#     if x[i]==x[-i-1]:
#         y.append(x[i])
# if x==y:
#     print('this is palindrome')
# else:
#     print('this is not a palindrome')

##########################################################################

#x=["n","k","t","i","n"]
#y=[]
#a=0
#while a<len(x):
#    if x[a]==x[-a-1]:
#        y.append(x[a])
#    a+=1
#if x==y:
#    print(" this is palindrome")
#else:
#    print("this is not palindrome")
#

###############################################################################################3  STRONG  PASSWORD 


#pas=input("enter password")
#if len(pas)>8 and len(pas)<16:
#    if ("A"in pas or"B" in pas or"C" in pas or"D" in pas or"E"in pas or"F" in pas or"H" in pas or "I"in pas  or "J"in pas or "K"in pas or "L"in pas or "M"in pas or "N"in pas or "O"in pas or "P"in pas or "Q"in pas or "R"in pas or "S"in pas or "T"in pas or "U"in pas or "V"in pas or "W"in pas or "X"in pas or "Y"in pas  or "Z"in pas):
#        if ("a"in pas or"b"in pas or"c"in pas or"d"in pas or"e"in pas or"f"in pas or "g"in pas or"h"in pas or"i"in pas or"j"in pas or"k"in pas or"l"in pas or"m"in pas or"n"in pas or"o"in pas or"p"in pas or"q"in pas or"r"in pas or"s"in pas or"t"in pas or"u"in pas or"v"in pas or"w"in pas in pas or"x"in pas or"y"in pas or"z"in pas):
#            if "@"in pas  or "#"in pas or "$"in pas  or "!"in pas:
#                if ("1"in pas  or "2"in pas  or "3"in pas  or "4"in pas  or "5"in pas  or "6"in pas  or "7"in pas  or "8"in pas or"9"in pas or"0"in pas):
#                    print("correct password")
#                else:
#                    print("enter number")
#            else:
#                print("not special character")
#        else:
#            print("small")           
#    else:
#        print("capital")
#else:
#    print("enter 8 to 16 character")
#
##############################################################################  list compare 


#list1 = [1,2,3,4,5,6]
#list2 = [2,3,1,0,6,7] 
#a=0
#for i in list1:
#    if i in list2:
#        continue
#    else:
#        print(i)
#
#
###################################################################   hangman game @##################



#hangman=1,2,3,4,5,6,7
#print("wel-come")
#name=input("what is yourname")
#print("hello,"+name,"time to lay hangman")
#word=["subhash","abhishek","pawan","tushar","ajay","atul","sanjay"]
#guesses=("")
#while True:
#    a=1
#    t=7
#    while t>0:
#        b=0
#        for i in word:
#            if i in guesses:
#                print(i)
#            else:
#                print("________")
#                b=+1
#        if b==0:
#            print("you won")
#            break
#        guess=input("guess the character")
#        guesses+=guess
#        if guess not in word:
#            t-=1
#            print(hangman[-a])
#            a+=1
#            print("you have",+t,"more guess")
#            if t==0:
#                print("you are lose")
#    print("do you want play: y/n")
#    again=input()
#    if again=="y":
#        print("thank you")
#        guesses="0"
#        
#    else:
#        print("good bye")
#        break   
########################################################


#hangman= ['''
#  +---+
#  |   |
#      |
#      |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
#      |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
#  |   |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
# /|   |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
# /|\  |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
# /|\  |
# /    |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
# /|\  |
# / \  |
#      |
#=========''']
#print("wel-come")
#name=input("what is yourname\n")
#print("hello,"+name,"time to lay hangman")
#word=["subhash","abhishek","pawan","navid","ajay","atul","sanjay"]
#guesses=("")
#while True:
#    a=1
#    t=7
#    while t>0:
#        b=0
#        for i in word:
#            if i in guesses:
#                print(i)
#            else:
#                print("________")
#                b=+1
#        if b==0:
#            print("you won")
#            break
#        guess=input("guess the character\n")
#        if guess in guesses:
#            print("already use this word")
#        guesses+=guess
#        if guess not in word:
#            t-=1
#            print(hangman[-a])
#            a+=1
#            print("you have",+t,"more guess")
#            print("do you help me: yes/no")
#            help=input()
#            if help=="yes":
#                for i in range(1):
#                    print("(1st chance press : 1), (2nd chance press: 2) and (3rd chance press: 3)")
#                    helpp=input("you have 3 chance")
#                    if helpp=="1":
#                        print("*ajay*")
#                    elif helpp=="2":
#                        print("*pawan*")
#                    elif helpp=="3":
#                        print("*abhishek*")
#            elif help== "no":
#                print("ok")
#            
#                
#            if t==0:
#                print("you are lose")
#    print("do you want play: y/n")
#    again=input()
#    if again=="y":
#        print("thank you")
#        guesses="0"
#        
#    else:
#        print("good bye")
#        break   
#

































































































