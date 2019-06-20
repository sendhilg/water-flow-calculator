# Water Flow Calculator

## Description
The application is completed as a task following the [brief](BRIEF.md).

## Requirements
The application was developed using python version 3.7.3 on a windows 10 machine.

To check the version on your machine run the below command:

    $ python --version

This project uses tox as a generic virtualenv management and test command line tool for local development/testing purposes. 

Install tox using the below command.

    $ pip3 install tox

## Cloning the project and running the application

Clone the project from github. 

    $ git clone https://github.com/sendhilg/water-flow-calculator.git

Change into the project directory 'water_flow_calculator'.

    $ cd water-flow-calculator

The application prompts the user to enter values for the below at the command line.
* `Quantity` Quantity of water poured.
* `Row Number` Row number for the glass.
* `Glass Number` Glass number on the row for which the flow needs to be calculated.

To enter values at the command line, type the below tox command and press enter:

    $ tox -e flow_calculator

Wait for tox to build the virtualenv and install dependencies. This may take few seconds the first time
the virtualenv is built and should be faster with successive runs of tox. Once the virtualenv is built enter commands as below.

### Example
```
Enter water quantity poured in litres:
0.50

Enter row number:
1

Enter glass number:
1

Amount of water in glass number 1 of row number 1 is:
0.125
```

## Unit Tests

### Running unit tests
Navigate to the project directory.

    $ cd water-flow-calculator

Run the below command to run the tests with code coverage.

    $ tox
