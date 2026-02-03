from app.model.grammar_model import correct_grammar

def t5_correct(text: str) -> str:
    return correct_grammar(text)
