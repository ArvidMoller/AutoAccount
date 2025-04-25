# AutoAccount
This program predicts what account a invoice drew money from by using a Extreme Gradient Boost (XGB) model. 

## Table of Contents
1. [Showcase of AutoAccount](#showcase-of-autoaccount)
2. [Required Gems](#required-gems)  
3. [Installation](#installation)  
4. [Run Script](#run-script)  
5. [Add new training data](#add-new-training-data)
6. [Frontend](#frontend)

## Showcase of AutoAccount
Coming Soon

## Required Modules
- `OS`
- `Glob`
- `Pickle`
- `Numpy`
- `Pandas`
- `XGBoost`
- `Sic-Kit Learn`
- `Matplotlib`
- `Flask`


## Installation
1. **Clone the repo**  
   In GIT Bash, type:  
   `git clone https://github.com/ArvidMoller/WordleBot.git`
2. **Open in VS Code or another preferred editor**
3. **Install gems if not already installed**  
   Run:  
   `pip install numpy pandas xgboost scikit-learn matplotlib flask`

## Train Model
1. Navigate to the correct directory using `cd` in the terminal.
2. Run:  
   `python trainModel.py`
3. Choose a dataset to train on.
4. Save the model.

## Predict with Model
1. Navigate to the correct directory using `cd` in the terminal.
2. Type in your data in the predict.csv file.
3. Run:  
   `python predict.py`
(a front end is in the works)

## Add new training data
1. Make a csv document with your new data
2. Save it in the `dataset` folder

## Included python files
1. `trainModel.py`
   This program trains a new xgboost model with data from a csv document in the `dataset` folder.
2. `predict.py`
   This program predicts the account the invoice drew money from using the model trained in the `trainModel.py` program.

## Frontend
The front end is a NEXT.js app named `xgb_front` and can be found in the folder with the same name. The front end is still under development and isn't yet ready to be used. 
