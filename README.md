
![](assets/img/readme_img/amiresponsive.png)

# The Blue Box Exchange

## *** UNDER CONSTRUCTION ***

This is my final project for my Full-stack Level 5 Diploma. It is a Django based full e-commerce solution allowing users 4 tiers of access; basic, plus, pro and admin.

Bootstrap5.3, jQuery3.7.1 plus custom code from myself powers a site dedicated to allowing users to buy and sell Dr. WHo related merchandise. Running on the Heroku platform with ElephantSQL managing the databse this site has a clean modern uncluttered look and with its message board feature encourages Dr. Who fans to exchange info about the show they love whilst adding to their Dr. Who collection. Plus a gallery allowing fans of the show to upload their own fan art.

## Table of Contents

1. [Initial Setup of IDE and Github](#initial-setup-of-ide-and-github)



## Initial Setup of IDE and Github

To create a new repo:

first go to https://github.com/ and create a new repo, then in the terminal:

- echo "# test" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/thespamster/the_blue_box.git
- git push -u origin main

In VS Code in the terminal create a virtual environment:

- python -m venv venv -- creates virtual environment.

- venv\Scripts\Activate.ps1 -- activates virtual environment.

Once created add a  .gitignore file and MIT LICENSE, then create an assets folder and subfolders for CSS, Javascript and images with a separate subfolder for the README images.

With the virtual environment activated the Django project is created by first installing Django

- pip3 install django

and then starting the new project.

- django-admin startproject blue_box



[Back to top](#the-blue-box-exchange)

## Acknowledgements

- [Stan Triepels](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/) - for the excellent vscode django gitignore file.
- [reMarkable 2](https://remarkable.com/) - e-ink tablet used to generate wireframes as PDF.
- [Smashicons on Flaticon](https://www.flaticon.com/free-icons/tardis) - Tardis icons created by Smashicons. Check them out. Awesome icons for free.