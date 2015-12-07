def x(n):
        print "["
        for i in xrange(n):
            print "{"
            print """"fields": {
                            "username": """ + str(i) + ","
            print """
                            "first_name": "Weston",
                            "last_name": "Carvalho",
                            "is_active": true,
                            "is_superuser": false,
                            "is_staff": false,
                            "last_login": "2015-12-05T21:39:28.952Z",
                            "groups": [],
                            "user_permissions": [],
                            "password": "pbkdf2_sha56$20000$6DRc6odWjxq5$iw+XaYW4lKXivaL7luK3EhWpX6Xim6z2wxC+l6MiXFU=",                                                                 "email": "wac@duke.edu",
                            "date_joined": "2015-12-05T21:23:13.588Z"
                        },"""
            print  """
                        "model": "auth.user",
                        "pk": """ + str(i)
            print "},"
        print "]"
x(1000)
