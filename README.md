# PigTDD

A test driven approach to building the [Pig Game](https://en.wikipedia.org/wiki/Pig_(dice_game)). Recreation of 
the amazing tutorial at http://www.codekoala.com/pdfs/tdd.pdf. Some minor modifications to build with python3.

This was initially used while delivering a TDD workshop and was created as a steppable repository with each commit
introducing a new concept.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and 
testing purposes.

### Prerequisites

This project needs a python3. Depending on your OS the exact steps to get the prerequisites would vary.

### Build Steps

Once the [Prerequisites](#Prerequisites) are in place, you can run the below command to run the tests

```sh
python -m game.test.test_pig -v
```

To play the game run the command below

```sh
python -m game.pig
```
