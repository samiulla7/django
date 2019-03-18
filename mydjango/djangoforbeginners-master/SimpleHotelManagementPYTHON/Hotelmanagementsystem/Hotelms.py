from prettytable import PrettyTable

class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):

        print("\n\n**********************************")
        print("*****WELCOME TO HEWING HOTEL******")
        print("**********************************\n")
        
        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")
        
    def roomrent(self):#sel1353

        print("\n\n**********************************")
        print("*************ROOM RENT************")
        print("**********************************\n")

        print ("We have the following rooms for you:-\n")
        x = PrettyTable()
        x.field_names = ["Sr no.", "Type", "Price"]
        x.add_row([1,'A', 'Rs. 6000/-'])
        x.add_row([2,'B', 'Rs. 5000/-'])
        x.add_row([3,'C', 'Rs. 4000/-'])
        x.add_row([4,'D', 'Rs. 3000/-'])
        print(x)
        
        x=int(input("Enter Your Choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("you have opted room type A")

            self.s=6000*n

        elif (x==2):

            print ("you have opted room type B")

            self.s=5000*n

        elif (x==3):

            print ("you have opted room type C")

            self.s=4000*n

        elif (x==4):
            print ("you have opted room type D")

            self.s=3000*n

        else:

            print ("please choose a room")

        print ("your room rent is =",self.s,"\n")

    def restaurentbill(self):
        print("\n\n**********************************")
        print("*************RESTAURANT MENU******")
        print("**********************************\n")
        x = PrettyTable()
        x.field_names = ["Sr no.", "Item", "Price"]
        x.add_row([1,'Water', 'Rs. 20/-'])
        x.add_row([2,'Tea', 'Rs. 10/-'])
        x.add_row([3,'Break fast combo', 'Rs. 90/-'])
        x.add_row([4,'Lunch', 'Rs. 110/-'])
        x.add_row([5,'Dinner', 'Rs. 150/-'])
        x.add_row([6,'Exit',''])
        print(x)

        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+20*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+10*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d

            elif (c==6):
                break;
            else:
                print("Invalid option")

        print ("Total food Cost=Rs",self.r,"\n")

    def	laundrybill(self):
        print("\n\n**********************************")
        print("*************LAUNDRY MENU*********")
        print("**********************************\n")

        x = PrettyTable()
        x.field_names = ["Sr no.", "Item", "Price"]
        x.add_row([1,'Shorts', 'Rs. 3/-'])
        x.add_row([2,'Trousers', 'Rs. 4/-'])
        x.add_row([3,'Shirt', 'Rs. 5/-'])
        x.add_row([4,'Jeans', 'Rs. 6/-'])
        x.add_row([5,'Girlsuit', 'Rs. 8/-'])
        x.add_row([6,'Exit',''])
        print(x)

        while (1):
            #brought to you by code-projects.org

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f
            elif (e==6):
                break;
            else:

                print ("Invalid option")


        print ("Total Laundary Cost=Rs",self.t,"\n")

    def gamebill(self):
        print("\n\n**********************************")
        print("*************GAME MENU************")
        print("**********************************\n")
        
        x = PrettyTable()
        x.field_names = ["Sr no.", "Item", "Price"]
        x.add_row([1,'Table tennis', 'Rs. 60/-'])
        x.add_row([2,'Bowling', 'Rs. 80/-'])
        x.add_row([3,'Snooker', 'Rs. 70/-'])
        x.add_row([4,'Video games', 'Rs. 90/-'])
        x.add_row([5,'Pool', 'Rs. 50/-'])
        x.add_row([6,'Exit',''])
        print(x)

        
        while (1):

            
            g=int(input("Enter your choice:"))


            if (g==1):
                h=int(input("No. of hours:"))
                self.p=self.p+60*h

            elif (g==2):
                h=int(input("No. of hours:"))
                self.p=self.p+80*h

            elif (g==3):
                h=int(input("No. of hours:"))
                self.p=self.p+70*h

            elif (g==4):
                h=int(input("No. of hours:"))
                self.p=self.p+90*h

            elif (g==5):
                h=int(input("No. of hours:"))
                self.p=self.p+50*h
            elif (g==6):
                break;

            else:

                print ("Invalid option")



        print ("Total Game Bill=Rs",self.p,"\n")

    def display(self):
        print("\n\n**********************************")
        print("*************HOTEL BILL************")
        print("**********************************\n")

        x = PrettyTable()
        # x.get_string(title="Australian cities")
        x.field_names = ['Sr no.', 'Name', 'Value']
        x.add_row([1,"Customer name:",self.name])
        x.add_row([2,"Customer address:",self.address])
        x.add_row([3,"Check in date:",self.cindate])
        x.add_row([4,"Check out date",self.coutdate])
        x.add_row([5,"Room no.",self.rno])
        x.add_row([6,"Your Room rent is:",self.s])
        x.add_row([7,"Your Food bill is:",self.r])
        x.add_row([8,"Your laundary bill is:",self.t])
        x.add_row([9,"Your Game bill is:",self.p])

        self.rt=self.s+self.t+self.p+self.r

        x.add_row([10,"Your sub total bill is:",self.rt])
        x.add_row([11,"Additional Service Charges is",self.a])
        x.add_row([12,"Your grandtotal bill is:",self.rt+self.a])
        print(x)
        print("\n")
        self.rno+=1

        

def main():

    a=hotelfarecal()
    

    while (1):
        x = PrettyTable()
        x.field_names = ["Sr no.", "Action"]
        x.add_row([1, "Enter Customer Data"])
        x.add_row([2, "Calculate rommrent"])
        x.add_row([3, "Calculate restaurant bill"])
        x.add_row([4, "Calculate laundry bill"])
        x.add_row([5, "Calculate gamebill"])
        x.add_row([6, "Show total cost"])
        x.add_row([7, "EXIT"])
        print(x)

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()

        if (b==7):

            quit()



main()

