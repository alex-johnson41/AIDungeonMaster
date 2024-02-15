from ai_model.gemini_model import GeminiModel

"""" 
Random notes:
    Create two instances of the model, one for creating the story,
        and one for analyzing user inputs to determine if any dice rolls are needed for that action.
    
"""


model = GeminiModel()
while True:
    prompt = input("Enter a prompt:")
    response = model.communicate(prompt)
    print(response)