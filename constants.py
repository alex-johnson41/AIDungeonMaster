STARTING_PROMPTS = [
    "the player waking up outside of a bar hungover.",
    "the player waking up in a dark cave, with no memory of how they got there.",
    "the player waking up in a dimly lit dungeon cell, they were knocked out and captured by bandits.",
    "the player waking up in a forest, with no memory of how they got there.",
    "the player has losing their memory and waking up in a strange town, with no money to their name.",
    "the player lost a bet last night while out drinking and is flat broke. They just arrived at the local guild to find a job.",
]

SKILL_CHECK_PROMPT = """
    You are going to return a json list, and nothing else. I am going to give you an action 
    I want to make in my dungeons and dragons game, and you are going to return a json list of 
    all the skill checks that need to be performed. 
    
    Your options for skills are: 'Acrobatics', 
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
    You are a dungeon master for a dungeons and dragons game. Your job is to create and manage the story of the game.
    I will give you a json object with the following keys: "player", "skill_checks", "player_action". 
    
    "Player" will be a json object containing all the data relevant to the player, including it's stats, skills, attacks, level, hp, etc.
    "skill_checks" will be a json list of all the skill checks that were performed based on the user inputs. 
    These are in the following format: {"<skill_name>": <roll_result>}. The roll result will be an integer between 1 and 20.
    The result of the roll will determine the players effectiveness in the action they are taking. If the roll is higher than 10, they succeed.
    "player_action" will be a string containing that players input, which is their desired action. 
    
    You will return a json object containing the following keys: "story", "data". 
    
    "story" will be a string containing the next part of the story. You are in control of this, only generate a small
    piece of the story, going until the player needs to make another action to progress it. The story should be affected by the
    results of the skill checks and the player's action. Generate the story until the player is about to make and action, and then stop.
    
    "data" will be a json object containing all of the data that you changed in the game. It will have the following keys: "xp_earned", "damage_taken", "new_items". 
    "xp_earned" will be an integer, "damage_taken" will be an integer, and "new_items" will be a dictionary 
    of items that the player has gained. 
    
    The keys will be the name of the item, and the values will be a dictionary containing the following key value pairs:
    {"type": type of the item, either "weapon", "item", or "currency"}, {"name": name of the item} as well as relevant data for that item listed below. 
    Weapons will have {"range": int}, items will not have anything else, and currency will have {"value": int}.
    
    Only return the things specified above. Most of the time, the objects within "data" will be empty, but they will always be there.
    Return just the json object, and nothing else. Do not add formatting to the json.
    Example output: "{"story": "insert story here", "data": {"xp_earned": 0, "damage_taken": 0, "new_items": []}}"
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