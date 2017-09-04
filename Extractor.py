import whois
import os
import sys
'''
module > pip3 install python-whois

To Extract Information about the Domain Registrant

Make a file that has 'Domain name' to Search for then here name it as -
"shortdomains.txt" put it in same folder with python script.

the output > 'out.txt'  will be in the same folder as of this Python folder

Run the script
'''


cwd = os.getcwd()

'''  file=open(cwd + "/out","a")  >  To Redirect the output to 'cwd' Directory
  with file name 'out'
'''
print("Output in File" , cwd + "/out.txt")

#Range of domains to get INFO : ex - between 250 - 256 

UPPER_num = input("ENTER THE UPPER LIMIT OF DOMAINS > " )  #256  
LOWER_num = input("ENTER THE LOWER LIMIT OF DOMAINS > " )  #250



#Function to extract the Domain name

def name_domain():

   with open(cwd + '/shortdomains.txt' , 'r') as f:
       content = f.readlines()
   
   content = [x.strip() for x in content]

   
   for lists in range(int(LOWER_num),int(UPPER_num)):

      
      #Extracting INFO
      
      def info():

          w = whois.whois(content[lists])    
           # print(w)
          print( "_  Domain Name  _:\n" ,w.domain_name , file=open(cwd + "/out","a") )
       
          print("_  Organisation  _:\n" , w.org , file=open(cwd + "/out","a") )

   
          print("_  EMAIL INFO  _:" , file=open(cwd + "/out","a"))
          print(w.emails , file=open(cwd + "/out","a"))
    
          print("\n" , file=open(cwd + "/out","a"))            
          print("_  ADDRESS INFO  _:" , file=open(cwd + "/out","a"))
          print(w.address , file=open(cwd + "/out","a"))
    
          country = w.country 
          city = w.city
    
          print(city ,"\t", w.zipcode , file=open(cwd + "/out","a"))
    
          print(country , file=open(cwd + "/out","a"))
    
          print("\n" , file=open(cwd + "/out","a"))

    
          def fax_info():  #Extracting Fax Number from 'w.text' string
              str1 = w.text
              str2 = "Registrant Fax"
              index = str1.find(str2)
              i = index
              while(w.text[i] is not "\n"):
                  print(w.text[i] ,end='' , file=open(cwd + "/out","a"))
                  i = i+1
            
          fax_info()

    
          print("\n" , file=open(cwd + "/out","a") )

    
          def phone_info():
                 str1 = w.text
                 str2 = "Registrant Phone"
                 index = str1.find(str2)
                 i = index
                 while(w.text[i] is not "\n"):
                      print(w.text[i] ,end='' , file=open(cwd + "/out","a"))
                      i = i+1
            
          phone_info()
          
      

      info()
    
      print("\n______________________________________________________" , file=open(cwd + "/out","a"))


      
if __name__ == "__main__":
    
      
    name_domain()

    
   
    
