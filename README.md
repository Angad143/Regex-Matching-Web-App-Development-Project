# Regex Matching Web App Development Project

This project is a web application inspired by [regex101.com](https://regex101.com), designed to provide core functionality for regex pattern matching and email validation. The application allows users to input a test string along with a regular expression (regex) and returns all matches found. Additionally, the app features an email validation tool to check the format of a given email address.

## Features
- **Regex Matcher**: Users can input a test string and a regex pattern to identify all matches within the string.
- **Email Validator**: A tool to check if a given email address is valid based on standard email formats.
- **Flask-Based**: The app is built using the Flask web framework for easy web deployment and routing.
- **Responsive UI**: Includes a user-friendly interface with HTML, CSS, and JavaScript for a smooth user experience.
  
## Project Structure
```
Regex-Matching-Web-App-Project/
│
├── app.py                        # The core Python application file
├── static/
│   ├── css/
│   │   └── style.css              # Custom styling for the web app
│   └── js/
│       └── script.js              # JavaScript for additional functionality
└── templates/
    ├── index.html                 # Homepage with regex and email validation form
    ├── results.html               # Page displaying regex matches
    └── email_validator.html       # Page displaying email validation results
```

## How It Works

### Regex Matcher:
1. Users enter a **test string** and a **regex pattern**.
2. On submission, the app processes the input using Python’s built-in `re` module to find matches.
3. The results are then displayed on a separate page (`results.html`), showing all the matches found.

### Email Validator:
1. Users can validate an email by inputting it into the designated field.
2. The app checks if the email follows a valid format.
3. The result is displayed as either "Valid Email" or "Invalid Email" on `email_validator.html`.

## Technologies Used
- **Flask**: For building the web application and managing routes.
- **HTML/CSS**: For the structure and styling of the web pages.
- **JavaScript**: For alert functionality.
- **Regex (re module)**: For matching patterns and validating input strings.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/regex-matching-web-app.git
   cd regex-matching-web-app
   ```

2. Install the dependencies:
   ```bash
   pip install Flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open a web browser and go to `http://localhost:5000`.

## Usage
1. Enter a **regex pattern** and a **test string** in the "Regex Matcher" section.
2. Click **Match Regex** to view the results.
3. For email validation, input an email in the **Email Validator** section and click **Validate Email**.

## Future Enhancements
- **Regex Explanation Tool**: Provide a description of what each regex pattern does.
- **Detailed Match Results**: Show match positions and groups.
- **Deployment**: Deploy the app on AWS or other cloud services for wider accessibility.


