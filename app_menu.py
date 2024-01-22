while True: #input validation
    print ("\nPlease select an activity from the following options:") #menu system
    print ("[1] Sorting Integers\n[2] Noughts and Crosses")
    menu = input ("[1/2]:")

    if menu == "1":
        print ("\n[SORTING INTEGERS]")
        from integer_sorting import int_sort #calls module for integer sorting program
        int_sort()
        continue

    if menu == "2":
        print ("\n[NOUGHTS AND CROSSES]\n")
        from noughts_crosses import wipe_scores #calls module for noughts and crosses game.
        wipe_scores()
        continue

    else:
        print ("\nplease enter a listed number.\n")
        continue




