from event import Event

class Calendar():
	def __init__(self):
		self.week = {"Monday": [],
					"Tuesday": [],
					"Wednesday": [],
					"Thursday": [],
					"Friday": [],
					"Saturday": [],
					"Sunday": []
									}


	def add(self):
		day = str(input("Please enter what day your appointment is on: "))
		appoint_name = str(input("What is your appointment?: "))
		start_time = float(input("Enter your start time: "))
		end_time =  float(input("Enter the time it ends at: "))
		event = Event(day, appoint_name, start_time, end_time)
		okayToAdd = True
		for e in self.week[day]:
			if event.overlap(e): # return true if not overlapping, return false if overlapping
				okayToAdd = True
			else:
				okayToAdd = False

		if okayToAdd:
			self.week[day].append(event)
			print("Your {} appointment on {} has been added".format(event.name, event.day))
		else:
			print("Your appointment overlaps with another appointment, please check and try again!")
	#print(appoints)
		return



	def delete(self):
		day = input("Please enter the day you want to delete an appointment on: ")
		appoint_name = input("Please enter the appointment you want to delete: ")
		for e in self.week[day]:
			if e.name == appoint_name:
				self.week[day].remove(e)
			print("Your appointment has been removed!")




	def show_day(self):
		day = input("Please enter the day you'd like to show: ")
		print(day)
		for e in self.week[day]:
			print(e)

		return



	def show_week(self):
		days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		for day in days:
			if self.week[day] == []:
				print(day)
				print("Nothing scheduled for today, buddy!")
			else:
				print(day)
				for e in self.week[day]:
					print(e)
		return

	def prompty(self):
		prompt = input("Enter a command: ")

		if str(prompt) == 'close':
			return
		elif str(prompt) == 'add' :
			self.add()
		elif str(prompt) == 'delete':
			self.delete()
		elif str(prompt) == 'print day':
			self.show_day()
		elif str(prompt) == 'print week':
			self.show_week()
		else:
			print("This command doesn't exist! Enter a new one")
		self.prompty()
		
def main():
	calendar = Calendar()
	print("Welcome to your calendar! Please enter times using the 24 clock.\nYour options are: \nAdd an appointment using 'add' \nDelete an appoint using 'delete' \nView a specific day using 'print day' \nView the entire week using 'print week'\nClose the calendar using 'close'")
	calendar.prompty()
if __name__ == '__main__':
	main()