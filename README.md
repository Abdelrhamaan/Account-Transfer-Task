# Project Name

[Account Transfer]

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)

## Description

[Simple Project to read data from different files and transfer money between accounts.]

## Features

1. Read data from csv, json, excel, html
2. save it to postgres database
3. list users with their balances
4. can transfer data between any two users

## Installation

1. clone repository
   ```bash
       git clone git@github.com:Abdelrhamaan/Account-Transfer-Task.git
   ```
2. give execute permsion to entrypoint.sh

   ```bash
      sudo chmod +x Account-Transfer-Task/Task/entrypoint.sh
   ```

3. go inside project
   ```bash
       cd Account-Transfer-Task/Task/
   ```
4. build project with docker compose
   ```bash
       docker compose up --build
   ```
5. run script to read data and save it in database
   ```bash
   docker exec dj_backend python manage.py runscript  script
   ```
6. delete tests.py file in AccountTransfe file then run this command to see test cases
   ```bash
    docker exec dj_backend python manage.py test AccountTransfer
   ```

## Usage

    1. go to http://localhost:8000/list/ to see accounts in pagination
    2. go to http://localhost:8000/update/ to make transfer between any two accounts
    3. to see test cases go to Task/AccountTransfer/tests
    3. to see script which read data go to Task/AccountTransfer/scripts/script.py

<!-- ---

# Django ORM Showcase

## Introduction

Welcome to the Django ORM Showcase project! This project aims to demonstrate the capabilities of various Django Object-Relational Mapping (ORM) libraries.

## Overview

In this project, we have implemented the same functionality using different Django ORM libraries. This allows us to compare and contrast their features, syntax, and performance.

## ORM Libraries

1. **Django ORM (default)**
   - **Description**: Django's built-in ORM, which provides a high-level abstraction for interacting with the database.
   - **Features**: Querysets, model relationships, migrations, etc.

## Getting Started

To get started with this project, follow these steps:

1. Content:
2. Clone the repository:

   ```bash
   git clone git@github.com:Abdelrhamaan/ORM.git

   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt

   ```

4. Run the Django project:
   ```bash
   python manage.py runserver
   ``` -->
