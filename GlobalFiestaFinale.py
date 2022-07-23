import pickle
import random

userdatas = {}
user = {}
akeys = ["qwert","asdfg","zxcvb"]
movie = {"cast":{},"director":"","genre":[],"box":"int","storyline":"","year":"int","ratings":"Not rated Yet"}
rat = {}
moviedatas = {}

try:
    udata = open("users.dat","rb")
    userdatas = pickle.load(udata)
except EOFError:
    pass
except FileNotFoundError:
    udata = open("users.dat","wb")

udata.close()

try:
    mdata = open("movies.dat","rb")
    moviedatas = pickle.load(mdata)
except EOFError:
    pass
except FileNotFoundError:
    mdata = open("movies.dat","wb")

mdata.close()

def adminmenu():
    while True:
        print("Admin Menu\n[1]Add Film\n[2]Edit Film Details\n[3]Delete Film\n[4]Search Film Details\n[5]Display All Film Details\n[6]Rate\n[7]Log Out")
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            insert()
        elif ch == 2:
            edit()
        elif ch == 3:
            delete()
        elif ch == 4:
            search()
        elif ch == 5:
            display_all()
        elif ch == 6:
            rating()
        elif ch == 7:
            print("Logout Successful....")
            break;
        else:
            print("Enter Valid Choices only....")

def usermenu():
    while True:
        print("User Menu\n[1]Search Film Details\n[2]View All Film Details\n[3]Rate Your Favourite Film\n[4]Log Out")
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            search()
        elif ch == 2:
            display_all()
        elif ch == 3:
            rating()
        elif ch == 4:
            print("Logout Successful....")
            break;

def mainmenu():
    print("MAIN MENU\n[1]Login\n[2]Sign Up\n[3]Exit")
    choice = int(input("Enter Your Choice : "))
    return choice

def signup():
    while True:
        nname = input("Enter Username : ")
        if nname not in userdatas:
            break;
        else:
            print("The username is already taken choose another....")
    npass = input("Enter Password : ")
    while True:
        akey = input("Enter Admin key(if you dont have leave it blank) :")
        if akey in akeys:
            user["pass"] = npass
            user["admin"] = True
            user["ratings"] = []
            userdatas[nname] = user.copy()
            break;
        elif akey == "" or akey.isspace():
            user["pass"] = npass
            user["admin"] = False
            user["ratings"] = []
            userdatas[nname] = user.copy()
            break;
        else:
            print("wrong admin key....")
    udata = open("users.dat","wb")
    pickle.dump(userdatas,udata)
    udata.close()
    print("Sign Up successful")




def insert():
    mname = input("Enter The Movie Name : ")
    director = input("Enter director name : ")
    ge = []
    g = int(input("enter how many genres :"))
    for i in range(g):
        inp = input("Enter The Genre : ").title()
        ge.append(inp.lower()) 
    cast = {}
    c = int(input("Enter How Many persons on top cast : "))
    for i in range(c):
        inp2 = input("Enter the name of the person : ").title()
        cast[inp2] = input("Enter The roll in the movie : ").title()
    movie["genre"] = ge
    movie["cast"] = cast
    movie["director"] = director.title()
    movie["storyline"] = input("Enter The Storyline : ")
    movie["box"] = int(input("Enter The Box Office Collection : "))
    while True:
        yr = int(input("Enter The Year Of release : "))
        if yr>=1900 and yr<=2022:
            break;
        else:
            print("Enter Valid Date...")
    movie["year"] = yr
    movie["ratings"] = "Not Rated Yet"
    moviedatas[mname.lower()] = movie
    mdata= open("movies.dat","wb")
    pickle.dump(moviedatas,mdata)
    mdata.close()

def search():
    while True:
        print("Search\n[1]Movie Name\n[2]Genre\n[3]Year\n[4]Director\n[5]Ratings\n[6]Exit")
        sc = int(input("Enter at which type do you want to search : "))
        if sc == 1:
            ch = input("Enter Movie Name : ")
            if ch.lower() in moviedatas:
                display(ch)
            else:
                print("Movie not found.....")
                    
        elif sc == 2:
            ch = input("Enter Genre : ")
            found = False
            for i in moviedatas:
                if ch.lower() in moviedatas[i]["genre"]:
                    found = True
                    display(i)
            if found == False:
                print("No results found....")
        elif sc == 3:
            ch = int(input("Enter The Year : "))
            found = False
            for i in moviedatas:
                if moviedatas[i]["year"] == ch:
                    found = True
                    display(i)
            if found == False:
                print("No results found....")
        elif sc == 4:
            ch = input("Enter Director : ")
            found = False
            for i in moviedatas:
                if moviedatas[i]["director"] == ch:
                    found = True
                    display(i)
            if found == False:
                print("No results found.....")
        elif sc == 5:
            ch = int(input("Enter The rating : "))
            found = False
            for i in moviedatas:
                if moviedatas[i]["ratings"] >= ch:
                    found = True
                    display(i)
            if found == False:
                print("No results found.....")
        elif sc == 6:
            break;
        else:
            print("Enter Valid Option....")

