
#the program allows the user to modify the quantity
#in a record in the coffee.txt file
import os #library needed to remove and rename functions
def main():
    #create a boolean variable to use as a flag
    found=False
    #get search value and new quantity
    search=input("enter a description to search for")
    new_qty=int(input("enter the new quantity"))
    #open the original.txt file
    coffee_file=open("coffee.txt","r")
    #open the temporary file
    temp_file=open("temp.txt","w")
    #read the first record description file
    description=coffee_file.readline()
    #read rest of the file
    while description!="":
        #read the quantity field
        qty=float(coffee_file.readline())
        #strip \n from description
        description=description.rstrip("\n")
        #write either this record to the temporary file
        #or the new record is this is the one
        #to be modified
        if description==search:
            #write the modified record to temp file
            temp_file.write(description+"\n")
            temp_file.write(str(new_qty)+"\n")
            #set the found flag to true
            found=True
        else:
            #write original record to temp_file
            temp_file.write(description+"\n")
            temp_file.write(str(qty)+"\n")
        #read the next descripion
        description=description=coffee_file.readline()
    #close the coffee_file and temporary_file
    coffee_file.close()
    temp_file.close()
    #delete original coffee.txt file
    os.remove("coffee.txt")
    #rename temporary file
    os.rename("temp.txt","coffee.txt")
    #if search value was not found in the display
    #display the message
    if found:
        print("the file has been updated")
    else:
        print("The item was not found in the file")
main()

