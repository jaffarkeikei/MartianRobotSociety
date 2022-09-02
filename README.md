# Martian Robot Society


## Introduction


It is the year 3142. Robots have finally overtaken the world, and their society involves a very strict hierarchy where every robot knows their place in society. (Also, it should be noted that humans had obviously re-located to Mars by this time, so the planet which the robots have overtaken is Mars, not Earth.) This project models the organization of the Martian Robot Society using trees.

Every robot in the Martian Robot Society is considered a citizen of Mars. The nodes in the tree will each represent one citizen. Citizens all have subordinate-superior relationships, where one citizen may work under another. Additionally, some citizens are leaders of a specific district within the society. All citizens that work under a leader are considered part of that district.

Note that a district could be a geographical area, or just a domain of responsibility, like Finance.



## Structure

_The code is in three layers_:

society_hierarchy.py: Defines classes that keep track of information about the Martian robot society. This is the only file that you will modify. All classes, methods, and functions that you need to write are in this file.

society_ui.py: Defines a graphical user interface for interacting with information about the Martian robot society. Run this module to interact with the user interface. You do not have to read or understand the code in this file. Do not modify this file.

client_code.py: A layer of code that is between the user interface and the "back end" defined in society_hierarchy.py. It uses the code you will be writing in society_hierarchy.py to make the UI work. You may look through this file to see example usage of the methods and functions you will implement. Do not modify this file.

citizens.csv: A sample file describing a robot society hierarchy.

a2_starter_tests.py: Some basic tests cases to test your own code.



## Problem description

_The code consists of three main classes_:

Citizen: A class representing a citizen in a Martian Robot Society.
Society: A class representing the entire Martian Robot Society.
DistrictLeader: A class representing a district leader, a special type of
citizen.


## Citizen class

As mentioned before, each node of the Martian Robot Society tree represents a citizen of this society. Each citizen will have its own set of characteristics:their citizen ID number, manufacturer (the name of which company manufactured this particular robot), model year, job, and their rating (kind of like a credit score; basically a measure of how good of a citizen they are, represented as an integer from 0 to 100).

Each citizen may have one superior and any number of subordinates. For example, consider the following tree of citizens (attributes are labelled by name only for the root Citizen, to avoid clutter):



![simple_society](https://user-images.githubusercontent.com/94993837/188036124-0774da7e-57be-43f1-ae12-903aa1ff8f7a.png)



Notice that ID numbers are unique to citizens: the numbers used don't matter, but they will always be positive integers and there cannot be any duplicates within the hierarchy.

_There are 2 types of subordinate_:

Direct subordinates: These are subordinates that work directly under another citizen. For example, Citizen ID: 2 is a direct subordinate of Citizen ID: 6.
Indirect subordinates: These are subordinates that do not work directly under another citizen. For example, being the subordinate of a subordinate. In our example above, Citizen ID: 7 is an indirect subordinate of Citizen ID: 6.
DistrictLeader class
DistrictLeader is a subclass of Citizen. While district leaders are fairly similar to a regular citizen, they also keep track of the district that they lead. All subordinates (both direct and indirect) are said to be part of (or "belong to") the district. For example, consider the following hierarchy (district leaders are highlighted in blue; attributes are labelled by name only for the root Citizen, to avoid clutter):


![district_society](https://user-images.githubusercontent.com/94993837/188036727-e7ddd13b-135a-4541-8f15-6e70fd23c159.png)
Diagram of a simple hierarchy with districts.


Citizen ID: 5 is the DistrictLeader of the district named "Finance".  Because they are descendants of Citizen ID: 5, both the Citizens ID: 7 and ID: 9 are also considered to be in the "Finance" district. Additionally, since they're under Citizen ID: 6 in the hierarchy, who is the leader of "Area 52", they are also part of the "Area 52" district. In fact, all the citizens are part of the "Area 52" district because its leader is the roof of the society.

It is possible for a citizen to not belong to any district. For example, if Citizen ID: 6 were not a DistrictLeader, then Citizens ID: 3 and ID: 8 would not belong to any district.

If a citizen belongs to multiple districts, we will use the term "immediate district" to refer to the one that is at the lowest level in the tree. For example, in the above tree, Citizen ID: 5, Citizen ID: 7 and Citizen ID: 9 all have "Finance" as their immediate district.

Throughout your program, you may assume that no two DistrictLeaders have the same district; we will not test your code on a society in which two DistrictLeaders have the same district. And our testing will not ask your code to make an update that would create a society in which two DistrictLeaders have the same district.

## Society class
The Society class is responsible for keeping track of the head of the entire society (which is the root of the hierarchy), and providing operations that take the whole society into consideration. Most operations which involve accessing the citizens are done through the society class, such as adding a citizen to the society (when new robots are produced), removing one (when robots are deconstructed), or finding one with a specific citizen ID number.
