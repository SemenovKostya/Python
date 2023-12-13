import re

def function(data):
    for item in data:
        for key in item.keys():
            if isinstance(item[key], str):
                item[key] = re.sub(r'[^a-zA-Z]', '', item[key])
            elif isinstance(item[key], list):
                function(item[key])
            elif isinstance(item[key], dict):
                a = item[key]
                for key,value in a.items():
                    if isinstance(value,int):
                        a[key] = value 
                    else: 
                        value_without_digits = re.sub(r'\d', '', value)
                        a[key] = value_without_digits
            elif isinstance(item[key], int):
                a = item[key]

data = [
    {
        "guuid": 1,
        "name": "f2ojf1uhd12da3#QW(,2@fe3",
        "data": [
            {
                "guuid": 1,
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
            {
                "guuid": 3,
                "name": "2e11eea3dD$#%%#DWD1212eFQW2@fe3",
                "data": [
                    {
                        "guuid": 1,
                        "name": "f2FD!F#!23f3344T@e@r21s,2@fe3",
                    }
                ]
            }
        ]
    },
    {
        "guuid": 2,
        "name": "f2ojf1uh234g0Q1W(,2@fe3",
        "data": [
            {
                "guuid": 1,
                "name": "2e11e34g212eFQW2@fe3",
                "data": [
                    {
                        "guuid": 1,
                        "name": "f2FD!F!R@F@#F@#Fr21s,2@fe3",
                        "data": [
                            {
                                "guuid": 1,
                                "name": "f2FD!F#!Q@#!@23f12r21s,2@fe3",
                            }
                        ]
                    }
                ]
            },
            {
                "guuid": 2,
                "name": "2e11eea3dg43gW2@fe3",
                "data": [
                    {
                        "guuid": 1,
                        "name": "f2Fg43g3sffq1rr12r21s,2@fe3",
                    },
                    {
                        "guuid": 2,
                        "name": "fg43g$@GGG@ffq1rr12r21s,2@fe3",
                    }
                ]
            },
            {
                "guuid": 3,
                "name": "2e11eea3dD$#%%#DWD1212eFQW2@fe3",
                "data": [
                    {
                        "guuid": 1,
                        "name": "f2FD!F#!Q@#!@!@rrasffq1rr12r21s,2@fe3",
                    }
                ]
            }
        ]
    },
    {
        "guuid": 3,
        "name": "f2ojf1uh29h*#92810Q1W(,2@fe3",
        "data": [
            {
                "guuid": 1,
                "name": "2e11eea3dD#DWD1212eFQW2@fe3",
                "data":
                    {
                        "guuid": 1,
                        "name": "f2FD!F!R@$#!rrasffq1rr12r21s,2@fe3",
                        "datagram": "test1723617351735172317",
                    }

            },
            {
                "guuid": 2,
                "name": "2e11eea3dD#DWD1212eFQW2@fe3",
                "data": [
                    {
                        "guuid": 1,
                        "name": "f2FD!F#!rrasffq1rr12r21s,2@fe3",
                    },
                    {
                        "guuid": 2,
                        "name": "f2FD!F#!rrasffq1rr12r21s,2@fe3",
                    }
                ]
            },
            {
                "guuid": 3,
                "name": "2e11eea3dD$#%%#DWD1212eFQW2@fe3",
                "data": [
                    {
                        "guuid": 1,
                        "name": "f2FD!F#!Q@#!@!@rrasffq1rr12r21s,2@fe3",
                    }
                ]
            }
        ]
    }
]
function(data)
print(data)

