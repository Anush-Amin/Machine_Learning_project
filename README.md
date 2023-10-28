# Steps followed in end to end machine learning project
1) Create the environment inside the folder which you are working and activate it
* To create the environment using conda:
conda create -p venv python==3.8 -y
* To activate the environment:
conda activate venv/
2) Create the .gitignore file and add venv inside it so that while pushing the code into the repo, venv is not not pushed.
3) Create the requirements.txt where all the required libraries to be installed are mentioned.
Add -e . at the end of requirements.txt so that setup.py is triggered.
4) Create the set.py file which will be helpful to create the machine learning application as package, maybe deploy to Pypi and install the packages by reading requirements.txt. In setup.py we describe the meta-data of the project.
5) Create src folder and __init__.py file inside. The project implemented will be inside this folder.
6) Now in terminal enter:
* pip install -r requirements.txt
* while running this for first time retain -e .
* if running again with extra libraries added in requirements.txt comment out -e . line
7) Now the new folder will be created with the name given inside the setup.py file and it will contain few files
8) Inside src create components folder. All the required python files like data_injestion, data_transformation, model_trainer are created inside this folder.
9) Inside src create pipeline folder. All the required python files for pipeline are created inside this folder.
10) Inside src folder create logger, utils, exception python files.
11) In exception.py file, code is written to get the customised exception.
12) In logger.py file, code is written log the execution details.
13) Inorder to check if the logger.py file is working 
* write a code at the end of logger.py file (delete these lines of code after checking)
if __name__=='__main__':
    logging.info("Logging has started")
* run the logger file using terminal: python src/logger.py
* if logs folder is created in the main folder, then logger.py is running properly.
14) Similarly we can check the exception.py file 
* write a code at the end of exception.py file (delete these lines of code after checking)
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        raise CustomException(e, sys)
* run the exception file using terminal: python src/exception.py
* if exception is raised in the terminal in the format specified in exception.py code that means code is working fine
15) EDA can done in notebook inside VS code, but its best to do EDA in external jupyter.
16) In the data_ingestion.py file, write the code to read the data, split the data into train and test set and return it.
* write the following code at the end of data_ingestion.py file to test this file (delete these lines of code after checking)
if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
* Run the data_ingestion.py file
17) In the data_transformation.py file, write the code to handle categorical and numerical features, create a pickle file.
* write the following code at the end of data_ingestion.py file to test this file (delete these lines of code after checking)
if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
18) Getting the Error while running python data_ingestion.py
src.exception.CustomException: Error occured in python script name [c:\ineuron\internships\1_restaurant_rating_prediction\final\src\components\data_transformation.py], line number [94], error message [all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 1 and the array at index 1 has size 41287]
19) Inorder to get rid of this error convert input_feature_train_arr and input_feature_test_arr into numpy array since its type is scipy.sparse.csr.csr_matrix
20) In model_trainer.py file, write the code to train the model using different algorithms.
* write the following code at the end of data_ingestion.py file to test this file (delete these lines of code after checking)
if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
