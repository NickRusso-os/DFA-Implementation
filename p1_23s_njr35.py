#Nicholas Russo
#njr35

#1
print("Project 1 for CS 341")
print("Section number: 008")
print("Semester: Spring 2023")
print("Written by: Nicholas Russo, njr35")
print("Instructor: Marvin Nakayama, marvin@njit.edu")

#2
while True:
    #user input about continuing loop
    ans = input("Do you want to enter a string? y/n ")
    if ans == "n":
        exit(0)
    if ans == "y":
        #get and store user string
        user_string = input("Please enter a string over Σ: ")
        print(user_string)
    #3
    upsilon = "0123456789"
    psi = "abcdefghijklmnopqrstuvwxyz"
    delta = "."
    theta = "@"
    #initialize current state to q0
    current_state = "q0"
    print(" " , current_state)
    #loop through user string one letter at a time  
    for letter in user_string:
    #move through each state according to the current state and the current character
        #process q0 state
        if current_state == "q0":
            if letter in psi:
                current_state = "q1"
                print(letter , current_state)
                continue
        #process q1 state
        if current_state == "q1":
            if letter in psi or letter in upsilon:
                current_state = "q1"
                print(letter , current_state)
                continue
            if letter == delta:
                current_state = "q2"
                print(letter , current_state)
                continue
            if letter == theta:
                current_state = "q4"
                print(letter , current_state)
                continue
        #process q2 state           
        if current_state == "q2":
            if letter in psi:
                current_state = "q3"
                print(letter , current_state)
                continue
        #process q3 state
        if current_state == "q3":
            if letter in psi or letter in upsilon:
                current_state = "q3"
                print(letter , current_state)
                continue
            if letter == delta:
                current_state = "q2"
                print(letter , current_state)
                continue
            if letter == theta:
                current_state = "q4"
                print(letter , current_state)
                continue
        #process q4 state            
        if current_state == "q4":
            if letter in psi:
                current_state = "q5"
                print(letter , current_state)
                continue
        #process q5 state
        if current_state == "q5":
            if letter in psi or letter in upsilon:
                current_state = "q5"
                print(letter , current_state)
                continue
            if letter == delta:
                current_state = "q6"
                print(letter , current_state)
                continue
        #process q6 state           
        if current_state == "q6":
            if letter == "e":
                current_state = "q8"
                print(letter , current_state)
                continue
            if letter in psi:
                current_state = "q7"
                print(letter , current_state)
                continue
        #process q7 state
        if current_state == "q7":
            if letter in psi or letter in upsilon:
                current_state = "q7"
                print(letter , current_state)
                continue
            if letter == delta:
                current_state = "q6"
                print(letter , current_state)
                continue
        #process q8 state           
        if current_state == "q8":
            if letter == "d":
                current_state = "q9"
                print(letter , current_state)
                continue
            if letter in psi or letter in upsilon:
                current_state = "q7"
                print(letter , current_state)
                continue
            if letter == delta:
                current_state = "q6"
                print(letter , current_state)
                continue
        #process q9 state
        if current_state == "q9":
            if letter == "u":
                current_state = "q10"
                print(letter , current_state)
                continue
            if letter in psi or letter in upsilon:
                current_state = "q7"
                print(letter , current_state)
                continue
            if letter == delta:
                current_state = "q6"
                print(letter , current_state)
                continue
        #process q10 state
        if current_state == "q10":
            if letter == delta:
                current_state = "q6"
                print(letter , current_state)
                continue
            if letter in psi or letter in upsilon:
                current_state = "q7"
                print(letter , current_state)
                continue
    #print "accepted" if final state is q10 (goal state)   
    if current_state == "q10":
        print("String Accepted")
    else:
        print("String Rejected")


        

    

