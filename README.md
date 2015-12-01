##Run and Setup on Duke VM w/Vagrant##

### Required Packages ###
- django-tables2 --> from vm run `sudo pip install django-tables2`
- django_chartit --> from vm run `sudo pip install django_chartit`
  - Also have to edit /chartit/templatetags/chartit.py
    ```
    -from django.utils import simplejson
    +import simplejson
    ```

### Setup ###
1. Run vagrant up then ssh into the vm in your terminal
2. Navigate into /316-Project/Running_log/
3. If you haven't, you must initiate the database by running
  - `dropdb log; createdb log; psql log -af schemas/log-schema.sql`
4. Update and migrate the app files
  - `python manage.py syncdb`
  - `python manage.py makemigrations log`
5. Run the local host server of your VM
  - `python manage.py runserver`
  - port 8000 is the default, so if you open the VirtualBox VM you should just have to go to localhost:8000 on a web browser
