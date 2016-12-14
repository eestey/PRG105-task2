def returning():
    print "Returning Customer"


def new():
    print "New Customer"


def guest():
    print "Hello Guest"

    print "[======================]"
    print "   1. Returning Customer"
    print "   2. New Customer"
    print "   3. Guest"
    print "[======================]\n"


choice = 0
while choice >= 0:
    try:
        if choice < 1 or choice > 3:
            choice = int(raw_input("Choose an option:   "))
            continue
        elif choice == 1:
            returning()
            break
        elif choice == 2:
            new()
            break
        elif choice == 3:
            guest()
            break
        else:
            print "\n\nNot a valid choice:   "
            continue
    except ValueError:
        if choice != 1 or choice != 2 or choice != 3:
            choice = int(raw_input("Please select customer choice\n Enter a number between 1 and 3: "))
        elif choice == 1:
            print "Welcome Back!"
            break
        elif choice == 2:
            print "Please fill out the information"
            break
        elif choice == 3:
            print "Hello Guest"
            break
