"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 1, 4, 4, 4, "hello", "hello", 4]],
            "answer": [[1,1],[4,4,4],["hello","hello"],[4]]
        },
        {
            "input": [[1, 2, 3, 4]],
            "answer": [[1], [2], [3], [4]]
        },
        {
            "input": [[1]],
            "answer": [[1]],
            "explanation": "5+7=?"
        },
        {
            "input": [[]],
            "answer": [],
            "explanation": "5+7=?"
        }
    ],
    "Extra": [
        {
            "input": [[5, 5, "5", 5, 5]],
            "answer": [[5, 5], ["5"], [5, 5]]
        }
    ]
}
