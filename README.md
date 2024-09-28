# Pytest BDD setup similar to Behave

## Install

```bash
python3 -m venv qa/env
source qa/env/bin/activate
pip install -r qa/requirements.txt
./qa/utilities/chromedriver.sh
```

## Run

### Local Run

Run tests against Local Dev

```bash
pytest --gherkin-terminal-reporter -vvs
```

## Run on an environment

```bash
## Source environmental variables
source qa/test.env
## Source Secret variables if you're using IAP
source qa/secrets/test.env
# -n set to run tests in parellel
pytest -n 2
```

### Run a Single feature

```bash
pytest -k 'requests'
```

### Run a Single Scenario

Use the associated function name from `@scenerio` decorator or `test_` + the
scenario name from the feature file with spaces replaced with underscores

```bash
pytest -k 'function_name'
```

or tag the test you're working on as `@wip` and use `-m`.

### Run a suite or tag

```bash
pytest -m 'smoke'
```

### To Create an Allure Report Locally

```bash
pytest --alluredir=./results
allure generate results -o reports --clean
allure open reports
# On subsequent runs
rm -R results/
cp -R reports/history/ results/history
```

### Tips

More pytest info can be found [here](https://docs.pytest.org/en/stable/example/simple.html).

#### View Live Logs

```bash
LOG_LEVEL=INFO pytest  -o log_cli=true
```


The pytest-bdd Gherkin Reporter will work if you pass `-v` but it does not
appear live with test run and there is a
[bug](https://github.com/pytest-dev/pytest-bdd/issues/214) where it does not
color passed and failed steps correctly.

```bash
--gherkin-terminal-reporter -v
```
