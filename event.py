class Event(object):

	def __init__(self, day, name, start_time, end_time):
		self.day = day
		self.name = name
		self.start_time = start_time
		self.end_time = end_time

	def overlap(self, other):
		#insert code here i guess
		if other.start_time < self.start_time < other.end_time:
			return False
		elif other.start_time < self.end_time < other.end_time:
			return False
		return True


	def __str__(self):
		return "You have {} at {} until {}".format(self.name, self.start_time, self.end_time)