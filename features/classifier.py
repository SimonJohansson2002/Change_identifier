import openai
from .extract_txt import extract_txt

def classifier(client: openai.OpenAI, report_text: str, tables: list=None) -> str:
    """
    Classifies sentiment of the text, identifies if there is a change in strategy, and if there is any kind of restructuring. 

    Args:
        client (openai.OpenAI): openai client with api key
        report_text (str): text to be analyzed
        tables (list, optional): list of tables from the text to help ChatGPT understand what content are tables. Defaults to None.

    Returns:
        str: output from ChatGPT. If error occurs with the client, 'Unable to get response from ChatGPT API' is returned
    """
    # Construct the system prompt
    system_prompt = (
        "You are a financial analyst AI. Given a company report excerpt, classify it from three perspectives. "
        "Use only the EXACT labels provided below and follow the exact output format.\n\n"

        "### Summary ###\n"
        "Summarize the text briefly (max 250 characters). Focus on the company's key highlights, achievements, and challenges. Be concise and factual.\n\n"

        "### Guidance ###\n"
        "Extract the company's financial guidance if mentioned. If no guidance is provided, return exactly 'None'.\n\n"

        "### Strategy Change Classification ###\n"
        "Pick ONE of the following labels: 'None', 'Changed'.\n"
        "- None: No clear or significant change in strategy or targets.\n"
        "- Changed: There is a major shift in strategy, direction, or company targets (e.g., new business model, sharp pivot, market exit/entry, etc.).\n"
        "Only use one label exactly as written. Then briefly explain your reasoning.\n\n"

       "### Restructuring Classification ###\n"
        "For EACH of the following restructuring types, answer 'Yes' or 'No':\n"
        "- Refinancing: New capital or debt taken primarily to stabilize operations (not for growth investment).\n"
        "- Spinoff: A subsidiary is being separated to be listed independently.\n"
        "- Sale: A subsidiary, asset, or business unit is being sold.\n"
        "- Merger: A full merger with another company (exclude acquisitions).\n"
        "- Major Cost Reduction: A clearly impactful cost-cutting measure beyond routine efficiencies.\n"
        "- Bankruptcy: Bankruptcy is being discussed or has been decided.\n"
        "- Unknown: Restructuring is mentioned, but the form is unclear.\n"
        "Provide a Yes/No for each type. Then explain your reasoning.\n\n"

        "### Output Format (Strict) ###\n"
        "Summary: <max 250 characters>\n\n"
        "Guidance: <guidance text or 'None'>\n\n"
        "Strategy: <'None' or 'Changed'>\n"
        "Reason: <brief explanation>\n\n"
        "Restructuring:\n"
        "Refinancing: <Yes/No>\n"
        "Spinoff: <Yes/No>\n"
        "Sale: <Yes/No>\n"
        "Merger: <Yes/No>\n"
        "Major Cost Reduction: <Yes/No>\n"
        "Bankruptcy: <Yes/No>\n"
        "Unknown: <Yes/No>\n"
        "Reason: <brief explanation>"

        "Do not include any other text outside of the required format."
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
    try: 
        response = client.chat.completions.create(
        model="gpt-3.5-turbo", #gpt-3.5-turbo gpt-4o
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": report_text}
        ],
        temperature=0
        )

        classification = response.choices[0].message.content.strip()
    
    except: 
        classification = 'Unable to get response from ChatGPT API'

    return classification

if __name__=='__main__':
    text, tables = extract_txt("test_data/LINDEX25Q2.pdf")
    
    api = "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"

    client = openai.OpenAI(api_key=api)
    classification = classifier(client, text)
    print(classification)
    with open("classification.txt", "w", encoding='utf-8') as f:
        f.write(classification)