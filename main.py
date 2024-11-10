avail_activa = 20
charge=500
database={}
security_code= "qwe123"
return_activa= 0
def Terms_cond():
   tc= (f"""
    1.Aadhaar Card is Mandatory.
    2.Driving Licence is Mandatory.
    3.One Activa for One Day: {charge}:""")
   return tc

def print_bill(*data):
    info=f"""
Welcome to Cyber Success Activa Rental House
*******************************************************   
T&C:  
1. Aadhaar Card is Mandatory. 
2. Driving Licence is Mandatory. 
3. One Activa for One Day:{charge}:

********************************************************
   name:{data[0]}
   phone_no:{data[1]}
   address:{data[2]}
   Adhar:{data[3]}
   Lic: {data[4]}
   rent_no_activa: {data[5]}
   no_days :{data[6]}
   *************************************
   bill :{data[7]}
   Thanku you"""

    file_name={data[0]+"Documents.txt"}
    p = open(file_name,"w")
    p.write(info)
    p.close()



def rent_database_entry(*data):
    global avail_activa
    if data[3] not in database:
        database[data[3]]= {"name": data[0],"phone_no":data[1],"address":data[2],
                            "Adhar":data[3],"lic":data[4],"rent_on_activa":data[5],
                            "no_days":data[6],"bill":data[7],"Status":"pending"}
        avail_activa -= data[5]
    else:
        database[data[3]]["rent_no_activa"] +=[data[5]]
        database[data[3]]["no_days"] += [data[6]]
        database[data[3]]["bill"] +=[data[7]]
        avail_activa -= data[5]
def rent_user_info(rent_no_activa):
    global var
    name=input("Enter your name :")
    phone_no=input("Enter your no :")
    address=input("enter your address :")
    Adhar=input("enter your adhar no :")
    lic=input("enter your driving lic :")
    no_days=int(input("Enter no of days"))
    bill=rent_no_activa*no_days*charge
    print("your bill ",bill)
    conform=input("Conform (Y/N): ")
    if conform == "Y":
        print("Succesfuly book")
        print_bill(name,phone_no,address,Adhar,lic,rent_no_activa,no_days,bill)
        rent_database_entry(name,phone_no,address,Adhar,lic,rent_no_activa,no_days,bill)

print("Welcome to cyber success Activa rental house")

def Adhar (return_activa):
   Adhar=input("enter a adhar no :")

   if Adhar in database:
      print("enter no of car return: ")
      if return_activa <= rent_no_activa:
           rent_user_info(rent_no_activa)
      else:
           print("Succesfuly return ")
   else:
         print("adhar not found :")

while True:
    print("NO of activa Available :", avail_activa)
    var= input("""
    1 . Rent
    2 . Return
    3 . Owner
    4 .Exit  : """)

    if var =="1":
        print("Welcome to rent :")
        print(Terms_cond())
        conform=input("Conform (Y/N):")
        if conform =="Y":
            rent_no_activa=int(input("Enter no of activa :"))
            if rent_no_activa <=avail_activa:
                rent_user_info(rent_no_activa)
            else:
                  print("not available")

        else:
            print("Thank you")

    elif var == "2":
        print("Welcome to Return ")
        Adhar(return_activa)


    elif var =="3":
        code=input("enter a security code :")

        if code == security_code:
            name=input("enter your name:")
            phone_no = input("Enter your no :")
            address = input("enter your address :")
            Adhar = input("enter your adhar no :")
            lic = input("enter your driving lic :")
            no_days = int(input("Enter no of days"))
            status="pending"
        else:
            print("wrong security code :")

    elif var == "4":
        print("Thank you for visiting  -------------")










