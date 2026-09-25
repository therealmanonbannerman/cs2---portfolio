name = input("Enter your name: ")

if name == "":
    print("ERROR 404: Student name is blank.")
else:
    section = input("Enter your section: ")

    if section != "Dahlia" and section != "Ilang-Ilang" and section != "Rosal" and section != "Sampaguita":
        print("ERROR 404: Enter a valid section.")
    else:
        club = input("Enter your club: ")

        if club != "Arab Adab" and club != "ACS" and club != "APC" and club != "Sports Club" and club != "English Club" and club != "Polaris" and club != "Dance Troupe" and club != "Danza" and club != "Chorale" and club != "Rondalla" and club != "Sigma" and club != "Earth Savers" and club != "Iskolarts" and club != "Pisay-MUN" and club != "Bahaynayan" and club != "Agham Radio Club":
            print("ERROR 404: Enter a valid club.")
        else:
            email = input("Enter your corporate email: ")

            if "@" not in email or "." not in email:
                print("ERROR 404: Enter a valid school email.")
            else:
                attendance = input("Enter attendance status:  ")

                if attendance != "Present" and attendance != "Absent" and attendance != "Late":
                    print("ERROR 404: Enter a valid attendance status.")
                else:
                    print("--------------------------------")
                    print("REGISTRATION COMPLETE")
                    print("--------------------------------")
                    print("Student:", name)
                    print("Section:", section)
                    print("Club:", club)
                    print("Email:", email)
                    print("Attendance:", attendance)
