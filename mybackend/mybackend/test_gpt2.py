from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Load pre-trained model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Encode text input
input_text = "Hello, my name is GPT-2. How can I assist you today?"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate a sample output
output = model.generate(input_ids, max_length=50)

# Decode the generated text
decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

print(decoded_output)
