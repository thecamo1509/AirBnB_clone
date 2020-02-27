# AirBnB clone - The console

![N|Solid](https://www.tecnofem.com/wp-content/uploads/2020/02/airbnb-logo.png)
____

## Description
This is the beginning of a great project, in the next few months, we at Holberton School will be creating the AirBnB clone project, and how it says is a clone of the AirBnB application.
This application will be built step by step, the first step of this project is The console.

### The console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
___

## Directories and Files
___
### Directories
| Directory | Description |
| ------ | ------ |
| [models] | This directory contains the modules and classes to create an object|
| [engine] | This directory contains the modules file storage|
| [tests] | This directory contains all the test for models|

### Files
| File | Description |
| ------ | ------ |
| [console.py] | The console file|
| [AUTHORS] | This file contains all the authors of this project|

##### Files models directory
| File | Description |
| ------ | ------ |
| [base_model.py] | BaseModel superclass|
| [amenity.py] | Amenity subclass|
| [city.py] | City subclass|
| [place.py] | Place subclass|
| [review.py] | Review subclass|
| [state.py] | State subclass|
| [user.py] | User subclass|

##### Files engine directory
| File | Description |
| ------ | ------ |
| [file_storage.py] | FileStorage class|

##### Files tests directory
| File | Description |
| ------ | ------ |
| [test_models/test_base_model.py] | Unittest module for file storage|
| [test_engine/test_file_storage.py] | Unittest module for file storage|
___

### Installation
```sh
$ git clone https://github.com/thecamo1509/AirBnB_clone.git
```

### Examples
Display help command
___
```sh
AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) quit
AirBnB_clone$
```
Using commands
___
```sh
AirBnB_clone$ ./console.py
(hbnb) create BaseModel
3d672706-b4b2-4ef1-9f20-d3d4862ac425
(hbnb) show BaseModel 3d672706-b4b2-4ef1-9f20-d3d4862ac425
[BaseModel] (3d672706-b4b2-4ef1-9f20-d3d4862ac425) {'id': '3d672706-b4b2-4ef1-9f20-d3d4862ac425', 'created_at': datetime.datetime(2020, 2, 18, 11, 46, 2, 203459), 'updated_at': datetime.datetime(2020, 2, 18, 11, 46, 2, 203459)}
(hbnb) update BaseModel 3d672706-b4b2-4ef1-9f20-d3d4862ac425 name "Holberton"
(hbnb) show BaseModel 3d672706-b4b2-4ef1-9f20-d3d4862ac425
[BaseModel] (3d672706-b4b2-4ef1-9f20-d3d4862ac425) {'id': '3d672706-b4b2-4ef1-9f20-d3d4862ac425', 'created_at': datetime.datetime(2020, 2, 18, 11, 46, 2, 203459), 'updated_at': datetime.datetime(2020, 2, 18, 11, 46, 2, 203459), 'name': 'Holberton'}
(hbnb) create User
7a808798-d1c7-42ed-977a-2d23f0834f24
(hbnb) all
[ "[BaseModel] (3d672706-b4b2-4ef1-9f20-d3d4862ac425) {'id': '3d672706-b4b2-4ef1-9f20-d3d4862ac425', 'created_at': datetime.datetime(2020, 2, 18, 11, 46, 2, 203459), 'updated_at': datetime.datetime(2020, 2, 18, 11, 46, 2, 203459), 'name': 'Holberton'}", "[User] (7a808798-d1c7-42ed-977a-2d23f0834f24) {'id': '7a808798-d1c7-42ed-977a-2d23f0834f24', 'created_at': datetime.datetime(2020, 2, 18, 11, 47, 57, 519573), 'updated_at': datetime.datetime(2020, 2, 18, 11, 47, 57, 519573)}"]
(hbnb) destroy User 7a808798-d1c7-42ed-977a-2d23f0834f24
(hbnb) all
[ "[BaseModel] (3d672706-b4b2-4ef1-9f20-d3d4862ac425) {'id': '3d672706-b4b2-4ef1-9f20-d3d4862ac425', 'created_at': datetime.datetime(2020, 2, 18, 11, 46, 2, 203459), 'updated_at': datetime.datetime(2020, 2, 18, 11, 46, 2, 203459), 'name': 'Holberton'}"]
(hbnb) destroy BaseModel 3d672706-b4b2-4ef1-9f20-d3d4862ac425
(hbnb) all
[]
(hbnb) quit
AirBnB_clone$
```
___

### Developed with
- Python3: Language builded
- Ubuntu 14.04 LTS: Operative System
- PEP8: Style guide for Python code in ver. 1.7
___

### Authors
- Andrea Méndez Mesias - email: 1159@holbertonschool.com - GitHub user: andreammgcol
- Camilo Morales - email: 1160@holbertonschool.com - GitHub user: thecamo1509
- Paula Fuentes - email: 1076@holbertonschool.com - GitHub user: pafuentess
