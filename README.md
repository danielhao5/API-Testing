# API Project 
This project is to demonstrate how to develop the basic API tests by employing the robust test framework Pytest. The focus is primarily on the CRUD operations on API resources via the SDK.  The chosen API is Stripe, an online payment system, which is very popular in states.  

### Prerequisites

```
It will need python 3.6+, pytest 4.0.2, and stripe library.

You will also need to register with stripe.com to get an api key since all
API uses the key(s) to authenticate requests. 
```

### Installing
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all packages:

```
$ pip install python   (and repeat for other components listed above, if not existing)
```


## Running the tests

In the project directory, issue one of these commands for the target test cases: 

command      | meaning 
------------ | -------------
$pytest -v unit | *for all unit test cases* 
$pytest -v func | *for all functionl test cases*
$pytest --html=regression.html  | *for all cases, and generate report*

## Running Results
![Results](unit/unit_test.PNG)

## Built With

* [pytest](https://github.com/pytest-dev/pytest/) - The test framework used
* [pytest-html](https://pypi.org/project/pytest-html/1.6/) - HTML report generating plug-in
* [stripe](https://https://stripe.com/docs/api) -   Stipe API library. 


## Author

* **Daniel Hao** - *Initial work* 


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgements
* This project is purely inspired by an interviewer's challenges.

