# ETL-Example

### Intro
In this repo will demonstrate the steps of the an ETL. ETL, stands for Extract, Transform, and Load. Almost in every Data pipeline or workflows we generally extract data from various sources and structures. 

For data manipulation can be multiple ways to perform an ETL. There is the possibility can either be a normal SQL query, also an ETL tool can be involved or any other programming language (in our case we will use Python). This small repo is to demostrates a very basic ETL pipeline, where we will learn to extract data from a .CSV file and follow the transform or clean steps on the data, using various Pandas library methods or PySpark (in our case is Pandas) and load the transformed or cleaned data into target systems.

<p align="center"> 
<img src="https://github.com/BardisRenos/ETL-Example/blob/main/ETL.png" width="450" height="250" style=centerme>
</p>


### Data set
The datase is from kaggle [link](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists) and is in the .csv format 


### Extract data from the file


```python
# Read the csv file
def read_data(file_name):
    with open(file=file_name) as csv_file:
        csv_reader = pd.read_csv(csv_file)

    return csv_reader
```

```python
file_path = "/file/path/of/the_file/aug_train.csv"
res = read_data(file_name=file_path)
print(res.head(5))
```

### Data Transformation and Cleaning



### Data manipulation


### Create cleaned dataset
