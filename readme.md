# Example of API Testing Framework using Python, Pytest, Pytest-BDD, Allure, and Requests.
### How to Build/Run locally:
#### clone repo:
```
git clone https://github.com/vsshk/python-pytest-pytestbdd-requests-example.git
cd python-pytest-pytestbdd-requests-example
```
1. In order to run you have to install Python3.6+
2. You need to have pip installed
3. Getting dependencies:
   ```shell script
    pip install virtualenv
    virtualenv venv
    (win) venv/Scripts/activate
    (mac/linux) source venv/bin/activate
    pip install -r requirements.txt
    ```
4. Running Api tests:
```
python -m pytest --alluredir=reports/ tests/test_api.py  --base_url https://swapi.dev 
```
5. Running Smoke tests:
```
python -m pytest --alluredir=reports/ tests/test_web_smoke.py  --base_url https://swapi.dev
```
WHERE (-n 4) number of threads, (--alluredir=reports/) report directory.
6. Running all tests
```
python -m pytest --gherkin-terminal-reporter  --showlocals  --alluredir=reports/ tests/test_api.py  --base_url https://swapi.dev
```
    WHERE (-n 4) number of threads, (--alluredir=reports/) report directory.
* Please give a "star" if it helped you.
