# Tardis Selenium UI Tests

Smoke/Acceptance tests for tardis UI using Selenium and Python.

## Getting Started

### Install Python and Pip
You will need the following installed:
 - python 3
 - pip

### Install Libraries
Using Pip install the following libraries:
```
pip install pytest
pip install pypom
pip install selenium
pip install approvaltests
```

 
## Running the tests
From the root of the project run:
```
cd py_selenium
pytest
```

## Changing Tests or Data
The tests and data are stored in BitBucket. You can get the code from bitbucket, 
make changes and check it back in.
Please speak to Olga or Shawn to get set up.

## TODO
- move common functionality to base classes (mostly done)
- run under jenkins (mostly done)
- run under linux (mostly done)
#### Done
- Done! setting url - config file or command line
- Done! close browser after test

