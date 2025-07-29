# Change_identifier
## Requirements

This project requires the following Python libraries:
- openai
- pdplumber
- requests
- BeautifulSoup from bs4
- PdfReader from PyPDF2
- BytesIO from io

## Database

Installments:
- MySQL 8.4.6 LTS Installer
- pip install mysql-connector-python

To start/stop the database:
- Win + R
- Enter "services.msc"
- Find and press MySQL84
- Press start/stop

Note: The database does not run automatically when the computer is booted.

Use MySQL in python:
- mydb, mycursor = access_db('password', 'name') if database already exists
- mydb, mycursor = init_db('jfyu_1&ofQnsp1^d6FJ') if it does not exist

Once database is running, mydb and mycursor should exist as a global variable. 

## Features

The features are:
- Sentiment classification
- Strategy classification
- Restructure classification

Each feature will be viewed dynamically and change in classification will be key output. 

### Sentiment classification

The following are the sentiment classes:
    - Positive
    - Potential
    - Neutral
    - Warning Signs
    - Worse Than Expected

If the prompts or model are changed in any way, such as even a single character in the input, the order of messages, the model version (e.g., switching from gpt-4o to gpt-3.5-turbo), or add/remove whitespace in a sensitive context, then the output might change slightly.

### Strategy classification

The following are the strategy classes:
    - Growth
    - Profitability

### Restructure classifier

The following are the restructure classes:
    - None
    - Refinancing
    - Spinoff
    - Sale
    - Merger
    - Major cost reduction
    - Unknown

### Errors
Classifying
- 'Unable to use ChatGPT API' -> Possible reasons are insufficient balance on OpenAI or failing API key.

Scraping
- 'No PDF available' -> No pdf with title "PDF" available for the latest notification in MFN
- 'No pdf:s available' -> No pdf:s with any title available for the latest notification in MFN
- 'Error reading PDF' -> pdf exists but couldn't read it