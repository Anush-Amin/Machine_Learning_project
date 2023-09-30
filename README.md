# Steps followed in end to end machine learning project
1) Create the environment inside the folder which you are working and activate it
* To create the environment using conda:
conda create -p venv python==3.8 -y
* To activate the environment:
conda activate venv/
2) Create the .gitignore file and add venv inside it so that while pushing the code into the repo, venv is not not pushed.
3) Create the requirements.txt where all the required libraries to be installed are mentioned.
Add -e . at the end of requirements.txt so that setup.py is triggered.
4) Create the set.py file which will be helpful to create the machine learning application as package, maybe deploy to Pypi and install the packages by reading requirements.txt
5) Create src folder and __init__.py file inside. The project implemented will be inside this folder.
6) Now in terminal enter:
* pip install -r requirements.txt
* while running this for first time retain -e .
* if running again with extra libraries added in requirements.txt comment out -e . line
7) Now the new folder will be create with the name given inside the setup.py file and it will contain few files
8) Inside src create components folder, inside which all the required python files are created.
9) Inside src create pipeline folder, inside which all the required python files for pipeline are created.
10) Inorder to check if the logger.py file is working 
* write a code at the end of logger.py file (delete these lines of code after checking)
if __name__=='__main__':
    logging.info("Logging has started")
* run the logger file using terminal: python src/logger.py
* if logs folder is created in the main folder, then logger.py is running properly.
11) Similarly we can check the exception.py file 
* write a code at the end of exception.py file (delete these lines of code after checking)
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        raise CustomException(e, sys)
* run the exception file using terminal: python src/exception.py
* if exception is raised in the terminal that means code is working fine
12) In this project EDA is done in notebook inside VS code, but its best to EDA in external jupyter only
13) In the data_ingestion.py file, write the code to read the data, split the data into train and test set and return it.
* write the following code at the end of data_ingestion.py file to test this file (delete these lines of code after checking)
if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()