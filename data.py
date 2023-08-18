import requests

response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
response.raise_for_status()
data = response.json()

question_data = data["results"]
#    {
#        "category": "Science: Computers",
#        "type": "boolean",
#        "difficulty": "medium",
#        "question": "The HTML5 standard was published in 2014.",
#        "correct_answer": "True",
#        "incorrect_answers": [
#            "False"
#        ]
#    },
