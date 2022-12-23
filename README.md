# Patient Registration System
    Description:
    This is a patient registration system, the database of which is a CSV file. The program imports: sys, csv, and emoji libraries and contains 5 functions outside of Main().
    (1) Register patient
    (2) Search patient
    (3) Match blood-type
    (4) Update prognosis
    (5) Delete patient

Main is a choice menu which takes user input in the range of 5 choices and passes a function dependent on user choice. If an incorrect integer or string is entered, main will reprompt the user for correct input. However, "Q", will exit the program via sys.exit.

(1) Register patient: via list of dictionaries, takes user input for keys ["name", "blood-type", "location", "prognosis"]. 'Name' uses .strip() and .capitalize() methods. 'Blood-type' prompts for a correct blood-type and uses the emoji library to add a vampire to the associated blood-type. 'Location' gives the user 3 choices to choose from: primary care, surgery, or discharged, and uses the emoji library to add a thermometer, clock, or person surfing to the associated location. 'Prognosis' gives the user 3 choices to choose from: good, poor, critical, and uses the emoji library to add a face with sunglasses, a thermometer, or bandages to the associated prognosis. Lastly, once all input has been received, the program opens a DictWriter and writes the input to the local CSV file and prints user input confirmation.

For example: Patient Registered: NAME: Abraham lincoln BLOOD-TYPE: O+🧛 LOCATION: surgery 🕐 PROGNOSIS: critical 🤕.

(2) Search patient: takes user input for key 'name', opens DictReader to iterate over the CSV file and returns a printed match with the associated input value 'name', or 'no match found' if none was found.

(3) Match blood-type: takes user input for key 'blood-type' within ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], uses the emoji library to add an emoji vampire, then opens DictReader to iterate over the CSV file and returns all printed matches with the associated input value 'blood-type', or 'no match found' if no matches were found.

(4) Update prognosis: takes user input for key 'name', opens DictReader to iterate over the CSV file and find the input. If the input matches a name within the CSV file, the program will prompt the user the 3 choices to choose from: good, poor, and critical, to update the prognosis. Per the user input, the program index's into the value's position and updates the value via csv.writer. If no initial match is found in the file, the program prints 'no match found' and returns to the choice menu.

(5) Delete patient: takes user input for key 'name', opens DictReader to iterate over the CSV file and find the input. If the input matches a name within the CSV file, the program will prompt the user to confirm deletion via "Y/N". If the user confirms "Y", the program index's into the row and writes a new list without the input row's associated key and value pairs, deleting each from the CSV file.

Given more time I would improve the program: I believe the design would be better served using classes and creating 'patient' as an object. As I learned more about CSV files, I learned updating and writing to an existing file may not be the best database. Moreover, I would use a more interactive database like SQL, MongoDB, or Mongoose to store the data. Additionally, I would also specify 'name' input using regular expressions, add a patient 'IN' and 'OUT' function using 'datetime, and add a random four digit patient ID number to each patient for more flexibility with search criteria.

Overall, I'm happy with what I've built, the program covers corner cases, achieves what I intended, and provides an excellent, easy to follow user experience.
