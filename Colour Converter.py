#HTCS4604 Programming Foundation
#Student:Qiaoming Shi  Date:01/06/2023

print("Welcome!")#WeLcome message
print("This program converts colours in hex format to RGB format.")

hex_covert = ""

while hex_covert != "q":
  try: #use try and except to  eliminate errors  when input Valid input eg :G to Z 
    hex_covert = input("Enter a colour in hex format without the '#' or 'q' to quit: ")

    if len(hex_covert)==6:#use the len to restrict the input should be 6 characters 
        red = int(hex_covert[0:2], 16)#use the Slicing to slice 6 characters to 3 individual variable
        green = int(hex_covert[2:4], 16)
        blue = int(hex_covert[4:6], 16)
        print(red, green, blue)
#while loop input Q or q to quit  and stop looping    
    elif "q" in hex_covert.lower():
        break
        
    else:
        print("Invalid input. Please enter a valid hexadecimal colour code.")
  except ValueError:
        print("Invalid input.Please enter 0 to 9 or A to F")
print("Goodbye have a nice day")
#Goodbye Message