#  Chenyu's Personal Website
![visitors](https://visitor-badge.laobi.icu/badge?page_id=moringspeaker.visitor-badge) ![Static Badge](https://img.shields.io/badge/python-3.8-blue) [![npm](https://img.shields.io/npm/v/vue.svg)](https://www.npmjs.com/package/vue)

![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

 ---
## Welcome to my secret space! :blush: 
Here are my tech blogs and life sharing, and of course, some really cool stuff waiting for you to explore! :sunglasses:

[GitHub Repo:](https://github.com/moringspeaker/mysite)

This project builds a personal website which supports a ==fully CI/CD method==. Easy and comfortable deployment by using two docker containers on the front and backend For my frontend part, I choose [Vue3](https://github.com/vuejs/core) as my frontend framework. For my backend part, I choose to use [Django](https://github.com/django/django) with [Mysql](https://www.mysql.com/) to implemente backend functionalities.


---
# Introduction
In this site, you can see:
- ### My Blogs 
   
Blogs with different collections and tags, each collection has its own category:

![imgur](https://i.imgur.com/eLrTbFr.png "Blogs navigation bar")

And on the right side there's a realtime TOC(Table of Content) to highlight the reading header, By clicking the header you want to go to, you can quickly jump to the corresponding chapter:
![imgur](https://i.imgur.com/oTI4xZB.png)

- ### My Info 
    My CV and other personal information, please feel free to contact me for any cool and meaningful ideas that you want to share with me
- ### My Info
    This is the part I plan to put my academic achievements and publications, but for now it's empty... :sob: :sob: :sob:
- ### My Resources
    I put some really cool and helpful websites or programming tools here. Also, I'm considering adding some fun movies or books here.
- ### My Gallery:
  I'm going to make this into a photo album documenting my life, and maybe I'll add some interesting memes in the future... :think:
- ### Login:
    It's totally a meaningless for visitors... I created it just for adding and editing my website's contents more convenient, of course, feel free to dispose of my site if you can guess my login password and account number LOL. :sweat_smile:


---
# Setup
To run this project, you need to run both frontend and back-nd, as well as the database to make sure this project works.

### Frontend
First add a ==.env== file under frontend/myfront directory:
```shell
cd frontend/myfront/
vim .env
```
Your ==.env== file should be like this:
```
VUE_APP_API_KEY=""
VUE_APP_BACKEND_URL=http://localhost:8000/
```
Then run following commands:
```shell
npm install
npm run serve
```

### Backend
First let's add a ==.env== file under backend/mysite direcotry as well:
```shell
cd backend/mysite/
vim .env
```
Your backend ==.env== file should be like this:
```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=3306
SECRET_KEY=''
```
Then run following commands:
```shell
cd ..
pip install -r requirements.txt
cd backend/mysite/
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Don't forget to run your Mysql database at the same time!**

Then you can visit http://localhost:8080/ to see this project! :smile:

### Deployment

You need to setup this project's github workflow file, adding corresponding git repo secrets. Once you're done, the git action will automatically build dockers and deploy it to a given sever. 
