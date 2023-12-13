import re

def process_list(data):
    # Iterate through the list
    for item in data:
        # Iterate through the keys of each dictionary
        for key in item.keys():
            # Check if the value is a string
            if isinstance(item[key], str):
                # Remove non-letter characters from the value
                item[key] = re.sub(r'[^a-zA-Z]', '', item[key])
            # If the value is a list, recursively process it
            elif isinstance(item[key], list):
                process_list(item[key])

# Call the function with the

data = [
    {
        "id": 1,
        "name": "f2ojf1uh29h*1#92810QW(,2@fe3"
    },
    {
        "id": 2,
        "name": "fojfuhhQWfe"
    },
    {
        "id": 3,
        "name": "2e11121eea3dD#21DWD1212eFQW2@fe3",
        "data": [
                    {
                        "guuid": 1,
                        "name": "aaafwfWF#rsffq1rr12r21s,2@fe3",
                    }
                ]
    },
    {
                "guuid": 2,
                "name": "F@FASF32f23f$1212eFQW2@fe3",
                "data": [
                    {
                        "guuid": 1,
                        "name": "f2FDF*&9f2hffq1rr12r21s,2@fe3",
                    },
                    {
                        "guuid": 2,
                        "name": "f2FD!F#!r232321s,2@fe3",
                        "data": [
                            {
                                "guuid": 1,
                                "value": "f2FDF*&34g34g1rr123f,2@fe3",
                            },
                            {
                                "guuid": 2,
                                "value": "f2FD!F#!r232321s,2@fe3",
                            }
                        ]
                    }
                ]
            },
]

process_list(data)

# Print the updated list
print(data)