# Change_identifier
## Requirements

This project requires the following Python libraries:

- openai
- pdplumber

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