name1="My Name Power";  
name = "";  
   
for i in range(0, len(name1)):  
    
    if name1[i].islower():  
        
        name += name1[i].upper();  
      
    elif name1[i].isupper():  
       
        name += name1[i].lower();  
      
    else:  
        name += name1[i];          
print(  name);  