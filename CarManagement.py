import logging

class CarManagement:
    def __init__(self,Cars):
        self.Cars=Cars
        
    # function to display all the available cars
    def available_cars(self):
        logging.info("Available cars: ")
        for car,car_count in self.Cars.items():
            print(car,car_count)
            
    # function to reserve car by user
    def reserve_car(self,username,carname):
        if carname not in self.Cars.keys():
            logging.error("Car is not available!! it might be due to invalid car name or car is currently not available")
        elif not self.Cars[carname]:
            logging.error("Car is currently not available")
        else:
            reserve_cars_db.update({carname:username})
            print("Hi {}, Car {} is available and booked".format(username,carname))
            #print("Updated  d: {}".format(self.reserve_cars_db))
            self.Cars[carname]=self.Cars[carname]-1
        
    # function to return car by user
    def return_car(self,username,carname):
        if carname not in reserve_cars_db.keys():
            logging.error("Requested car is not present. Please enter a valid carname or check the spelling")
        else:
            reserve_cars_db.pop(carname)
            self.Cars[carname]=self.Cars[carname]+1
            print("{} has succesfully returned car {}".format(username,carname))

    # function to add car to CarManagement by Owner
    def add_car_to_carmgmt(self,carname,c_count):
        self.Cars.update({carname:c_count})
        logging.info("Added car to CarManagement. Available cars: {}".format(self.Cars))
    
    # function to delete car from CarManagement by Owner
    def remove_car_from_carmgmt(self,carname):
        self.Cars.pop(carname)
        logging.info("Owner has removed car {} from CarManagement".format(carname))


Cars={'tata nexon':2,'hyundai creta':3,'maruti baleno':2,'ford ecosport':2,'nissan magnite':3}
car_obj=CarManagement(Cars)
reserve_cars_db={}
 
user_count=0
profile=''

while(True):
    if user_count==0:
        print("Welcome to the CarManagement!!")
        user = input("Please mention if you are Owner or User: ")
        user_count=user_count+1
    profile=user
    if profile.lower() == "user":
        # options available for user
        print("Please select any of the option:")
        print("1. Display available cars ")
        print("2. Reserve car")
        print("3. Return car")
        choice=input()
        print("User selected option is {}".format(choice))
        if choice not in ["1","2","3"]:
            print("User selected option is not valid, please select valid option")
            continue
    elif profile.lower() == "owner":
        # options available for owner
        print("Please select any of the option:")
        print("1. Display available cars")
        print("4. Add car")
        print("5. Remove car")
        choice=input()
        if choice not in ["1","4","5"]:
            print("Owner selected option is not valid, please select valid option")
            continue
        
    choice=int(choice)
    if choice==1:
        car_obj.available_cars()
    elif choice==2:
        print("Please enter the below details:")
        username=input("Enter your name: ")
        carname=input("Enter name of the car: ")
        car_obj.reserve_car(username,carname)
    elif choice==3:
        carname=input("Enter the car you would like to return: ")
        username=input("Enter your name:")
        car_obj.return_car(username,carname)
    elif choice==4:
        carname=input("Enter the car name to be added CarManagement: ")
        c_count=input("Enter number of cars to be added: ")
        car_obj.add_car_to_carmgmt(carname,c_count)
    elif choice ==5:
        carname=input("Enter the car name to be deleted from CarManagement: ")
        car_obj.remove_car_from_carmgmt(carname)
    else:
        print("Not a valid choice")
    print("To Continue enter 'c/C' and for Exit/Quit enter 'q/Q':")
    continue_choice=input()
    if continue_choice=='q' or continue_choice=='Q':
        print("Exiting CarManagement")
        exit()
    elif continue_choice=='c' or continue_choice=='C':
        continue
