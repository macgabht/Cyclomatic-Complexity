# Cyclomatic-Complexity
Internet Applications Project

Tiarnan MacGabhann
Student Number 13325213


This project is run on windows 10, using Python 3.6.3.

The Flask, request and Radon modules are used and require a virtual environment installation.

This project requires a git token to gain access to the repository's whose cyclomatic complexity is being calculated.

To gain a token, go to github, settings and generate a new token from the developer settings. Create a text file called 'git-token.txt' in the same directory as the worker and master codes, and paste this token to the 'git-token.txt' file.

To run the master.py - python master.py (the number of workers used is set to eight)
To run the workers, compile the cmd script which will set eight worker.py's to work

DESCRIPTION
The idea here is that a single manager distributes files from a given github repository url to various worker nodes, which in turn calculate the cyclomatic complexity of the files. The workers return the values calculated and the master script averages the values out.

The master uses a Flask server to distribute the work. It uses requests to obtain a git url to the commits a repository we hard code in. From this url, the idea is to filter out the file trees for each git commit. We then parse out the blob urls for each file within the tree before sending these blobs to be worked on.

The worker upon reception of the blob url, separates the url from the file name. After separating the file name from the blob a quick check whether it is a python file or not is done. It then passes these file names to a temporary file before the CCharvester module calculates the complexity. These values are then passed back to the master who calculates the CC average from there.


DISCLAIMER
I have been having issues in my compilation of this project. I believe they stem from the github url being in the incorrect format
