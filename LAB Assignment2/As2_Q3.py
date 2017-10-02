
class hotel(object): #superclass
    """ Class for Hotel Reservation system

    Attributes
        Guest information - name, address, phone,
        Room information - Room number, room type, price
    Methods - different fuctions(as classes and def) performed on the attributes are
        Hotel
            login
            person details
            available rooms
        Reservevation
            make reservation
            pay amount
        Check In room
        In house list
        Check Out Room
        Employee list
            Enter employees' details
            Print emoployees' details
    """

    UserName = "Hotel"
    Password = "HappyStay"
    Double = {"101":"st","103":"st","105":"st","107":"st"}
    Queen = {"102":"st","104":"st","106":"st","108":"st"}
    King = {"109": "st", "110": "st", "111": "st", "112": "st"}
    rooms = {"Double":Double,"Queen":Queen,"King":King}
    rooms2 = {"101":["","",""], '102':["","",""],'103':["","",""],"104":["","",""],"105":["","",""],
              '106':["","",""],'107':["","",""],"108":["","",""],"109":["","",""], '110':["","",""],
              '111':["","",""],"112":["","",""],}
    room_payment = {"101": "", '102': "", '103': '', "104": "", "105": "", '106': "",
              '107': '', "108": "", "109": "", '110': "", '111': '', "112": "", }
    prices = {"Double":"$120","King":"$100","Queen":"$80"}
    #rooms[][][]
    def __init__(self):
        pass

    def login(self):
        self.usr = input("enter username:")
        self.pwd = input("enter password")
        while self.usr != hotel.UserName or self.pwd != hotel.Password:
            print("\t Incorrect Username or Password")
            self.usr = input("enter username:")
            self.pwd = input("enter password")

    def person_details(self):
        self.name = str(input("Enter Name"))
        self.address = str(input("Enter Address"))
        self.phone = str(input("Enter Phone Number"))
        self.p_details = [self.name, self.address, self.phone]
    def available_rooms(self):
        nv = 0
        nvr = 0
        print("Available Rooms are:")
        for k in hotel.rooms:
            print(k,end='\t')
            for key in hotel.rooms[k]:
                if hotel.rooms[k][key] != "Occupied":
                    print(key,end='\t')
                    nv = 1
                if nv != 1:
                    print("no vacancy")
            print()


class reservation(hotel):  # subclass(inheritance)

    def __init__(self):
        hotel.__init__(self)
        self.available_rooms()
        self.make_reservation()
        self.pay_amount()
    def make_reservation(self):
        nvr = 0
        for k in hotel.rooms:
            for key in hotel.rooms[k]:
                if hotel.rooms[k][key] == "Occupied":
                    nvr += 1
        if nvr == 12:
            print("Sory No Rooms available this time")
        else:
            self.person_details()
            print("Select Room Type(eneter 1/2/3)")
            print("1.Double  2.King 3.Queen")
            n = int(input())
            while n not in (1, 2, 3):
                print("incorrect selection")
                print("Select Room Type(eneter 1/2/3)")
                print("1.Double  2.King 3.Queen")
                n = int(input)
            if n == 1:
                self.roomtype = "Double"
            elif n == 2:
                self.roomtype = "King"
            elif n == 3:
                self.roomtype = "Queen"
            self.roomselect = str(input("Enter the room number"))
            if hotel.rooms[self.roomtype][self.roomselect] != "Occupied" or "Reserved":
                hotel.rooms[self.roomtype][self.roomselect] = "Reserved"
            else: print("Sorry"+self.roomselect+" is"+ hotel.rooms[self.roomtype][self.roomselect], "select another room ")
            hotel.rooms2[self.roomselect]= self.p_details
    def pay_amount(self):
        print("Your Price is "+hotel.prices[self.roomtype])
        self.money = str("$"+input("Enter Transaction Amount: "))
        while self.money != hotel.prices[self.roomtype]:
            print("Pay full amount")
            print("Your Price is " + hotel.prices[self.roomtype])
            self.money = str("$" + input("Enter Transaction Amount: "))
        hotel.room_payment[self.roomselect] = "paid"
        print(self.name + ", you have reserved a " + self.roomtype + " Room " + self.roomselect)
        print(" \t You can Check-In \n \t Thank You!!")


