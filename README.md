# Test QA ZUP 
#### Breno de Almeida Pereira

## Preparing environment
- This project was developed and tested on PyCharm and VSCode
- To install all dependencies, run: pip install -r requirements.txt
- Or if open this project on Pycharm and let it install all dependencies  

## Testing scenarios
- All scenarios are described in feature files inside /tests/features

## Running automation

###### Running all tests
- Inside root folder
- run with more details: py test --gherkin-terminal-reporter -vv
- run with less details: py test --gherkin-terminal-reporter -v

###### Running an specific test
- Inside root folder
- run: py test --gherkin-terminal-reporter -vv tests/steps/test_search_for_product.py