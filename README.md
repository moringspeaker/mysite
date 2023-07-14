#  Chenyu's Personal Website
![visitors](https://visitor-badge.laobi.icu/badge?page_id=moringspeaker.visitor-badge) ![Static Badge](https://img.shields.io/badge/python-3.8-blue) [![npm](https://img.shields.io/npm/v/vue.svg)](https://www.npmjs.com/package/vue)

![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

 ---
> Welcome to my secret space! :blush: Here are my techblogs and life lessons, and of course, some really cool stuff waiting for you to explore! :sunglasses:


### Go to [My Site](http://164.90.253.90:80)

This project builds a personal webiste which supports a **fully CI/CD method**. Easy and comfortable deployment by using two docker containers on the front and backend For my frontend part, I choose [Vue3](https://github.com/vuejs/core) as my frontend framework. For my backend part, I choose to use [Django](https://github.com/django/django) with [Mysql](https://www.mysql.com/) to implemente backend functionalities.


---
# Features

This site support a markdown file blog reading and writing
![Imgur](https://i.imgur.com/5TFPNag.png)

---
# Setup
To run this project, you need to runboth frontend and back-nd, as well as the database to make sure this project works.

### Frontend
First add a ==.env== file under forntend/myfront directory:
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
