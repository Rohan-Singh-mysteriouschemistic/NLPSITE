import nlpcloud

token = "6685a8255c786827b96c3ab9c0cac04b8ae8d836" #write your own api key here

def Code(prompt):
    client = nlpcloud.Client("finetuned-llama-3-70b", token, gpu=True)
    response = client.code_generation(prompt)
    pseudocode = response.get('generated_code')
    explanation = response.get('explanation')
    if pseudocode and explanation:
        return f"{pseudocode}\n\n### Explanation:\n{explanation}"
    elif pseudocode:
        return pseudocode
    elif explanation:
        return f"### Explanation:\n{explanation}"
    else:
        return str(response)

def Grammar(prompt):
    client = nlpcloud.Client("finetuned-llama-3-70b", token, gpu=True)
    response=client.gs_correction(prompt)
    return response

def NER(prompt, entity):
    client = nlpcloud.Client("finetuned-llama-3-70b", token, gpu=True)
    response = client.entities(prompt, searched_entity=entity)
    entities = response.get('entities')
    if entities:
        return [(e['text'], e['type']) for e in entities]
    else:
        return str(response)


def Sentiment(prompt):
    client = nlpcloud.Client("finetuned-llama-3-70b", token, gpu=True)
    response = client.sentiment(prompt, target="NLP Cloud")
    scored_labels = response.get('scored_labels')
    if scored_labels:
        formatted = [f"Sentiment: {label['label']} | Percentage: {label['score']*100}" for label in scored_labels]
        return "\n".join(formatted)
    else:
        return str(response)
