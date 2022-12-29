# HBNB - The Console

This repository contains the initial stage of the project to build a clone of the AirBnB website.
This project implements a backend interface - the console, to manage program data.
Console commands allow the user to create, retrieve, update, and destroy objects, as well as manage file storage.
Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

### Repository Contents by Project Task

|       Tasks        |                Files                   |               Description      |
|--------------------|----------------------------------------|--------------------------------|
|  0. Authors/README File |    [AUTHORS]()                      |  Project authors               |
|  1. Pep8           |  N/A                                   |  All code is pep8 compliant    |
|  2. Unit Testing   |  [/tests]()                              |  All class-defining modules are unittested |
|  3. Make BaseModel   |  [/models/base_model.py]()           |  Defines a parent class to be inherited by all model classes.  |


## General Use

1. First clone this repo
2. locate the "console.py" file and run it as follows:

```
/AirBnB_clone$ ./console.py
```

3. When the command runs, this prompt should appear:
```
(hbnb) 
```

4. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program

##### Commands
	* create - Creates an instance based on given class

	* destroy - Destroys an object based on class and UUID

	* show - Shows an object based on class and UUID

##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax"
