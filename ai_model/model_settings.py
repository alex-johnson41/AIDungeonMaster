SKILL_CHECK_PROMPT = """
    You are going to return a json list, and nothing else. I am going to give you an action 
    I want to make in my dungeons and dragons game, and you are going to return a json list of 
    all the skill checks that need to be performed. Your options for skills are: 'Acrobatics', 
    'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight', 'Intimidation',
    'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion', 'Religion',
    'Sleight of Hand', 'Stealth', 'Survival'.
    Only return the name of the skill, like so: ["Perception", "Stealth", "Arcana"]. 
    Do not add any headers indicating that it is a json list, just return the list.
    This is what your output should look like: "["Perception", "Stealth", "Arcana"]"
    Return an empty list if no skill checks are absoluteley needed.
    Only return a skill if it is absolutely needed for the action.
"""

STORY_PROMPT = """
    You are a dungeon master for a dungeons and dragons game. 
"""

SAFETY_SETTINGS = [
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]