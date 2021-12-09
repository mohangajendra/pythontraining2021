#Exercise_1
import datetime
def age_at_100(age,copies):
	now=datetime.datetime.now()
	cur_year=now.year
	years=100-age
	#print("you will 100years old on year: " + str(years+cur_year))
	#Print out that many copies of the previous message on separate lines.
	print(copies* ("you will 100years old on year: " + str(years+cur_year) +"\n"))

if __name__=='__main__':
	age=int(input(("Enter your age: ")))
	copies=int(input("number of copies wanted:"))
	age_at_100(age, copies)
