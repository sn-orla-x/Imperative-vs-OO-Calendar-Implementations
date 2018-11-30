#dictionary was hard coded
appoints = {"Monday" : [],
	   "Tuesday": [],
	   "Wednesday": [],
	   "Thursday": [],
	   "Friday": [],
	   "Saturday": [],
	   "Sunday": []}

#prompty prompts the user to enter commands on their terminal and then runs the command that they enter
def prompty():
	prompt = input("Enter a command: ")

	if prompt == "close":
		return
	elif prompt == "add" :
		add_appoint()
	elif prompt == "delete":
		delete_appoint()
	elif prompt == "print day":
		print_day()
	elif prompt == "print week":
		print_week()
	else:
		print("This command doesn't exist! Enter a new one")
	prompty()
		
	 

def add_appoint():
	day = input("Please enter what day your appointment is on: ")
	appoint_name = input("What is your appointment?: ")
	start_time = float(input("Enter your start time: "))
	end_time =  float(input("Enter the time it ends at: "))
	if overlap_checker(day, start_time, end_time):
		appoints[day].append([appoint_name,start_time,end_time])
		print("Your {} appointment on {} has been added to the calendar.".format(appoint_name, day))
	else:
		print("There is an overlap with your schedule, please check your calendar and try again!")
	#print(appoints)
	return

def delete_appoint():
	day = input("What day is the appointment you wish to delete on?: ")
	appoint_name = input("What is the appointment?:")
	for appointment in appoints[day]:
		if appointment[0] == appoint_name:
			appoints[day].remove(appointment)
			print("Your {} appointment on {} has been deleted from the calendar.".format(appoint_name,day))
	print("There is no such appointment")
	#print(appoints)
	return

def print_day():
	day = input("What day would you like to see?: ")
	for appointment in appoints[day]:
		print("On {}, at {:.2f} you have a {}. It finishes at {:.2f}.".format(day, appointment[1], appointment[0], appointment[2]))
	
	return

def print_week():
	weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	for day in weekdays:
		print(day)
		if appoints[day] == []:
			print("Nothing scheduled for today!")
		else:
			for appointment in appoints[day]:
				print("At {:.2f}, you have a {}. It finishes at {:.2f}".format(appointment[1], appointment[0], appointment[2]))
	return

#checks to see if an appointment overlaps with another appointment
def overlap_checker(day, start_time, end_time):
	for appointment in appoints[day]:
		if appointment[1] < start_time < appointment[2]:
			return False
		elif appointment[1] < end_time < appointment[2]:
			return False
	return True

def main():
	print("Welcome to your calendar! Please enter times using the 24 clock.\nYour options are: \nAdd an appointment using 'add' \nDelete an appoint using 'delete' \nView a specific day using 'print day' \nView the entire week using 'print week'\nClose the calendar using 'close'")
	prompty()
if __name__ == '__main__':
	main()