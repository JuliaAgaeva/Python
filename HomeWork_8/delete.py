import re


def deletecontact(): 
    str = input( "Enter contact to delete: ") 
    with open('myphonebook.txt', 'r') as f:
      lines = f.readlines()
      pattern = re.compile(re.escape(str))
      with open('myphonebook.txt', 'w') as f:
        for line in lines:
         result = pattern.search(line)
        if result is None:
            f.write(line)









