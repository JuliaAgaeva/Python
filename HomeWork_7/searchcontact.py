

# defining search function  
#        
def searchcontact(): 
    filename = "myphonebook.txt" 
    searchname = input( "Enter First name for Searching contact record: ") 
    with open(filename, "r") as f:
     for line in f: 
      if searchname in line: 
        print(line) 
   


   
    #word = str(input("слово  "))
    #with open ('example.txt', "r") as f:
    #for line in f:
    #if word in line:
    #print(line)