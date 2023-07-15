#  尘语的个人网站
![visitors](https://visitor-badge.laobi.icu/badge?page_id=moringspeaker.visitor-badge) ![Static Badge](https://img.shields.io/badge/python-3.8-blue) [![npm](https://img.shields.io/npm/v/vue.svg)](https://www.npmjs.com/package/vue)

![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

 ---
## 欢迎来到我的秘密空间！ :blush:
这里有我的一些技术博客和生活分享，当然还有一些很酷的东西等着你去探索！ :sunglasses:

[GitHub Repo:](https://github.com/moringspeaker/mysite)

本项目构建了一个支持==完全CI/CD方法==的个人网站。 通过在前端和后端使用两个docker容器，可以轻松自如地进行部署。前端部分，我选择了[Vue3](https://github.com/vuejs/core)作为我的前端框架。后台部分，我选择使用[Django](https://github.com/django/django)和[Mysql](https://www.mysql.com/)来实现后台功能。

---
# 网站简介
在这个网站，你可以看到：
- ### 我的博客

有着不同分类和tag的博客，其中有些博客会以合集的形式放到下方 Blog Collection中，当然它们也会有各自的分类：

![imgur](https://i.imgur.com/eLrTbFr.png "Blogs navigation bar")

并且在右边有一个实时的内容树（TOC），其中您正在阅读的部分会被高亮显示，同时，您也可以通过点击对应的章节名跳转到对应的章节：
![imgur](https://i.imgur.com/oTI4xZB.png)

- ### My Info
  我的 CV 以及其他的一些个人信息， 如果您有任何有趣、有意义的想法，欢迎和我交流联系。
- ### My Info
  这部分我打算放我的学术成就和出版物，但现在它是空的...... :sob: :sob: :sob:
- ### My Resources
  在这里我放了一些非常酷又很有用的网站或者是编程工具，另外，我也会考虑在这里加一点喜欢的书和电影什么的。。。
- ### My Gallery:
  我准备把这里做成一个记录我生活的相册，当然，或许未来会加些梗图什么的也说不定。。。 :think:
- ### Login:
 这个板块对于访问者来说是完全无效的。。。 我创造这个接口的目的其实就是为了方便我在前端可以写博客和管理自己的网站内容，当然，如果你能猜到我的登录密码和账号的话，请随意处置我的网站哈哈 :sweat_smile:


---
# 运行设置
要运行该项目，您需要同时运行前端和后端以及数据库，以确保该项目能够正常运行。

### Frontend
首先添加一个 ==.env== 文件在frontend/myfront 目录下:
```shell
cd frontend/myfront/
vim .env
```
你的 ==.env== file 应该长这样:
```
VUE_APP_API_KEY=""
VUE_APP_BACKEND_URL=http://localhost:8000/
```
然后运行命令:
```shell
npm install
npm run serve
```

### Backend
同样地，让我们先在ackend/mysite目录下添加==.env==文件:
```shell
cd backend/mysite/
vim .env
```
你的后端 ==.env== 文件应该长这样：
```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=3306
SECRET_KEY=''
```
然后运行命令：
```shell
cd ..
pip install -r requirements.txt
cd backend/mysite/
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**别忘了在运行前后端的同时运行你的数据库!**

之后你就可以访问 http://localhost:8080/ 来看看效果啦 :smile:

### Deployment

你需要设置这个项目的gitHub工作流文件，添加相应的git repo secrets。完成后，git操作将自动构建dockers并部署到指定的服务器上。
