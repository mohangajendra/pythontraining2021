guests=["virat", "sachin", "lara", "kallis"]

print("Hello, " +guests[0].title() + " you are invited for dinner at my place")
print("Hello, " +guests[1].title() + " you are invited for dinner at my place")
print("Hello, " +guests[2].title() + " you are invited for dinner at my place")
print("Hello, " +guests[3].title() + " you are invited for dinner at my place")


#changing Guest list
print("changing Guest list")



no_show_guest=guests[1]

print("Hello All, " +no_show_guest.title() + " would not be making it to Dinner")

guests[1]="Donald"

print(guests[1].title() + " will join us instead of " + no_show_guest.title())

print("Hello, " +guests[0].title() + " you are invited for dinner at my place")
print("Hello, " +guests[1].title() + " you are invited for dinner at my place")
print("Hello, " +guests[2].title() + " you are invited for dinner at my place")
print("Hello, " +guests[3].title() + " you are invited for dinner at my place")

####### inserting guest to the list

guests.insert(0, "nikita")

guests.insert(3, "ponting")

guests.append("pooja")

print(guests)


####### popping guests from the list

print(" Hello All, sorry I can only invite two, as we got table for just two, thank you")

last_guest=guests.pop()
print("Hello " + last_guest.title() + "\n sorry we couldn't get a table for all and hence cancelling the dinner for you ")
last_guest=guests.pop()
print("Hello " + last_guest.title() + "\n sorry we couldn't get a table for all and hence cancelling the dinner for you ")
last_guest=guests.pop()
print("Hello " + last_guest.title() + "\n sorry we couldn't get a table for all and hence cancelling the dinner for you ")
last_guest=guests.pop()
print("Hello " + last_guest.title() + "\n sorry we couldn't get a table for all and hence cancelling the dinner for you ")
print(guests)
last_guest=guests.pop()
print("Hello " + last_guest.title() + "\n sorry we couldn't get a table for all and hence cancelling the dinner for you ")
print(guests)
print(" Hello invited for the Dinner ")

###	deleting guests from list##
del guests[0]
del guests[0]
print("printing empty list")
print(guests)

