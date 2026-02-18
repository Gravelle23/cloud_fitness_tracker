Overview

As a software engineer, I am working to strengthen my understanding of how applications interact with cloud databases. For this project, I built a Cloud Fitness Tracker in Python that connects to a Firebase Firestore database.

This terminal-based application allows users to:

Create user accounts

Add fitness entries (workouts or meals)

View entries (all or filtered by user)

Update entries

Delete entries and users

The program performs full CRUD (Create, Read, Update, Delete) operations on a cloud-hosted database. Each fitness entry is connected to a user through a userId field, demonstrating how related data can be structured in a NoSQL database.

To run the program:

Install dependencies:

pip install firebase-admin


Add your serviceAccountKey.json file to the project folder (not included in the repository).

Run:

python main.py


Software Demo Video

Cloud Database

This project uses Google Firebase Firestore, a NoSQL cloud database.

The database contains two related collections:

users

name

email

createdAt

entries

userId (links to users collection)

type (workout or meal)

title

calories (optional)

duration (optional)

createdAt

updatedAt (optional)

The entries collection is related to the users collection through the userId field.

The software demonstrates:

Insert operations

Retrieve/query operations

Update operations

Delete operations

Development Environment

Tools used:

Visual Studio Code

Python 3

Firebase Console

GitHub

Language:

Python

Libraries:

firebase-admin

datetime

The Firebase Admin SDK was used to securely connect to Firestore using a service account key.

Useful Websites

https://firebase.google.com/docs

https://firebase.google.com/docs/admin/setup

https://docs.python.org/3/

https://stackoverflow.com/

Future Work

Add user authentication

Create a web or GUI version

Add stronger input validation

Add data summary features (totals, reports)

Implement unit testing