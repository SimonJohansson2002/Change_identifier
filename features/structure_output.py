from .classifier import classifier
from .extract_txt import extract_txt
import openai

def structure_output(string: str) -> dict:
    """
    Takes output from ChatGPT and returns structured classifications as dictionary.
    
    E.g.
    {
    'Sentiment': {'State': 'Neutral', 'Reason': 'The reason...'},
    'Strategy': {'State': 'Changed', 'Reason': 'The reason...'},
    'Restructuring': {'State': Spinoff, 'Reason': 'The reason...'}
    }

    """
    d = {}
    
    a = string.split('\n\n')

    for i in a:
        if not i:
            continue

        b = i.split('\n')

        c = b[0].split(': ')
        classification = c[0]
        state = c[1]
        reason = b[1].split(': ')[1]
        
        d.update({classification: {'State': state, 'Reason': reason}})
    
    return d

def get_classifications(filename: str, api_key: str) -> str:
    text, tables = extract_txt(filename)

    client = openai.OpenAI(api_key=api_key)
    classification = classifier(client, text)

    return structure_output(classification)


if __name__=='__main__':
    text, tables = extract_txt("test_data/LINDEX25Q2.pdf")
        
    api = "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"

    client = openai.OpenAI(api_key=api)
    classification = classifier(client, text)

    print(structure_output(classification))