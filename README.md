# Pytest BDD setup similar to Behave


## Install
```bash
python3 -m venv qa/env
source qa/env/bin/activate
pip install -r qa/requirements.txt
./qa/utilities/chromedriver.sh
```


## Run

### Simple Run

Run command with optional `-n` flag to control number of concurrent tests

```bash
pytest -n 2
```

### Run a single Scenario

```
pytest qa/steps/test_example.py:
```

### Run a suite

```
pytest -m "smoke"
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
