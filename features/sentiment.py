import openai
from extract_txt import extract_txt

def sentiment(report_text, api, tables = False):

    # Set your API key here
    openai.api_key = api

    # Construct the prompt
    system_prompt = (
        "You are a financial sentiment classifier. "
        "Classify the given company report excerpt into one of the following categories:\n\n"
        "- Strong Positive: Results are clearly better than expected, strong outlook.\n"
        "- Moderate Positive: Some signs of improvement, but not yet strong.\n"
        "- Neutral: Performance is as expected.\n"
        "- Warning Signs: Business is okay overall, but with some concerns.\n"
        "- Uncertain: Business faces many or significant unknowns or risks.\n"
        "- Worse Than Expected: Results are disappointing or below expectations.\n\n"
        "Reply ONLY with the best-fitting label from the list above."
    )

    # Call the Chat API
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # You can switch to gpt-3.5-turbo if needed
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": report_text}
        ],
        temperature=0  # Deterministic output
    )

    # Output the classification
    classification = response['choices'][0]['message']['content'].strip()
    return classification

if __name__=='__main__':

    text, tables = extract_txt("test_data/VPLAY-B24Q3.pdf")
    
    api = "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"

    q = input('Want to use API? (y/n): ')

    if q == 'y':
        classification = sentiment(text, api)
        print(f"Classification: {classification}")