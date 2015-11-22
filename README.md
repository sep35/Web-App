Run and Setup on Duke VM w/Vagrant

1. Run vagrant up then ssh into the vm in your terminal
2. Navigate into /316-Project/Running_log/
3. If you haven't, you must initiate the database by running
  - run
4. Update and migrate the app files
  - python manage.py syncdb
  - pytohn manage.py makemigrations log
5. Run the local host server of your VM
  - python manage.py runserver
  - port 8000 is the default, so if you open the VirtualBox VM you should just have to go to localhost:8000 on a web browser
