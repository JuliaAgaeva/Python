from searchcontact import searchcontact
from newcontact import newcontact


def greeting():
 print( "WELCOME TO THE PHONEBOOK DIRECTORY") 
 
# creating a .txt file to store contact details 
filename = "myphonebook.txt" 
myfile = open(filename, "a+")   
myfile.close 
 
# defining main menu 
def main_menu(): 
    print( "\nMAIN MENU\n") 
    print( "1. Show all existing Contacts") 
    print( "2. Add a new Contact") 
    print( "3. Search the existing Contact") 
    print( "4. Exit") 
    choice = input("Enter your choice: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "There is no contact in the phonebook.") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Press Enter to continue ...") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Press Enter to continue ...") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Press Enter to continue ...") 
        main_menu() 
    elif choice == "4": 
        print("Thank you for using Phonebook!") 
    else: 
        print( "Please provide a valid input!\n") 
        enter = input( "Press Enter to continue ...") 
        main_menu() 
 


 

