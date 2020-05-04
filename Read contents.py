#program shows records in coffee.txt file
def main():
    #open coffee.txt file
    coffee_file=open("coffee.txt","r")
    #read first record description field
    description=coffee_file.readline()
    #use while loop to read rest of file
    while description!="":
        #read quantity field
        #converted to float because it is stored as a string
        qty=float(coffee_file.readline())
        #strip \n from description..not from the float
        description=description.rstrip("\n")
        #show the record
        print("description",description)
        print("quantity",qty)
        #read next line-description
        description=coffee_file.readline()
    #clode the file
    coffee_file.close()
main()
