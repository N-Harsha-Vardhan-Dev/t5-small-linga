from transformers import T5Tokenizer, T5ForConditionalGeneration

MODEL_NAME = "Harshathemonster/t5-small-updated"

tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)

def correct_grammar(text: str):
    input_text = "grammar: " + text
    tokens = tokenizer(input_text, return_tensors="pt", truncation=True)
    outputs = model.generate(**tokens, max_length=128)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
