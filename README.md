# AutoAccount
This program predicts what account a invoice drew money from by using a Extreme Gradient Boost (XGB) model. 

## Table of Contents
1. [Showcase of AutoAccount](#showcase-of-autoaccount)
2. [Required Modules](#required-modules)  
3. [Installation](#installation)  
4. [Train Model](#train-model)
5. [Predict with Model](#predict-with-model) 
6. [Add new training data](#add-new-training-data)
7. [Included Python Files](#included-python-files)
8. [Frontend](#frontend)
9. [Virtual Environment](#virtual-environment)

## Showcase of AutoAccount
https://github.com/user-attachments/assets/08004744-9462-4648-a93a-0e822c9c7b54

## Required Modules
- `os`
- `glob`
- `pickle`
- `numpy`
- `pandas`
- `xgboost`
- `scikit-learn`
- `matplotlib`
- `shap`
- `flask`
- `flask-cors`

## Installation
I recommend running the program in an virtual environment. Create one by following [Virtual Environment](#virtual-environment)
1. **Clone the repo**  
   In GIT Bash, type:  
   `git clone https://github.com/ArvidMoller/AutoAccount`
2. **Open in VS Code or another preferred editor**
3. **Install modules if not already installed**  
   Run:  
   `pip install numpy pandas xgboost scikit-learn matplotlib flask shap`

## Train Model
1. Navigate to the correct directory using `cd` in the terminal.
2. Run:  
   `python trainModel.py`
3. Choose a dataset to train on.
4. Save the model.

## Predict with Model
1. Navigate to the `xgb_front` folder and run `npm run dev:all`.
2. Open `http://localhost:3000` in a browser to access the front-end.
3. Enter your data and hit submit.

## Add new training data
1. Make a csv document with your new data
2. Save it in the `dataset` folder

## Included python files
1. `trainModel.py`
   This program trains a new xgboost model with data from a csv document in the `dataset` folder.
2. `predict.py`
   This program predicts the account the invoice drew money from using the model trained in the `trainModel.py` program.
3. `main.py`
   This file contains the API and fetches data from the front-end. Then the file calls the `main()` function in `predict.py`. 

## Frontend
The front end is a NEXT.js app named `xgb_front` and can be found in the folder with the same name.

## Virtual Environment
1. Open the folder you want to create the virtual environment in the terminal using `cd`
2. Run `python -m venv <name of virtual environment>`
3. To activate virtual environment, run `venv/Scripts/activate`
4. To deactivate virtual environment, run `deactivate`
