


```bash
./qa/utilities/chromedriver.sh
pip install -r qa/requirements.txt
```

```bash
python3 -m pytest
```

```bash
pytest -n 2
```

```bash
pytest --alluredir=./results
allure generate results -o reports --clean
allure open reports
# On subsequent runs
rm -R results*
cp -R reports/history/ results/history
```
They don't look as pretty maybe https://pypi.org/project/allure-pytest-bdd/?
Referenced from https://github.com/allure-framework/allure-python
