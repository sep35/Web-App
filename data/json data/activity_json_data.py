from random import randint
def json_data(n):
        print "["
        for i in xrange(2000):
            print """ {
                "fields": {
                    "distance":""" + str(randint(0,15)) + """,
                    "user":""" + str(randint(1,999)) + """,
                    "location": "",
                    "comments": "",
                    "shoe": null,
                    "time": "00:10:00",
                    "date": "2015-12-07",
                    "conditions": "",
                    "activity_type": "test"
                },
                "model": "log.activity",
                "pk": """+ str(i) + """
            }, """
        print "]"
json_data()
