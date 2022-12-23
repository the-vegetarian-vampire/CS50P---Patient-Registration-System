import sys
import csv
import emoji

data = "patient.csv"

def main():
        while True:
            choice = input("\nWhat would you like to do?\n(1) Register patient \n(2) Search patient\n(3) Match blood-type\n(4) Update prognosis\n(5) Delete patient\n(Q) -- Sys Exit --\nEnter 1-5: ")
            if choice == "Q" or choice == "q":
                sys.exit
                break
            elif choice == "1":
                register_patient(choice)
            elif choice == "2":
                search_patient(choice)
            elif choice == "4":
                match_blood(choice)
            elif choice == "5":
                update_prog(choice)
            elif choice == "6":
                delete_patient(choice)
            else:
                print("\n--Invalid input--")
                continue

def register_patient(n): # Register patient
        patient_name = input("Name: ").strip().capitalize()
        while True:
            blood_type = input("Blood-type: ").upper()
            if blood_type not in ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]:
                print("Invalid type: A+ A- B+ B- O+ O- AB+ AB-")
            else:
                blood_type = emoji.emojize(blood_type + ":vampire:", language='alias')
                break
        while True:
            location = input("Location: (p)rimary care, (s)urgery, (d)ischarged): ").strip().lower()
            if location not in ["p", "s", "d"]:
                print("Invalid location")
                continue
            elif location == "p":
                location = emoji.emojize("primary care :thermometer:", language='alias')
            elif location == "s":
                location = emoji.emojize("surgery :one_o’clock:", language='alias')
            elif location == "d":
                location = emoji.emojize("discharged :person_surfing:", language='alias')
            break
        while True:
            prognosis = input("Prognosis: (g)ood, (p)oor, (c)ritical): ").strip().lower()
            if prognosis not in ["g", "p", "c"]:
                print("Invalid prognosis")
                continue
            elif prognosis == "g":
                prognosis = emoji.emojize("good :sunglasses:", language='alias')
            elif prognosis == "p":
                prognosis = emoji.emojize("poor :face_with_thermometer:", language='alias')
            elif prognosis == "c":
                prognosis = emoji.emojize("critical :face_with_head-bandage:", language='alias')
            break
        with open(data, "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "blood-type", "location", "prognosis"])
            writer.writerow(({"name": patient_name, "blood-type": blood_type, "location": location, "prognosis": prognosis}))
            print(f"\nPatient Registered:\nNAME: {patient_name}\nBLOOD-TYPE: {blood_type}\nLOCATION: {location}\nPROGNOSIS: {prognosis}")

def search_patient(s): # Search patient:
    match = 0
    name = input("Search Name: ").lower().capitalize().strip()
    with open(data) as file:
        reader = csv.DictReader(file)
        for row in reader:
            ls = []
            a = row["name"]
            b = row["blood-type"]
            c = row["location"]
            d = row["prognosis"]
            if a == name:
                ls.append({"name": a, "blood-type": b, "location": c, "prognosis": d})
                print(f"\nMatch:\nNAME: {a}\nBLOOD-TYPE: {b}\nLOCATION: {c}\nPROGNOSIS: {d}")
                match = 1
        if match == 0:
            print("\nNo match found")

def match_blood(y): # Match blood-type:
    match = 0
    while True:
        blood_entry = input("Patient blood-type: ").strip().upper()
        if blood_entry not in ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]:
            print("Invalid blood-type: A+ A- B+ B- O+ O- AB+ AB-")
            continue
        else:
            emoji_blood = emoji.emojize(blood_entry + ":vampire:", language='alias')
            with open(data) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    all = []
                    a = row["name"]
                    b = row["blood-type"]
                    all.append({"name": a, "blood-type": b})
                    if b == emoji_blood:
                        for name in sorted(all, key=lambda name: name["name"]):
                            print(f" --> Match: {name['name']} is {name['blood-type']}")
                            #print(f" --> Match: {a} is {b}")
                        match = 1
                        continue
                if match == 0:
                    print("\nNo match found")
        break

def update_prog(p): # Update prognosis
    f=open(data, "r")
    reader = csv.reader(f)
    match = 0
    list = []
    name = input("Name to update: ").lower().capitalize().strip()
    for row in reader:
        if(row[0] == name):
            print("\nMatch: "f"{name}'s prognosis is currently {row[3]}")
            while True:
                row[3] = input("Update: (g)ood, (p)oor, (c)ritical): ").strip().lower()
                if row[3] not in ["g", "p", "c"]:
                    print("Invalid prognosis")
                    continue
                elif row[3] == "g":
                    row[3] = emoji.emojize("good :sunglasses:", language='alias')
                elif row[3] == "p":
                    row[3] = emoji.emojize("poor :face_with_thermometer:", language='alias')
                elif row[3] == "c":
                    row[3] = emoji.emojize("critical :face_with_head-bandage:", language='alias')
                match = 1
                break
        list.append(row)

    if match == 0:
        print("\nNo match")
        f.close

    else:
        f = open(data, "w", newline='')
        reader=csv.writer(f)
        reader.writerows(list)
        f.close

def delete_patient(p): # Delete patient:
    f=open(data, "r")
    reader = csv.reader(f)
    list = []
    name = input("Search Name: ").lower().capitalize().strip()
    found = False
    for row in reader:
        if(row[0] == name):
            found = True
        else:
            list.append(row)
    f.close()

    if found == False:
        print("\nName not found")
    else:
        print(f"\nMatch: {name}")
        confirm_delete = input("Confirm delete? Y/N? ").lower()
        while True:
            if confirm_delete not in ["y", "yes", "n", "no"]:
                print("Invalid input")
                continue
            elif confirm_delete == "n" or confirm_delete == "no":
                break
            else:
                f = open(data, "w", newline='')
                writer = csv.writer(f)
                writer.writerows(list)
                f.close
                print("\nPatient deleted")
                break

if __name__ == "__main__":
    main()
