###STRUCTURE

./maps: contains a list of json files. Each file contains a map in json format.
./results: contains a list of json files. Each file contains the output of the algorithm in json format.
./tests: contains the list of json files. Each file is a test that can be run.

./config.py contains some parameters, paths useful for the correct behaviour of the environment.
./main.py runs a test, according to the configuration specified in config.py.
./maze.py contains the classes used for the implementation of the algorithms.
./utils.py contains some functions of utility used for the implementation of the algorithms.

./requirements.txt contains the packages to install in order to use this code.

###SETUP OF THE ENVIRONMENT
From the project directory install the requirements with the command: pip3 -r install requirements.txt

###HOW TO USE

####HOW TO ADD MAPS
If you want to add a new map, just create a new json file and place it in ./maps. See the existing ones for the correct syntax.

####HOW TO ADD TESTS
If you want to add a new test, just create a new json file and place it in ./tests. See the existing ones for the correct syntax.

####HOW TO RUN A TEST
To run a certain test, change the value of TEST_NAME in ./config.py. Set the field to the name of the file which contains the test you want to run.
Then, just run ./main.py.