class checkin(hotel):

    def __init__(self):
        hotel.__init__(self)
        self.roomselect = str(input("Enter the room the checkin room"))
        self.person = str(input("Enter the guest name"))
        self.check_in()
    def check_in(self):
        roomtype = ""
        if self.person != hotel.rooms2[self.roomselect][0]:
                print("Incorrect Guest Name")
        else:
            if self.roomselect in ("101","103","105","107"):
                roomtype = "Double"
            elif self.roomselect in ("102","104","106","108"):
                roomtype = "Queen"
            elif self.roomselect in ("109","110","111","112"):
                roomtype = "King"
            if  hotel.rooms [roomtype][self.roomselect] == "Reserved":
                hotel.rooms[roomtype][self.roomselect] = "Occupied"
                print(self.person+" checkedin the room"+self.roomselect)
            elif hotel.rooms [roomtype][self.roomselect] == "st":
                print(self.roomselect+" Room is not reserved")
            elif hotel.rooms[type][self.roomselect] == "Occupied":
                print(self.roomselect+ " Room is already occupied")

class inhouse_list(hotel):
    def __init__(self):
        hotel.__init__(self)
        print("Name \t\t Address \t\t Phone")
        for key in hotel.rooms2:
            if hotel.rooms2[key] == ["","",""]:
                print(key+ "  -  "+"\t\t No Guest")
            else:
                print(key, "  -  "+ hotel.rooms2[key][0]+" - "+hotel.rooms2[key][1]+" - "+hotel.rooms2[key][2])

class employee_list(hotel):

    def __init__(self):
        hotel.__init__(self)
        self.emoployees = []
        self.n = 0
        self.enter_employeelist()
        self.print_employees_details()
    def enter_employeelist(self):
        self.n = int(input("Enter number of employees"))
        for x in range (0,self.n):
            self.person_details()
            self.emoployees.append(self.p_details)
    def print_employees_details(self):
        print()
        print("*****Hotel Employees' List*****")
        print()
        print("name \t\t Address \t\t phone")
        for x in range (0,self.n):
            for y in range (0,3):
                print(self.emoployees[x][y],end="\t\t")
            print()

class checkout(hotel):

    def __init__(self):
        hotel.__init__(self)
        self.roomselect = str(input("Enter the checkout Room :"))
        self.check_out()

    def check_out(self):
        roomtype = ""
        if self.roomselect in ("101", "103", "105", "107"):
            roomtype = "Double"
        elif self.roomselect in ("102", "104", "106", "108"):
            roomtype = "Queen"
        elif self.roomselect in ("109", "110", "111", "112"):
            roomtype = "King"
        if hotel.rooms[roomtype][self.roomselect] == "Occupied":
            hotel.rooms[roomtype][self.roomselect] = "st"
            print(hotel.rooms2[self.roomselect][0], end ="")
            print(" Checked out from room ", end = "")
            print(self.roomselect)
            print("***Thank you for the stay")
            hotel.rooms2[self.roomselect] = ["","",""]
        elif hotel.rooms[roomtype][self.roomselect] == "Reserved" or "st":
            print(self.roomselect + " is vacant")




# main program

def hoteltask():
    f = hotel()
    f.login()

    def select_task():
        print("Press a number to select the Task")
        print("1.Available Rooms 2.Reservation 3.Chenk-In 4.CheckOut  5.InhouseList 6.Employees 7.Exit")
        option = int(input())
        return option
    option = select_task()
    #all classes and fucntions are instantiated below
    while option != 7:
        while option not in (1,2,3,4,5,6,7):
            print("Please enter valid number")
            option = int(input())
        if option == 1:
            f.available_rooms()
            print("==" * 40)
            print()
            option = select_task()
        elif option == 2:
            reservation()
            print("=="*40)
            print()
            option = select_task()
        elif option == 3:
            checkin()
            print("==" * 40)
            print()
            option = select_task()
        elif option == 4:
            checkout()
            print("==" * 40)
            print()
            option = select_task()
        elif option == 5:
            inhouse_list()
            print("==" * 40)
            print()
            option = select_task()
        elif option == 6:
            employee_list()
            print("==" * 40)
            print()
            option = select_task()
    print("Exit")


hoteltask()
#