def display(key):
    print(key.title(),end = "")
    for l in moviedatas[key]["genre"]:
        print("  (",l,") ",sep="",end="")
    print("\t",moviedatas[key]["year"],"\t",moviedatas[key]["ratings"],"/10",sep = "")
    print(moviedatas[key]["storyline"])
    print("Box Office Collection : $",moviedatas[key]["box"],sep = "")
    print("TOP CAST :")
    for j in moviedatas[key]["cast"]:
        print(j," - ",moviedatas[key]["cast"][j])
    print("Director - ",moviedatas[key]["director"])
    print("----------------------------------------------------------")

    

def display_all():
    for i in moviedatas:
        display(i)

def edit():
    while True:
        mn = input("Enter Movie Name : ")
        if mn.lower() in moviedatas:
            break;
        else:
            print("Movie not found...")
    mov = moviedatas[mn].copy()
    org = {mn.title():mov.copy()}
    while True:
        print("Edit The\n[1]Movie Name\n[2]Year\n[3]Box Office\n[4]Cast\n[5]Director\n[6]Genre\n[7]Storyline\n[8]Exit")
        ch = int(input("Enter What to edit"))
        if ch == 1:
            inp = input("Enter The New Movie Name To change : ")
            moviedatas.pop(mn.lower())
            moviedatas[inp.lower()] = mov.copy()
            mn = inp
        elif ch == 2:
            inp = int(input("Enter The modified year : "))
            moviedatas[mn]["year"] = inp
        elif ch == 3:
            inp = int(input("Enter modified Box office collection : "))
            moviedatas[mn]["box"] = inp
        elif ch == 4:
            cas = {}
            c = int(input("Enter How Many persons on top cast : "))
            for i in range(c):
                inp2 = input("Enter the name of the person : ")
                cas[inp2.title()] = input("Enter The roll in the movie : ")
            moviedatas[mn]["cast"] = cas
        elif ch == 5:
            inp = input("Enter the name to edit the name of the director : ")
            moviedatas[mn]["director"] = inp
        elif ch == 6:
            ge = []
            g = int(input("enter how many genres"))
            for i in range(g):
                inp = input("Enter The Genre : ")
                ge.append(inp.lower()) 
            moviedatas[mn]["genre"] = ge.copy()
        elif ch == 7:
            moviedatas[mn]["storyline"] = input("Enter The modified storyline : ")
        elif ch == 8:
            mdata = open("movies.dat","wb")
            pickle.dump(moviedatas,mdata)
            mdata.close()
            break;
        else:
            print("Enter Valid Options")
    

def rating():
    global mov
    while True:
        mov = input("Enter The movie name to rate : ")
        if mov in moviedatas:
            break;
        else:
            print("Movie Not Found")
    while True:
        rate = int(input("Enter Your Rating(out of 10) :"))
        if rate >=1 and rate<=10:
            break;
        else:
            print("Enter Valid Rating......")
    rat[mov.lower()] = rate
    userdatas[uname]["ratings"].append(rat)
    u = open("users.dat","wb")
    pickle.dump(userdatas,u)
    u.close()
    avgrate()

def avgrate():
    global tot
    tot = 0
    no = 0
    for i in moviedatas:
        for j in userdatas:
            for k in userdatas[uname]["ratings"]:
                for p in k:
                    key = p
                tot+=k[key]
                no+=1
                
    avg = tot/no
    moviedatas[mov]["ratings"] = avg
    u = open("movies.dat","wb")
    pickle.dump(moviedatas,u)
    u.close()                

        

def login():
    global uname
    uname = input("Enter your username : ")
    if uname in userdatas:
        count = 0
        while count<3:
            passw = input("Enter Your Password : ")
            if userdatas[uname]["pass"] == passw:
                print("Login Success....")
                if userdatas[uname]["admin"] == True:
                    adminmenu()
                else:
                    usermenu()
                break;
            else:
                print("Wrong Password,Try Again....")
                count+=1
    else:
        print("User Not Found....")
    
def delete():
    while True:
        inp = input("Enter The Movie Name To Delete : ")
        if inp in moviedatas:
            cnf = input("Are You sure want to delete : (Y/N)")
            if cnf == "Y" or cnf == "y":
                while True:
                    cap = random.randint(1000,9999)
                    print("Your Captcha is",cap)
                    incap = int(input("Enter Your captcha : "))
                    if incap == cap:
                        break;
                    else:
                        print("Captcha is wrong.... Try again")
                moviedatas.pop(inp)
            elif cnf == "N" or cnf == "n":
                break;
            else:
                print("Enter valid options...")
        else:
            print("Movie is not found to delete.....")
            


while True:
    menu = mainmenu()
    if menu == 1:
        login()
    elif menu == 2:
        signup()
    elif menu == 3:
        print("Thank You...")
        break;
    else:
        print("Enter Valid Options Only....")
 
