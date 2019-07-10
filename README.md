# API Project 
This project is to demonstrate how to develop the basic API tests by employing the robust test tool Pytest. The focus is primarily on the CRUD operations on API resources via the SDK.  The chosen API is Stripe, an online payment system, which is very popular in states.  

### Prerequisites

```
It will need python 3.6+, pytest 4.0.2, ans strip.

You will also need to register with stripe.com to get an api key since all API uses API keys to authenticate requests. 
```

### Installing

```
$ pip install pytest  *(and repeat for other components list above)*
```


## Running the tests

In the project directory, issue one of these commands for the target test cases: 

command      | meaning 
------------ | -------------
$pytest -v unit | *for all unit test cases* 
$pytest -v func | *for all functionl test cases*
$pytest --html=regression.report  | *for all cases, and generate report*



## Built With

* [pytest](https://github.com/pytest-dev/pytest/) - The test framework used
* [pytest-html](https://pypi.org/project/pytest-html/1.6/) - HTML report generating plug-in
* [stripe](https://https://stripe.com/docs/api) -   Stipe API for testing. 


## Authors

* **Daniel Hao** - *Initial work* 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

