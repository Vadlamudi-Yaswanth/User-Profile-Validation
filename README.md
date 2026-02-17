## User-Profile-Validation
Description:
This project is designed to validate user profile details using Python.
It checks whether the user input such as name, phone number, and other details meet the required validation rules.
Purpose:
The main purpose of this project is to practice input validation in Python
How the Code Works:
- The program takes user input from the console.
- It validates each field using conditional statements.
- If the input is valid, it displays a User Profile is Valid.
- If the input is invalid, it shows User Profile is InValid.
Files in This Project:
- `Day1_Challenge.py` : Contains the Python code for user profile validation.
Output:
The program displays whether the entered user details are valid or not based on the given conditions.
##output screenshot:
<img width="1920" height="1080" alt="Screenshot 2026-01-29 190432" src="https://github.com/user-attachments/assets/8a4c3685-fb20-4e7a-9bbb-7720094dc54d" />
# -Smart-ID-Credential-Validator
Purpose:
The main purpose of this project is to understand and practice string validation concepts in Python, such as checking characters, symbols, and conditions without using built-in validation functions.
The program accepts the following inputs from the user:
Student ID
Email ID
Password
Referral Code
And checks which is checked first password or student_Id
Each input is validated based on specific rules.
If all validation rules are satisfied, the program displays APPROVED.
If any rule fails, the program displays REJECTED.
Day2_Challenge.py : Contains the Python program for validating student credentials.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/988cf16c-82a1-486e-9989-44e48287cc94" />

# Student-Performance-Analyzer
## Description
This project is designed to analyze student performance based on their internal
assessment marks using Python. The marks are stored in a list and processed
one by one to determine the performance category of each student.
 Purpose:
The main purpose of this project is to practice using lists, for loops, and
conditional statements in Python without using any advanced data structures
or built-in shortcut functions.

 How the Code Works:
- The program takes N student marks as input and stores them in a list.
- A for loop is used to process each mark individually.
- Each mark is classified into a performance category based on given rules.
- Using the same loop, the program counts valid students and failed students.
- A final summary is displayed at the end.

 Performance Classification Rules
- 90 – 100 : Excellent
- 75 – 89  : Very Good
- 60 – 74  : Good
- 40 – 59  : Average
- 0 – 39   : Fail
- Less than 0 or greater than 100 : Invalid

Personalization
A personalized condition is added to the program based on my details.
This personalization modifies the program logic/output to ensure originality,
as required by the challenge guidelines.

Files in This Project
- `Day3_Challenge.py` : Contains the Python code for student performance analysis.

 Output
The program displays the performance category for each student mark and
shows a final summary including the total number of valid and failed students.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fcc4ae08-07cf-4fa0-9578-7434b3ba268c" />
## Cyber Activity Risk Analyzer:
## Description
This project analyzes student login activity scores to identify possible
security risks. Each activity score represents the intensity of a login session.
The program processes these scores, categorizes them into different risk levels,
and applies a personalized security rule based on my register number.

## Purpose
The purpose of this project is to understand how basic Python concepts like
lists, for loops, and conditional statements can be used to analyze data.
It also demonstrates how personalization can change the behavior of a program
for different users.

## How the Program Works
- The program takes a list of integer activity scores as input.
- Each score is checked using a for loop.
- If a score is negative, it is treated as invalid and ignored.
- Valid scores are categorized into Low, Medium, High, or Critical risk.
- Separate lists are created to store scores under each category.
- After categorization, a personalized filter is applied based on the
  last digit (D) of my register number.
- The program then displays the final filtered results along with a summary.

## Risk Categorization Rules
- Less than 0 → Invalid (Ignored)
- 0 to 30 → Low Risk
- 31 to 60 → Medium Risk
- 61 to 100 → High Risk
- Above 100 → Critical Risk

## Personalized Security Filter
Let D be the last digit of my register number.

- If D is even:
  Low Risk scores are removed after categorization.
  Only Medium, High, and Critical scores are kept.

- If D is odd:
  Critical Risk scores are removed after categorization.
  Only Low, Medium, and High scores are kept.

The value of D is printed in the output to clearly show how the
program behavior changes based on personalization.

## Additional Features
The program also:
- Counts the total number of valid entries
- Counts the number of ignored (invalid) entries
- Counts how many entries were removed due to personalization
- Displays the final categorized lists after filtering

## Output
At the end, the program shows:
- The value of D
- The categorized risk lists
- The filtered lists after personalization
- A final security summary
## Files in This Project
- `Day4_Challenge.py` : Contains the Python implementation of the Cyber Activity Risk Analyzer.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c12a5be0-380e-4555-a201-7db0ca977c15" />
# Emergency Resource Dispatch Analyzer
## Description
This project simulates an emergency command center analyzing resource
requests during a disaster drill. Each zone submits a request value,
and the system processes these values to identify demand levels,
remove invalid data, and generate a final dispatch report.
## Purpose
The purpose of this project is to practice using lists, for loops,
and conditional statements in Python to analyze data step by step.
It also demonstrates how personalization (PLI) can change the final
output of the program based on individual details.

## How the Program Works
- The program accepts a list of integer resource requests.
- Each request is processed using a for loop.
- Invalid and valid requests are identified.
- Valid requests are categorized into:
  - Low Demand
  - Moderate Demand
  - High Demand
- Separate lists are created for each category.
- A Personalized Logic Index (PLI) is calculated using the
  length of my full name.
- Based on the PLI value, certain categories are removed
  from the final dispatch report.
- The program displays final categorized lists along with
  summary counts.
## Base Classification Rules
- Less than 0 → Invalid Request
- 0 → No Demand
- 1–20 → Low Demand
- 21–50 → Moderate Demand
- Above 50 → High Demand

## Personalized Logic Implementation (PLI)
Let:
L = Length of my full name (excluding spaces)
PLI = L % 3
My Values:
L = 17
PLI =2
Applied Rule:
- If PLI = 0 → Rule A (Remove all Low Demand requests)
- If PLI = 1 → Rule B (Remove all High Demand requests)
- If PLI = 2 → Rule C (Keep only Moderate Demand requests)
The program prints both L and PLI values to clearly show
the applied personalization rule.

## Additional Tracking
The program also:
- Counts total valid requests
- Counts invalid requests
- Counts how many requests were removed due to PLI
- Displays final categorized lists after filtering

## Output
The program displays:
- Length of name (L)
- PLI value
- Applied rule
- Categorized demand lists
- Final filtered lists
- Summary of valid and removed requests
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/90b086e1-48f4-4967-a0eb-84b2d759ee9d" />



