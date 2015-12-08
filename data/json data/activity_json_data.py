from random import randint
def user1_data():
        print "["
        for i in xrange(0,300):
            print """ {
                "fields": {
                    "distance":""" + str(randint(0,25)) + """,
                    "user":1,
                    "location": "",
                    "comments": "",
                    "shoe": null,
                    "time": "00:"""+ str(randint(0,5))+ str(randint(0,9))+ ":"+ str(randint(0,5))+ str(randint(0,9))+"""",
                    "date": "2015-""" + str(randint(1,12))+ "-" + str(randint(1,27)) +"""",
                    "conditions": "",
                    "activity_type": "test"
                },
                "model": "log.activity",
                "pk": """ + str(i)+ """
                },"""
user1_data()

def json_data():
        for i in xrange(300,2300):
            print """ {
                "fields": {
                    "distance":""" + str(randint(0,20)) + """,
                    "user":""" + str(randint(1,999)) + """,
                    "location": "",
                    "comments": "",
                    "shoe": null,
                    "time": "00:"""+ str(randint(0,5))+ str(randint(0,9))+ ":"+ str(randint(0,5))+ str(randint(0,9))+"""",
                    "date": "2015-"""+ str(randint(1,12)) + "-"+ str(randint(1,27)) + """",
                    "conditions": "",
                    "activity_type": "test"
                },
                "model": "log.activity",
                "pk": """+ str(i)
            if i == 2299:
                print "}"
            else:
                print "},"
        print "]"
json_data()
