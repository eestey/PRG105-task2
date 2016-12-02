choice = 0
while choice >= 0:
    print "[======================]"
    print "   1. Returning Customer"
    print "   2. New Customer"
    print "   3. Guest"
    print "[======================]\n"

    choice = int(raw_input("Choose an option:  "))
    try:
        if choice <1 or choice > 3:
            choice = int(raw_input("Choose an option:   "))
        elif choice == 1:
            print "Welcome Back!"
            choice = -1
        elif choice == 2:
            print "Welcome!\n"
            choice = -1
        elif choice == 3:
            print "Hello Guest"
            choice = -1
        else:
            print "\n\nChoose an option:   "
    except ValueError:
        print "Choose an option:   "
