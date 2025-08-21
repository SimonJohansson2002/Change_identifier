# Change_identifier
## Requirements

This project requires the following Python libraries:
- openai
- pdplumber
- requests
- mysql.connector
- BeautifulSoup from bs4
- PdfReader from PyPDF2
- BytesIO from io
- Flask

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
- mydb, mycursor = init_db('password') if it does not exist

Once database is running, mydb and mycursor should exist as a global variable. 

## Features

The features are:
- Summary
- Guidance
- Strategy classification
- Restructure classification

- Sentiment classification

Each feature will be viewed dynamically and change in classification will be key output. 

### Summary

A summary of the company's key highlights, accomplishments, and challenges is generated. Maximum 250 characters. 

### Guidance

The company's financial guidance is extracted if it exists. 

### Strategy classification

The following are the strategy classes:
- None
- Changed

### Restructure classifier

The following are the restructure classes:
- Refinancing
- Spinoff
- Sale
- Merger
- Major cost reduction
- Bankruptcies
- Unknown

### Sentiment classification

THIS WILL BE CHANGED

The following are the sentiment classes:
- Positive
- Potential
- Neutral
- Warning Signs
- Worse Than Expected

If the prompts or model are changed in any way, such as even a single character in the input, the order of messages, the model version (e.g., switching from gpt-4o to gpt-3.5-turbo), or add/remove whitespace in a sensitive context, then the output might change slightly.

### Website

Redirecting:
- code 302: default and tells the browser not to cache the redirection (not to mix up with information on the page)
- code 301: tells the browser to cache the new URL to a web page, e.g. if a page is moved from /old_url to /new_url in a website 
restructuring. This would make the user being redirected to /new_url even if the /old_url is entered. 

### Errors
Classifying
- 'Unable to use ChatGPT API' -> Possible reasons are insufficient balance on OpenAI or failing API key.

Scraping
- 'No PDF available' -> No pdf with title "PDF" available for the latest notification in MFN
- 'No pdf:s available' -> No pdf:s with any title available for the latest notification in MFN
- 'Error reading PDF' -> pdf exists but couldn't read it

