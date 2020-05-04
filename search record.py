
#allows the user to search the
#coffee.txt file for records matchin
# a description
def main():
    #use a boolean variable to use as a flag
    found=False
    #get the search value
    search=input("enter a description to search for")
    #open the file
    coffee_file=open("coffee.txt","r")
    #read the first record's description
    description=coffee_file.readline()
    #read the rest of the file
    while description!="":
        #read the quantity field
        qty=float(coffee_file.readline())
        #strip \n from description
        description=description.rstrip("\n")
        if description==search:
            #display the record
            print("description",description)
            print("quantity",qty)
            print()
            #set the flag to true
            found=True
        #read the next description
        description=coffee_file.readline()
    #close the file
    coffee_file.close
    #if the file was not found in file 
    #display message
    if not found:
        print("That item was not found in the file")
main()

