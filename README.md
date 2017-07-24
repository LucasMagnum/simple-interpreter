Simple Interpreter
==================

[![CircleCI](https://circleci.com/gh/LucasMagnum/simple-interpreter.svg?style=shield)](https://circleci.com/gh/LucasMagnum/simple-interpreter)
[![codecov](https://codecov.io/gh/LucasMagnum/simple-interpreter/branch/master/graph/badge.svg)](https://codecov.io/gh/LucasMagnum/simple-interpreter)

Simple interpreter for Pascal language built using Python.
This interpreter was built following the `Let's Build a Simple Interpreter` tutorial.
This is an experiment project, the aim is have fun and learn more about compilers & interpreters.


### How to use it

This interpreter can either process a file or run in the REPL mode.

Basically, we have to follow the steps bellow:

1. Clone this repository
2. Install all dependencies (see [setup](#1-setup))
3. Process a Pascal file (see [process a file](#3-processing-a-pascal-file))
4. REPL version (see [REPL version](#4-repl))


### Table of Contents

  * [1. Setup](#1-setup)
  * [2. Running tests](#2-running-tests)
  * [3. Processing a Pascal file](#3-processing-a-pascal-file)
  * [4. REPL](#4-repl)
  * [Useful links](#useful-links)

---

## Development

### 1. Setup

To properly run this interpreter, we should install the dependencies:

  ```bash
  make setup
  ```

### 2. Running tests

We have two kinds of tests implemented: unit tests and behaviour tests. We can run the tests with the following commands:

  ```bash
  make tests   # Run both unit and behaviour tests
  make unit-tests
  make behaviour-tests
  ```

### 3. Processing a Pascal file
  
We can run the application and see the web version of this interpreter.
Just have to run the command bellow:
  
  ```bash
  make run <filename>.pas
  ```

### 4. REPL

This interpreter also has a REPL mode that can be enable with the following command:

  ```bash
  make run-repl
  ```

### Running inside docker

To run this interpreter inside docker, we have to follow the commands bellow:

1. Install docker
2. Build simple interpreter image

     ```bash
     docker build -t simple-interpreter
     ```

3. Run commands using docker

      ```bash
      docker run -i -v `pwd`:/simple-interpreter make tests
      ```


### Useful links

  1 - [Let's build a simple interpreter](https://ruslanspivak.com/lsbasi-part1/)


