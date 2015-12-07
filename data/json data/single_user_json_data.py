from random import randint
def singleUserJsonData():
        print "["
        for i in xrange(300):
            print """ {
                "fields": {
                    "distance":""" + str(randint(0,15)) + """,
                    "user":1,
                    "location": "",
                    "comments": "",
                    "shoe": null,
                    "time": "00:10:00",
                    "date": "2015-""" + str(randint(1,12))+ "-" + str(randint(1,27)) +"""",
                    "conditions": "",
                    "activity_type": "test"
                },
                "model": "log.activity",
                "pk": """+ str(i) + """
            }, """
        print "]"
singleUserJsonData()
