# education-friendly-portal
Django version:3.1.4
Python version:3.7.0

Features-
There is a login page which contains two buttons- 1)Login(if student already have an account) 2)Sign up(for new student registration).  

Credentials for student login- Username-tanmay1022, Password-1234

After login by student will be home page which contains navigation bar and three buttons named as- 
a)Book your slot: This button is used to setup live meeting with teacher for doubt solving. After clicking on "Book your slot" button, the form will be open which having basic details like Student name,Parent name,Date and time,etc. Just fill the details and click on submit, you will get confirmation message.

b)Quick revision: This button is used to revised the basic concepts of topic with short interval of time. By using this section student can clear his/her small doubts within short time. Just select the subject and topic and click on "submit" button, the information will come up in the tabular form.  

c)Video links: This button is used for clearing the doubts using videos. Just select the subject and topic and click on "submit", the video links will come up in the tabular form.


There is a "Home" button in the navigation bar to open home page directly and "Logout" button is used to logout from account and open login page directly.


There are different login credentials for teacher.
Credentials for teacher login- Username-admin, Password-messi1022

After filling up these credentials teacher can see the meeting details of students and accordingly teacher can personally take a virtual meeting and this will help student to clear the doubts.

Database information:
Here MySQL database is used to store data.
Database name-student
Table names-1)studentdoubts_account: This table is used to store the information of student who wants to take a meeting with teacher.
2)studentdoubts_contents: This table is used to store the detail information of topic which student can easily revised.
3)auth_user: This table is used to store the details of newly register student. 

Database credentials are in "settings.py" file.

Thank you!

