# Django To Do Project
## About To Do Project
This is a simple web app that allows users to create profiles and to do lists. This is my first time using Django for a personal project, so I hope to gain some additional experience with it through this.

## Features
Users are be able to sign up and login, and create to do tasks which will be displayed as their home page once logged in. They will be able to manage their lists by adding new tasks, checking off tasks as completed, and viewing their tasks by tasks' dates to be completed (in order of soonest to be finished).

## What I Learned
Having had exposure to Django from a prior summer internship, I was re-exposed to creating a functional web application with a full stack, utilizing some Bootstrap classes for the frontend. I learned how to create a form for adding objects into a model/database, and being able to retrieve the stored information in order to display it on the front end for users. 

Additionally, I learned about Django's built-in security features when it came to marking tasks as completed (which simply deletes those tasks from the model). With the LoginRequiredMixin and UserPassesTestMixin, I was able to ensure that a user would only be able to delete their own tasks, and making other users' tasks inaccessible via 403 response codes.
