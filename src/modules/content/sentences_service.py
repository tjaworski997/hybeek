import spacy

nlp = spacy.load('pl_core_news_md')


def get_sentences_from_content(text):
    doc = nlp(text)
    sentences = list(doc.sents)

    result = []
    for s in sentences:
        result.append(s.text)

    return result
