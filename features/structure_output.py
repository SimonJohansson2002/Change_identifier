from .classifier import classifier
from .extract_txt import extract_txt
from dotenv import load_dotenv
import openai

def structure_output(string: str) -> dict:
    """
    Takes output from ChatGPT and returns structured classifications as one dictionary and another dictionary with reasons.
    
    Input format:
        Summary: <max 250 characters>

        Guidance: <guidance text or 'None'>
        
        Strategy: <'None' or 'Changed'>
        Reason: <brief explanation>
        
        Restructuring:
        Refinancing: <Yes/No>
        Spinoff: <Yes/No>
        Sale: <Yes/No>
        Merger: <Yes/No>
        Major Cost Reduction: <Yes/No>
        Bankruptcy: <Yes/No>
        Unknown: <Yes/No>
        Reason: <brief explanation>

    E.g.
    Classifications=
    {
    'Summary': <max 250 characters>,
    'Guidance': <guidance text or 'None'>
    'Strategy': <'None' or 'Changed'>
    'Refinancing': <Yes/No>
    'Spinoff': <Yes/No>
    'Sale': <Yes/No>
    'Merger': <Yes/No>
    'Major Cost Reduction': <Yes/No>
    'Bankruptcy': <Yes/No>
    'Unknown': <Yes/No>
    }

    Reasons=
    {
    'Strategy': <Reason>,
    'Restructuring': <Reason>
    }

    """
    classification = {}
    reasons = {}

    categories = string.split('\n\n')

    summary = categories[0]
    guidance = categories[1]
    strategy = categories[2]
    restructuring = categories[3]

    summ = summary.split(': ')[1].strip()

    guid = guidance.split(': ')[1].strip()

    strategy_list = strategy.split('Reason: ')
    strat = strategy_list[0].split(': ')[1].strip()
    strat_reason = strategy_list[1].strip()

    restructuring_list = restructuring.split('Reason: ')
    restr_reason = restructuring_list[1].strip()

    restr = restructuring_list[0].split('\n')
    refinancing = restr[1].split(': ')[1].strip()
    spinoff = restr[2].split(': ')[1].strip()
    sale = restr[3].split(': ')[1].strip()
    merger = restr[4].split(': ')[1].strip()
    mcr = restr[5].split(': ')[1].strip()
    bankruptcy = restr[6].split(': ')[1].strip()
    unknown = restr[7].split(': ')[1].strip()
    
    classification.update({'Summary': summ, 'Guidance': guid, 'Strategy': strat, 'Refinancing': refinancing, 'Spin-off': spinoff, 'Sale': sale, 'Merger': merger, 'Major Cost Reduction': mcr, 'Bankruptcy': bankruptcy, 'Other': unknown})
    reasons.update({'Strategy': strat_reason, 'Restructuring': restr_reason})
    
    return classification, reasons

def get_classifications(filename: str, api_key: str) -> str:
    text, tables = extract_txt(filename)

    client = openai.OpenAI(api_key=api_key)
    classification = classifier(client, text)

    return structure_output(classification)


if __name__=='__main__':
    """text, tables = extract_txt("test_data/LINDEX25Q2.pdf")
        
    load_dotenv()
    api = os.getenv("OPENAI_API_KEY")
    
    client = openai.OpenAI(api_key=api)
    classification = classifier(client, text)"""

    with open('classification.txt', 'r', encoding='utf-8') as classification:
        s, r = structure_output(classification.read())

    print(s)
    print("\n", r)