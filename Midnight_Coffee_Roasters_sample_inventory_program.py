#program adds coffee inventory records 
#to coffee.txt file
def main():
    #create variable to create loop
    another="y"
    #open coffeee.txt file in append mode
    coffee_file=open("coffee.txt","a")
    #add records to file using while loop
    while another=="y" or another=="Y":#use .upper()
        #get coffee record data from the user
        #record is the description/type and the quantity
        print("enter the following data")
        description=input("description")
        qty=int(input("enter quantity(in pounds"))
        #append the data to the file
        coffee_file.write(description+"\n")
        coffee_file.write(str(qty)+"\n")
        #do you want to add another record to the file
        print("do you want to add another record")
        another=input("Y=yes,anything else=no:")
    #close the file
    coffee_file.close()
    print("data appended to coffee.txt")
main()
