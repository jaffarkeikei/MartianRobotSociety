# Martian Robot Society

Welcome to the repository for **Martian Robot Society** - a project modeling the organization of the Martian Robot Society using trees.

## Table of Contents

- [Introduction](#introduction)
- [Structure](#structure)
- [Problem Description](#problem-description)
  - [Citizen Class](#citizen-class)
  - [DistrictLeader Class](#districtleader-class)
  - [Society Class](#society-class)

## Introduction

It is the year 3142. Robots have finally overtaken the world, and their society involves a very strict hierarchy where every robot knows their place in society. (Also, it should be noted that humans had obviously re-located to Mars by this time, so the planet which the robots have overtaken is Mars, not Earth.) This project models the organization of the Martian Robot Society using trees.

Every robot in the Martian Robot Society is considered a citizen of Mars. The nodes in the tree will each represent one citizen. Citizens all have subordinate-superior relationships, where one citizen may work under another. Additionally, some citizens are leaders of a specific district within the society. All citizens that work under a leader are considered part of that district.

## Structure

_The code is in three layers_:

- `society_hierarchy.py`: Defines classes that keep track of information about the Martian robot society. This is the only file that you will modify. All classes, methods, and functions that you need to write are in this file.
- `society_ui.py`: Defines a graphical user interface for interacting with information about the Martian robot society. Run this module to interact with the user interface. You do not have to read or understand the code in this file. Do not modify this file.
- `client_code.py`: A layer of code that is between the user interface and the "back end" defined in `society_hierarchy.py`. It uses the code you will be writing in `society_hierarchy.py` to make the UI work. You may look through this file to see example usage of the methods and functions you will implement. Do not modify this file.
- `citizens.csv`: A sample file describing a robot society hierarchy.
- `a2_starter_tests.py`: Some basic test cases to test your own code.

## Problem Description

_The code consists of three main classes_:

### Citizen Class

As mentioned before, each node of the Martian Robot Society tree represents a citizen of this society. Each citizen will have its own set of characteristics: their citizen ID number, manufacturer (the name of which company manufactured this particular robot), model year, job, and their rating (kind of like a credit score; basically a measure of how good of a citizen they are, represented as an integer from 0 to 100).

...

### DistrictLeader Class

DistrictLeader is a subclass of Citizen. While district leaders are fairly similar to a regular citizen, they also keep track of the district that they lead. All subordinates (both direct and indirect) are said to be part of (or "belong to") the district. ...

### Society Class

The Society class is responsible for keeping track of the head of the entire society (which is the root of the hierarchy), and providing operations that take the whole society into consideration. Most operations which involve accessing the citizens are done through the society class, such as adding a citizen to the society (when new robots are produced), removing one (when robots are deconstructed), or finding one with a specific citizen ID number.

