

def searchcontact(): 
    filename = "myphonebook.txt" 
    searchname = input( "Enter First name for Searching contact record: ") 
    with open(filename, "r") as f:
     for line in f: 
      if searchname in line: 
        print(line) 
   


