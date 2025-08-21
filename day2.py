a=int(input("Enter your makrs:"))
if (a>100):
    print("Invalid")
    a=int(input("Enter your marks:"))    
    if(a<0):
      print("Invalid") 
      a=int(input("Enter your marks:"))
      if(a>=90):
          print("A+")   
      elif(a>=75):
           print("A")
      elif(a>=60):
           print("B")
      elif(a>=40):
           print("C")
      else:
           print("Fail")      
                  

