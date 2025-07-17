import openai
from extract_txt import extract_txt

def sentiment(client, report_text, tables=None):

    # Construct the system prompt
    system_prompt = (
        "You are a financial sentiment classifier. "
        "Classify the given company report excerpt into one of the following categories:\n\n"
        "- Strong Positive: Results are clearly better than expected, strong outlook.\n"
        "- Moderate Positive: Some signs of improvement, but not yet strong.\n"
        "- Neutral: Performance is as expected.\n"
        "- Warning Signs: Business is okay overall, but with some concerns.\n"
        "- Uncertain: Business faces many or significant unknowns or risks.\n"
        "- Worse Than Expected: Results are disappointing or below expectations.\n\n"
        "Reply with the best-fitting label from the list above, followed by a brief explanation of why that label was chosen.\n"
        "One negative comment weighs more than one positive."
    )

    if tables:
        # If tables exist, add an instruction
        system_prompt += (
            "\n\nThe tables have been extracted and attached from the report to help you identify them. "
            "If the rows seem to miss labels, they are probably the same as in the previous table."
        )
        # Append the tables to the user message
        report_text += "\n\n=== Extracted Tables ===\n" + "\n".join(tables)

    # Call the Chat API
    response = client.chat.completions.create(
    model="gpt-4o", #gpt-3.5-turbo
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": report_text}
    ],
    temperature=0
    )

    classification = response.choices[0].message.content.strip()

    return classification

if __name__=='__main__':

    text, tables = extract_txt("test_data/VPLAY-B25Q2.pdf")
    
    api = "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"

    q = input('Want to use API? (y/n): ')

    if q == 'y':
        client = openai.OpenAI(api_key=api)  # You can pass api_key here, or set OPENAI_API_KEY env var
        classification = sentiment(client, text)
        print(f"Classification: {classification}")