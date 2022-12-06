from searchcontact import searchcontact
from newcontact import newcontact
from delete import deletecontact
from export_to_file import export_txt 

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
    print( "4. Delete Contact")
    print("5. Export to file") 
    print( "6. Exit") 
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
        header = [ ' First Name', 'Last Name', 'Phone number', 'E-mail Address \n']
        print(' | ',end='')
        for name in header:
         print( name, ' | ', '\n')
    
        searchcontact() 
        enter = input("Press Enter to continue ...") 
        main_menu() 

    elif choice == "4": 
        deletecontact() 
        enter = input("Press Enter to continue ...") 
        main_menu() 
     
    elif choice == "5": 
        export_txt() 
        enter = input("Press Enter to continue ...") 
        main_menu() 

    elif choice == "6": 
        print("Thank you for using Phonebook!") 
    else: 
        print( "Please provide a valid input!\n") 
        enter = input( "Press Enter to continue ...") 
        main_menu() 
 


 

