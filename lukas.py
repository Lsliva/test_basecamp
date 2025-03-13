def check_if_finished(question):
    while True:
        user_input = input(f"{question} (Yes or No): ").strip().lower()
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else:
            print("Only yes or no, please try again")

def is_basecamp_complete():
    if check_if_finished("Is the assignment finished?") and check_if_finished("Is the challenge finished?"):
        return True
    else:
        return False

def is_internship_complete():
    if check_if_finished("Is the thesis finished?") or check_if_finished("Is the company happy?"):
        return True
    else:
        return False

def graduation():
    basecamp_status = is_basecamp_complete()
    internship_status = is_internship_complete()
    if basecamp_status and internship_status:
        print("Congrats you graduated!")
    elif basecamp_status == False and internship_status == False:
        print("Neither basecamp or the internship are finished")
    elif basecamp_status or internship_status:
        if internship_status:
            print("Only the internship is finished, please finish basecamp.")
        elif basecamp_status:
            print("Only the basecamp is finished, please finish the internship.")
    else:
        print("Neither basecamp or the internship is finished.")

graduation()