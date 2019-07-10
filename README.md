# API Project 
This project is to demonstrate how to develop the basic API tests by employing the robust test tool Pytest. The focus is primarily on the CRUD operations on API resources via the SDK.  The chosen API is Stripe, an online payment system, which is very popular in states.  

### Prerequisites

What things you need to install the software and how to install them

```
It will need python 3.6+, pytest 4.0.2, ans strip.
```

### Installing

A step by step series of examples that tell you how to get a development env running


```
$ pip install pytest  (and repeat for others) 
```


## Running the tests

In the project directory, issue this command for all specific tests:

$ pytest -v unit    (for all unit tests)

$ pytest -v func    (for all functional tests) 

$ pytest --html=regression.report    (for both test and report generating) 


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [pytest](https://github.com/pytest-dev/pytest/) - The test framework used
* [pytest-html](https://pypi.org/project/pytest-html/1.6/) - HTML report generating plug-in
* [stripe](https://https://stripe.com/docs/api) -   Stipe API for testing. 


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Daniel Hao** - *Initial work* 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

