print("WELCOME TO THE GRANN'S PHONE DIRECTORY\n 1.Add a record\n 2.Search a record\n 3.Update a record\n 4.Sort the record alphabetically\n 5.Delete a record\n 6.Quit")
phoneDirectory={}
x=int(input("Enter your choice"))

while(x!=6):
 if(x==1):
  
  print("input new record")
  a=input("enter name")
  b=int(input("enter your 10 digit number:"))
  phoneDirectory.update({a:b})
 
  print("new data is added")


 elif(x==2):
   
  c=input("enter name")
  d=int(input("enter your 10 digit number:"))
  phoneDirectory.update({c:d})
  print("new data is added")
  
 elif(x==3):
   
  e=input("enter name")
  f=int(input("enter your 10 digit number:"))
  phoneDirectory.update({e:f})
  print("new data is added")


 elif(x==4):
  i=input("enter your choice")
  j=int(input("enter sorted record"))
  phoneDirectory.update({i:j})

 elif(x==5):
  l=input("enter your choice")
  k=input("enter name")
 
 elif(x==5):
  m=input("enter your choice")
  print("exit from the whole program")