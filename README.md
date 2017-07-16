Simple Interpreter
==================

[![CircleCI](https://circleci.com/gh/LucasMagnum/simple-interpreter.svg?style=shield)](https://circleci.com/gh/LucasMagnum/simple-interpreter)
[![codecov](https://codecov.io/gh/LucasMagnum/simple-interpreter/branch/master/graph/badge.svg)](https://codecov.io/gh/LucasMagnum/simple-interpreter)

Simple interpreter for Pascal language built using Python.
This interpreter was built following the `Let's Build a Simple Interpreter` tutorial.
This is an experiment project, the aim is have fun and learn more compilers & interpreters.


### How to use it

You can run this interpreter by command line or the web version.

Basically, you have to follow the steps bellow:

1. Clone this repository
2. Install all dependencies (see [setup](#1-setup))
3. Command line:
    python simple_interpreter.py pascal_file.pas
4. Web version (see [web version](#3-running-the-web-application))


### Table of Contents

  * [1. Setup](#1-setup)
  * [2. Running tests](#2-running-tests)
  * [3. Running the web application](#3-running-the-web-application)
  * [Useful links](#useful-links)

---

## Development

### 1. Setup

To properly run this interpreter, you should install the dependencies:

  ```bash
  make setup
  ```

### 2. Running tests

We have two kinds of tests implemented: unit tests and behaviour tests. You can run the tests with the following commands:

  ```bash
  make tests   # Run both unit and behaviour tests
  make unit-tests
  make behaviour-tests
  ```

### 3. Running the web application
  
You can run the application and see the web version of this interpreter.
Just run the command bellow:
  
  ```bash
  make run
  ```

### Useful links

  1 - [Let's build a simple interpreter](https://ruslanspivak.com/lsbasi-part1/)


