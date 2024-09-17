# 🎉 Random Contacts Generator 📇

Welcome to the **Random Contacts Generator**! This Python project generates a large number of unique and realistic Indian contact details, including names and mobile numbers, and exports them into a `.vcf` (vCard) file format.

This can be useful for testing mobile applications, contact management systems, or any scenario where you need a list of realistic Indian names and mobile numbers.

## 🚀 Features
- Generates **thousands** of unique contacts.
- Creates a **vCard** file (`.vcf`) with **realistic Indian names** and mobile numbers.
- Includes both **male** and **female** names.
- Randomly adds last names to the contacts.
- Exports ready-to-import contact lists for apps or devices.

## 📂 Project Structure

```plaintext
📦random_contacts_generator
 ┣ 📜main.py                 # The main script to run
 ┣ 📜male_first_names.py      # List of male first names
 ┣ 📜female_first_names.py    # List of female first names
 ┣ 📜last_names.py            # List of last names
 ┗ 📜README.md                # Project documentation
```

## ⚙️ Requirements
- Python 3.7+ should be installed on your machine.

To check your Python version, use:
```plaintext
python --version
```

## 🛠️ Installation and Setup
### Step 1: Clone the Repository
Clone the repository using:
```plaintext
git clone https://github.com/saiareti-crct/random-contacts-generator.git
```
Navigate into the project folder:
```plaintext
cd random_contacts_generator
```
### Step 2: Install Dependencies
There are no external dependencies for this project. Just make sure you have Python installed.

### Step 3: Run the Script
To generate the random contacts, execute the following command in your terminal:
```plaintext
python main.py
```
This will generate 10 contacts by default and save them to a file named random_contacts.vcf. You can adjust the number of contacts by modifying the num_contacts variable in main.py:

Change this value to generate more or fewer contacts
```plaintext
num_contacts = 10
```

## 💾 Output
The generated contacts are saved as a .vcf file, suitable for import into mobile contact apps.

File: random_contacts.vcf
Format: vCard 3.0 with contact names and mobile numbers.

## 📜 Example Contact (vCard Format)
Here’s how a contact will appear in the .vcf file:
```plaintext
plaintext
Copy code
BEGIN:VCARD
VERSION:3.0
FN:Sai Areti
TEL;TYPE=CELL:+919876543210
END:VCARD
```
This format is compatible with most contact management applications.

## 🎯 Customization
You can customize the number of contacts, name lists, or vCard structure by editing the main.py script.

Name lists: Modify male_first_names.py, female_first_names.py, and last_names.py.
vCard Format: Adjust the vCard creation logic in generate_contact() to include additional fields like email or address.

## 🤔 FAQs
### How do I import the .vcf file into my phone?
- Connect your phone to your computer.
- Transfer the .vcf file to your phone.
- Open the file with your Contacts app to import the contacts.
### Can I generate more or fewer contacts?
- Yes! Change the num_contacts variable in main.py.
### Is it possible to add more fields like email or address?
- Yes! Modify the vCard creation logic in generate_contact().
