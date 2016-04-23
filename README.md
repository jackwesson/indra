# Social todo Django starter code

git add . 
git commit 

git push heroku master 

heroku run python manage.py makemigrations

We wrote this in office hours. It defines the models for tasks,
migrations, etc. It is based on the 
[Django tutorial](https://docs.djangoproject.com/en/1.9/intro/).

To install this on c9, clone the repository. Then, before you run it
for the first time, you'd do

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
This installs your Python dependencies. Then you need to run your database
migrations with 

```
python manage.py migrate
```

This will create a file called `db.sqlite3`, which is ignored in your
`.gitignore` file. 

Now you're ready to run the application.Then you can run it with the following

```
python manage.py runserver 0.0.0.0:$PORT
```

<!--Then you can click "Preview" in the c9 interface to see your running application.-->
<!--Off to the races.-->

<!--Downloading/unpacking python-apt==0.9.3.5ubuntu2 (from -r requirements.txt (line 63))-->
<!--  Could not find a version that satisfies the requirement python-apt==0.9.3.5ubuntu2 (from -r requirements.txt (line 63)) (from versions: 0.0.0, 0.7.8)-->
<!--Cleaning up...-->
<!--No distributions matching the version for python-apt==0.9.3.5ubuntu2 (from -r requirements.txt (line 63))-->
<!--Traceback (most recent call last):-->
<!--  File "/home/ubuntu/workspace/env/bin/pip", line 11, in <module>-->
<!--    sys.exit(main())-->
<!--  File "/home/ubuntu/workspace/env/local/lib/python2.7/site-packages/pip/__init__.py", line 185, in main-->
<!--    return command.main(cmd_args)-->
<!--  File "/home/ubuntu/workspace/env/local/lib/python2.7/site-packages/pip/basecommand.py", line 161, in main-->
<!--    text = '\n'.join(complete_log)-->
<!--UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 72: ordinal not in range(128)-->
