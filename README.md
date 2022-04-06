# Selenium Django Template
A template to run tests based on the [Python Selenium](https://selenium-python.readthedocs.io/) end to end testing framework
interface in Docker.
Uses django as web framework. 

The code is based on the :fire: [Django Example Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) :fire:.

## Selenium
Selenium depends on web drivers to interface with browsers.
Make sure to install the [drivers](https://selenium-python.readthedocs.io/installation.html) of the web browsers you would like to use for testing.

## How To Use
Build the docker image using

```docker build -t selenium-test .```

Then run the container to run all tests with

```docker run selenium-test```

This should run all the tests in the `polls/tests` directory.