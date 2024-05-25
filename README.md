# Imam Mahdi Challenge
Imam mahdi challenge is a cultural competition about Imam Mahdi and  his biography with some information about him. It's a webapp made up with python using Flask API.
It uses python to apply sort of competiton by asking questions of different types and then gives its correction with a score, with the ability of the admin of the website to edit the questions and the content of the website.
## Used Languages
### Python
In order to run the Flask API. Its the language that hold the backend and the logic within it.
#### Imported Libraries
1 - Flask: To run the flask API.
2 - os: To make actions within the system.
3  - sqlalchemy: for dealing with database.
4 - validate_email: To make an vaalidation for an email provided.
5 - werkzeug: For generating hashes and check it for passwords of admins.
6 - functools: To make login_required function
7 - random: To select random questions from database with random order.
8 - spacy: To compare the answers using ai.
### Sqlite3
In order to deal with the database or editing it. The database are in file called 'coltar.db' in which it consist of 5 tables:
1 - Users: In which it's stores the users on this website. It contains an unique id, the user's name, his email, his type (user or admin). And if he is an admin then an admin's password.
2 - Info: In which it stores the part marked as "seperated info" in information page. The table contains an id and the info itself.
3 - Questions: It stores the one choice questions. It stores the question's id, the question itself, 'f1', 'f2', 'f3' as 3 false answers, and 't' the true answer.
4 - multiple_choice: Where the multiple choice questions are stored in which the question's id, the question itself, 'f1', 'f2', 'f3' as 3 false answers, and 't1' and 't2' as 2 true answers.
5 - qt: The questions of text type, in where there's id, the question and the answer.
### Frontend Languages (HTML, CSS, JS)
To create the website's structure. It was made it to be simple and beautiful.
Bootstrap was also imported and used to enhance the experience.
#### HTML templates
1 - 404.html
2 - 500.html
3 - admin.html
4 - index.html
5 - info.html
6 - layout.html
7 - log.html
8 - scores.html
9 - test.html
#### CSS Sheet
1 - style.css
#### js code
1 - mahdi.js
## Pages
### Homepage
Due to the using of Arabic language, the
It contains an introduction about the competition with its laws, then a "start" button to scroll down to a form in which you put a name and email. The form handles several error cases, as repetition of username and invalid emails.
![screenshot](/static/img/scrn/h1.png)
![screenshot](/static/img/scrn/h2.png)
### Information Page
In which it carries the information that you will be tested in, with a timer that when it ends, it’ll get you automatically to the test page,
![screenshot](/static/img/scrn/i1.png)
or you can press the button below to get it.
![screenshot](/static/img/scrn/i2.png)
Some of the information are built in where they cant be edited. But You can add an information if you're an admin.
Once you leave the the information page you cant go back to it until you'll complete the test.
### Test Page
you are gonna be tested in questions of 3 different types:
1 – One Choice Question: You choose only one choice in which answers are ordered randomly using shuffle method in python. This type Worths 1 point.
![screenshot](/static/img/scrn/t2.png)
2 – Multiple Choice Question: You could choose more than one answer. Also here, answers are ordered randomly. This type Worths 2 points for 2 true answers and -1 point for each false answer.
![screenshot](/static/img/scrn/t3.png)
3 – Text Question: You type answer in text field in which it’ll be compared to true answer stored in database using ai using "spacy" library. This type Worths 3 points.
![screenshot](/static/img/scrn/t4.png)
Note: Because of the using of Arabic language, the comparision of terms using spacy might not be 100% correct.
The python code handles the cases of void input, and stores the questions and its squence of answers to be displayed in the scores page with correction.
### Scores Page
In which you’ll be given your score with a correction for your answers.
The score is out of 14, If the score is greater than 13 then its "Excellent".
elif the score is greater than 10 then its "Very Good".
elif the score is greater than 7 then its "Good".
elif the score is greater than 4 then its "Normal".
else then its "Bad".
In multiple choice and one choice question, the answers are displayed to the user in the same order it was shown in the test page with correction to it.
![screenshot](/static/img/scrn/s1.png)
![screenshot](/static/img/scrn/s2.png)
![screenshot](/static/img/scrn/s3.png)
![screenshot](/static/img/scrn/s4.png)
### Administration
You can access admin page through entering an admin's email in email's field, then you'll be redirected to login page in will the user will enter his admin's password.
![screenshot](/static/img/scrn/l1.png)
You can:
1 – Add an admin with an email and password, in order to give him access to this page.
![screenshot](/static/img/scrn/a1.png)
2 – Add a Question: You choose the question’s type in a select tag then the type'll be displayed on the screen then insert it to be added to database.
![screenshot](/static/img/scrn/a3.png)
3 – Add an information that you want it to be displayed in the information page.
You can edit the database through administration. It holdes several error cases that would happen.
![screenshot](/static/img/scrn/a2.png)
## Error Handlers
1 - 404 Error: The website contains an handler for 404 error in which it renders an page that indicates that "Page wasnt Found".
2 - 500 Error: The website contains an handler for 500 error in which it renders an page that indicates "Internal Server Error".
## Images
Images used in the website.
![background](/static/img/backg2.jpg)
![image for imam](/static/img/backg.jpg)
## Links
#### Video Demo: [Imam Mahdi Challenge](https://www.youtube.com/watch?v=qsWhXPoR6qY&feature=youtu.be)
#### Website Link : [Imam-mahdi-challenge](https://www.imam-mahdi-challenge.onrender.com)
# Imam Mahdi Challenge
Imam mahdi challenge is a cultural competition about Imam Mahdi and  his biography with some information about him. It's a webapp made up with python using Flask API.
It uses python to apply sort of competiton by asking questions of different types and then gives its correction with a score, with the ability of the admin of the website to edit the questions and the content of the website.
## Used Languages
### Python
In order to run the Flask API. Its the language that hold the backend and the logic within it.
#### Imported Libraries
1 - Flask: To run the flask API.
2 - os: To make actions within the system.
3  - sqlalchemy: for dealing with database.
4 - validate_email: To make an vaalidation for an email provided.
5 - werkzeug: For generating hashes and check it for passwords of admins.
6 - functools: To make login_required function
7 - random: To select random questions from database with random order.
8 - spacy: To compare the answers using ai.
### Sqlite3
In order to deal with the database or editing it. The database are in file called 'coltar.db' in which it consist of 5 tables:
1 - Users: In which it's stores the users on this website. It contains an unique id, the user's name, his email, his type (user or admin). And if he is an admin then an admin's password.
2 - Info: In which it stores the part marked as "seperated info" in information page. The table contains an id and the info itself.
3 - Questions: It stores the one choice questions. It stores the question's id, the question itself, 'f1', 'f2', 'f3' as 3 false answers, and 't' the true answer.
4 - multiple_choice: Where the multiple choice questions are stored in which the question's id, the question itself, 'f1', 'f2', 'f3' as 3 false answers, and 't1' and 't2' as 2 true answers.
5 - qt: The questions of text type, in where there's id, the question and the answer.
### Frontend Languages (HTML, CSS, JS)
To create the website's structure. It was made it to be simple and beautiful.
Bootstrap was also imported and used to enhance the experience.
#### HTML templates
1 - 404.html
2 - 500.html
3 - admin.html
4 - index.html
5 - info.html
6 - layout.html
7 - log.html
8 - scores.html
9 - test.html
#### CSS Sheet
1 - style.css
#### js code
1 - mahdi.js
## Pages
### Homepage
Due to the using of Arabic language, the
It contains an introduction about the competition with its laws, then a "start" button to scroll down to a form in which you put a name and email. The form handles several error cases, as repetition of username and invalid emails.
![screenshot](/static/img/scrn/h1.png)
![screenshot](/static/img/scrn/h2.png)
### Information Page
In which it carries the information that you will be tested in, with a timer that when it ends, it’ll get you automatically to the test page,
![screenshot](/static/img/scrn/i1.png)
or you can press the button below to get it.
![screenshot](/static/img/scrn/i2.png)
Some of the information are built in where they cant be edited. But You can add an information if you're an admin.
Once you leave the the information page you cant go back to it until you'll complete the test.
### Test Page
you are gonna be tested in questions of 3 different types:
1 – One Choice Question: You choose only one choice in which answers are ordered randomly using shuffle method in python. This type Worths 1 point.
![screenshot](/static/img/scrn/t2.png)
2 – Multiple Choice Question: You could choose more than one answer. Also here, answers are ordered randomly. This type Worths 2 points for 2 true answers and -1 point for each false answer.
![screenshot](/static/img/scrn/t3.png)
3 – Text Question: You type answer in text field in which it’ll be compared to true answer stored in database using ai using "spacy" library. This type Worths 3 points.
![screenshot](/static/img/scrn/t4.png)
Note: Because of the using of Arabic language, the comparision of terms using spacy might not be 100% correct.
The python code handles the cases of void input, and stores the questions and its squence of answers to be displayed in the scores page with correction.
### Scores Page
In which you’ll be given your score with a correction for your answers.
The score is out of 14, If the score is greater than 13 then its "Excellent".
elif the score is greater than 10 then its "Very Good".
elif the score is greater than 7 then its "Good".
elif the score is greater than 4 then its "Normal".
else then its "Bad".
In multiple choice and one choice question, the answers are displayed to the user in the same order it was shown in the test page with correction to it.
![screenshot](/static/img/scrn/s1.png)
![screenshot](/static/img/scrn/s2.png)
![screenshot](/static/img/scrn/s3.png)
![screenshot](/static/img/scrn/s4.png)
### Administration
You can access admin page through entering an admin's email in email's field, then you'll be redirected to login page in will the user will enter his admin's password.
![screenshot](/static/img/scrn/l1.png)
You can:
1 – Add an admin with an email and password, in order to give him access to this page.
![screenshot](/static/img/scrn/a1.png)
2 – Add a Question: You choose the question’s type in a select tag then the type'll be displayed on the screen then insert it to be added to database.
![screenshot](/static/img/scrn/a3.png)
3 – Add an information that you want it to be displayed in the information page.
You can edit the database through administration. It holdes several error cases that would happen.
![screenshot](/static/img/scrn/a2.png)
## Error Handlers
1 - 404 Error: The website contains an handler for 404 error in which it renders an page that indicates that "Page wasnt Found".
2 - 500 Error: The website contains an handler for 500 error in which it renders an page that indicates "Internal Server Error".
## Images
Images used in the website.
![background](/static/img/backg2.jpg)
![image for imam](/static/img/backg.jpg)
## Links
#### Video Demo: [Imam Mahdi Challenge](https://www.youtube.com/watch?v=qsWhXPoR6qY&feature=youtu.be)
#### Website Link : [Imam-mahdi-challenge](https://www.imam-mahdi-challenge.onrender.com)
