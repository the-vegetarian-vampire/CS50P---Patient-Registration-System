# Patient Registration System
My final project for Harvard's CS50P - Introduction to Programming with Python.
    
    This is a patient registration system, the database of which is a `CSV file`. The idea of this program is to follow `CRUD`, creating, reading,              updating, and deleting a database.
    
    The program imports: `sys`, `csv`, and `emoji` libraries and contains 5 functions outside of Main().
    (1) Register patient
    (2) Search patient
    (3) Match blood-type
    (4) Update prognosis
    (5) Delete patient
    
`YOUTUBE WALKTHROUGH:` https://www.youtube.com/watch?v=Mxe5N0RC8K4

### Main() 
is a choice menu which takes user input in the range of 1-5 and passes in a function dependent on user choice. If an incorrect integer or string is entered, main will reprompt the user for correct input. However, "Q", will exit the program via sys.exit.

<img width="129" alt="Screen Shot 2022-12-23 at 4 36 49 PM" src="https://user-images.githubusercontent.com/105305546/209407602-925d37a0-5843-4882-976e-9e4e4c0be18b.png">


### (1) Register patient: 

via list of dictionaries, takes user input for keys ["name", "blood-type", "location", "prognosis"]. 'Name' uses .strip() and .capitalize() methods. 'Blood-type' prompts for a correct blood-type and uses the emoji library to add a vampire to the associated blood-type. 'Location' gives the user 3 choices to choose: primary care, surgery, or discharged, and uses the emoji library to add a thermometer, clock, or person surfing to the associated location. 'Prognosis' gives the user 3 choices to choose: good, poor, critical, and uses the emoji library to add a face with sunglasses, a thermometer, or bandages to the associated prognosis. Lastly, once all input has been received, the program opens a DictWriter and writes the input to the local CSV file and prints user input confirmation.

<img width="257" alt="Screen Shot 2022-12-23 at 4 38 59 PM" src="https://user-images.githubusercontent.com/105305546/209407739-e05c3f10-5ebb-4c6e-bea5-5b5fd3c8f238.png">


### (2) Search patient: 

takes user input for key 'name', opens DictReader to iterate over the CSV file and returns a printed match with the associated input value 'name', or 'no match found' if none was found.

<img width="144" alt="Screen Shot 2022-12-23 at 4 43 38 PM" src="https://user-images.githubusercontent.com/105305546/209407981-ab28f307-c776-42a3-a42e-8ee955cea962.png">

### (3) 

Match blood-type: takes user input for key 'blood-type' within ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], uses the emoji library to add an emoji vampire, then opens DictReader to iterate over the CSV file and returns all matches with the associated input value 'blood-type', or 'no match found' if no matches were found.

<img width="193" alt="Screen Shot 2022-12-23 at 7 54 45 PM" src="https://user-images.githubusercontent.com/105305546/209416080-8ad91cf7-7fb3-42fe-9049-c063178aa1aa.png">

### (4) Update prognosis: 

takes user input for key 'name', opens DictReader to iterate over the CSV file and find the input. If the input matches a name within the CSV file, the program will prompt the user the 3 choices to choose from: good, poor, and critical, to update the prognosis. Per user input, the program index's into the key's position and updates the value via csv.writer. If no match is found in the file, the program prints 'no match found' and returns to the choice menu.

<img width="278" alt="Screen Shot 2022-12-23 at 9 59 59 PM" src="https://user-images.githubusercontent.com/105305546/209418992-7e9ae15c-0604-4a30-b3b1-68797fa255e7.png">

### (5) Delete patient: 

takes user input for key 'name', opens DictReader to iterate over the CSV file and find the input. If the input matches a name within the CSV file, the program will prompt the user to confirm deletion via "Y/N". If the user confirms "Y", the program index's into the row and writes a new list without the input row deleting it from the CSV file.

<img width="144" alt="Screen Shot 2022-12-23 at 9 13 40 PM" src="https://user-images.githubusercontent.com/105305546/209417821-04659f2f-244d-4e26-bd1d-42784361371c.png">

Given more time I would improve the program: I believe the design would be better served creating 'patient' as a class object for its inheritence properties. As I learned more about CSV files, I learned updating and writing to an existing file may not be the best database; I would use a more interactive database like SQL, MongoDB, or Mongoose to store the data. Additionally, I would specify 'name' input using regular expressions, add a patient 'IN' and 'OUT' function using 'datetime, and add a random four digit patient ID number to each patient for flexibility with search criteria.

Overall, I'm happy with what I've built, the program covers corner cases, achieves what I intended, and provides an excellent, easy to follow user experience.
