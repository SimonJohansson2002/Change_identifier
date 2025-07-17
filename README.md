# Change_identifier
## Requirements

This project requires the following Python libraries:

- transformers

## Features

The features are:

- Sentiment classification
- Strategy classification
- Structure classification

Each feature will be viewed dynamically and change in classification will be key output. 

### Sentiment classification

The following are the sentiment classes:

    - Strong Positive
    - Moderate Positive
    - Neutral
    - Warning Signs
    - Uncertain
    - Worse Than Expected

If the prompts or model are changed in any way, such as even a single character in the input, the order of messages, the model version (e.g., switching from gpt-4o to gpt-3.5-turbo), or add/remove whitespace in a sensitive context, then the output might change slightly.