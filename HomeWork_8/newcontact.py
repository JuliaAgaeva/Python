

# storing the new contact details 
def newcontact(): 
    filename = "myphonebook.txt" 
    firstname = input( "Enter your First Name:")  
    lastname = input( "Enter your Last Name: ")  
    phoneNum = input( "Enter your Phone number: ") 
    emailID = input( "Enter your E-mail Address: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails+'\n') 
    print( "The following Contact Details:\n " + contactDetails + "\nhas been stored successfully!") 
    