# WEEK 07: MAP REDUCE

Exercise 7 of 02807 Computational Tools for Big Data at DTU

## Content:

This week will be an introduction to MapReduce and the Python library mrjob.

Watch my lecture here: https://youtu.be/nbQADQs57x8

## Learning objectives:

After this week, you are supposed to know:

- What MapReduce is
- How to write a MapReduce procedure
- How to implement and run an mrjob script locally

## Resources:

You should start by learning about the yield-command in Python. This is a command which you might not have seen before and it takes a few minutes to understand it. It is heavily used in the mrjob library that we will use this week. Read about yield here: http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

Finally go and learn about mrjob, a library for working with MapReduce in Python on your own computer. You can watch this: http://youtu.be/DrCKkQeU4kg?t=3m and check the full documentation here: https://pythonhosted.org/mrjob/guides.html


## Exercises:


### Exercise 7.1:

Define and implement a MapReduce job to count the occurrences of each word in a text file. Document that it works with a small example.

### Exercise 7.2:

Define and implement a MapReduce job that determines if a graph has an Euler tour (all vertices have even degree) where you can assume that the graph you get is connected. This file https://www.dropbox.com/s/usdi0wpsqm3jb7f/eulerGraphs.txt?dl=0 has 5 graphs – for each graph, the first line tells the number of nodes N and the number of edges E. The next E lines tells which two nodes are connected by an edge. Two nodes can be connected by multiple edges.

It is fine if you split the file into 5 different files. You do not need to keep the node and edge counts in the top of the file.

Document that it works using a small example.
### Exercise 7.3:

Make a MapReduce job which counts the number of triangles in a graph. Use the following graph http://www.cise.ufl.edu/research/sparse/matrices/SNAP/roadNet-CA.html. The “Matrix Market” format is the preferred one as it has the same format as the Facebook data. (Remember to remove the header in the beginning of file)

Document that it works using a small example and run it on the large file to see that you get the right results.

## Install

It's recommended to create a virtual environment (conda env preffered)
``` bash
make setup
```
## Usage



# Unit test
``` bash
make unit
```


## License
MIT © [Jose Luis Bellod Cisneros](http://josl.github.io)
