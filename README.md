Mini Social Platform
---

### Introduction

Mini Social Platform is a simple project with the following functionality:
  - User Actions
    - User can create an account
    - User can login to his account
    - User can create a new post
    - User can upload an attachment to my new post
    - User can see all posts created by other users
    - User can sort posts chronologically  
    - User can select a post to see more details
    - User can check the comments on a post
    - User can add comments to an any existing post
    - User can check the likes and comments count for any post
    - User can like any post
    - User can access his profile
    - User can view a list of users on the system
    - User can send a friend-request to another users
    - User can approve / reject a friend request
    - User can view all my friends


  - Admin Actions
    - Admin can list all system users
    - Admin can deactivate any user account
    - Admin can list all system posts
    - Admin can delete any post
    - Admin can list all system comments
    - Admin can delete any comment

### Technologies

Mini Social Platform uses a number of open source projects to work properly:

* [Python](https://www.python.org) - is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.
* [Pip](https://pypi.org/project/pip/) - is a package-management system written in Python used to install and manage software packages.
* [Django](https://www.djangoproject.com/) - Django is a Python-based free and open-source web framework that follows the model-template-views architectural pattern.
* [Restful APIs](https://restfulapi.net/) - is architectural style for distributed hypermedia systems.
* [Postgresql](https://www.postgresql.org/) -  is a powerful, open source object-relational database system.
* [Docker](https://www.docker.com/) - is a set of platform as a service (PaaS) products that use OS-level virtualization.
* [Docker Compose](https://docs.docker.com/compose/) - is a tool for running multi-container applications on Docker.

And of course Nespresso Coffee Machine Store itself is open source with a [public repository](https://github.com/FadyAlfred/ncoffemachine)
 on GitHub.

### Install and run

```sh
$ Clone the repository
$ Go into the project folder and exec docker-compose up --build
$ The app should be up and running on localhost:8000
```

### Admin dashboard

```sh
$ Open http://127.0.0.1:8000/admin on yor browser
$ Login using the following credentials {username: admin, password: admin}
$ All CURD operation on coffee machines or pods can be done throw this dashboard
```

### API Documentation
Find all APIs docs here `http://127.0.0.1:8000/swagger/`

### Todos
 - Write test cases for the system
 - Split settings and requirements into several file for several environment