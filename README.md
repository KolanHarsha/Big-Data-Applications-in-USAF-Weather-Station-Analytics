# Big-Data-Applications-in-USAF-Weather-Station-Analytics
## **Objective**
This project demonstrates the use of big-data technologies in weather station analytics. The project consists of four parts:
1. Developing a Mapper and Reducer application to calculate the average of wind direction (degree) for each observation month from each year
2. Developing a python application that can be implemented in PySpark to calculate the range (the difference between max and min values) of sky ceiling height (meters) for each USAF weather station ID
3. Developing a Mapper and Reducer application to retrieve USAF weather station ID and visibility distance (meters)
4. Loading the data generated from part-3 into hive and pig to retrieve the range of visibility distance for each USAF weather station ID.

## **Data-Overview**
The project utilizes records from the National Climatic Data Center (NCDC) spanning the years 1921 to 1930. The sample data of these records is available in the test_sample.txt file.
The data-format of these records is shown below
![WhatsApp Image 2024-03-13 at 1 34 08 PM](https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/05c9f1f6-e811-42b7-b2b0-4bfa5e60308c)

## **Softwares**
<img src="https://github.com/KolanHarsha/DDos-detection-Using-Machine-Learning/assets/110462466/ec05c02a-389a-4363-8b8c-9b1ba8ca28b0" alt="python" width="150" height="100">
<img src="https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/be5d12c2-1f68-4b50-8f0b-36a35983f4df" alt="python" width="150" height="100">
<img src="https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/a490a714-009d-49c9-94e2-d708d992f8a7" alt="python" width="150" height="100">
<img src="https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/15dbdda4-51ce-4464-a7cd-33dc01f6fb2e" alt="python" width="150" height="100">
<img src="https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/933c85fa-5be7-4f82-8ed5-a3a589d49afc" alt="python" width="150" height="100">

## **Running-Platfroms**
You can use any big-data platforms. Below are some of the popular platforms for big-data processing and parallel computing.
1. [Amazon Web Services (AWS) EMR](https://aws.amazon.com/emr/): A managed big data platform on AWS that provides Hadoop, Spark, and other big data frameworks as a service, making it easy to set up and manage large-scale data processing clusters.
2. [Microsoft Azure HDInsight](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjS2r_hlfKEAxXoH60GHWQKCfQYABAAGgJwdg&ase=2&gclid=Cj0KCQjwncWvBhD_ARIsAEb2HW-lSw5Mj7dElFbAO5xRSxlxO4fl9oCBcSfnKNi7QSH5JQEx3e1wKYQaAt1gEALw_wcB&ohost=www.google.com&cid=CAESV-D2VyBODsHQEeZKppkDMS8PUWyPIvj7QuSVFFeXYBuAgYWS5rTonumBRH4_vAPFbKk6tY5bATMyGvondkjd7zttqfrhOhgZbePGfASC_qQiTg-eQFj2vw&sig=AOD64_0IAYFp0t6LsnMnoIFCxZ59jH68UA&q&nis=4&adurl&ved=2ahUKEwiHgLnhlfKEAxXQKDQIHQ3qBU8Q0Qx6BAgGEAE): A managed big data platform on Azure that offers Hadoop, Spark, and other big data tools as a service, with integration with other Azure services.
This project is implemented on California State University- Eastbay Hadoop system which is the university's hadoop system. The running steps are same for any big-data environments.

## **How to run**
Execute the following commands in the command line after connecting to the big-data system.
### **Part-1**
#### **Mapper and Reducer application to calculate the average of wind direction (degree) for each observation month from each year from NCDC records (note: 999 indicates missing value, and [01459] indicate good quality value).**
The python files for this part are available in Part-1 directory.
Hadoop python Streaming is used in this part which allows you to use Python-programming language to write map and reduce functions, and then use these functions with Hadoop MapReduce framework.
The Jar file used for hadoop python streaming is hadoop-streaming-2.7.3.jar which is provided in files above.

Change the execution permission of the python files:
```bash
chmod +x avgwind_mapper.py
chmod +x avgwind_reducer.py
 ```
The sample data to test the python files is available in test_sample.txt file.
Test the two python files locally before running them using Hadoop:
```bash
cat test_sample.txt | /home/student23/avgwind_mapper.py
cat project_sample.txt | /home/student23/avgwind_mapper.py | sort | /home/student23/avgwind_reducer.py
 ```
Copy the Project data form local [WinSCP/Cyberduck] to HDFS :
```bash
hdfs dfs -mkdir /home/23student23/input_project
hdfs dfs -copyFromLocal Project_Data /home/23student23/input_project
hdfs dfs -ls /home/23student23/input_project
hdfs dfs -ls /home/23student23/input_project/Project_Data
 ```
Execute the mapper and reducer using Hadoop streaming:
```bash
hadoop jar hadoop-streaming-2.7.3.jar -file /home/student23/avgwind_mapper.py
-mapper /home/student23/avgwind_mapper.py -file /home/student23/avgwind_reducer.py
-reducer /home/student23/avgwind_reducer.py
-input /home/23student23/input_project/Project_Data/*/*
-output /home/23student23/output_avgwind
 ```
Find and print out the final output in the console.
```bash
hdfs dfs -ls /home/23student23/output_avgwind
hdfs dfs -cat /home/23student23/output_avgwind/part-00000
```
Output:

![image](https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/3e99f408-90b4-4ba4-a0c9-9b29ef660594)

### **Part-2**
#### **Python application that can be implemented in PySpark to calculate the range (the difference between max and min values) of sky ceiling height (meters) for each USAF weather station ID from NCDC records (note: 99999 indicates missing value, and [01459] indicate good quality value).**
The python files for this part are available in Part-2 directory.
Command to submit a PySpark application to a Spark cluster managed by YARN (Yet Another Resource Negotiator), which is a resource manager typically used with Hadoop.
```bash
spark-submit --master yarn range_pyspark.py
```
After successful execution the output file should be in output_range directory in hdfs.
Printing the final output in the console:
```bash
hdfs dfs -cat /home/23student23/output_range/part-000**
```
Output:
![image](https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/4e8db52b-7aac-4dad-95ee-9edfc210ca85)

### **Part-3**
#### **Mapper and Reducer application to retrieve USAF weather station ID and visibility distance (meters) from NCDC records (note: 999999 indicates missing value, and [01459] indicate good quality value) **
The python files for this part are available in Part-3 directory.
Hadoop python Streaming is used in this part which allows you to use Python-programming language to write map and reduce functions, and then use these functions with Hadoop MapReduce framework.
The Jar file used for hadoop python streaming is hadoop-streaming-2.7.3.jar which is provided in files above.

Change the execution permission of the python files:
```bash
chmod +x distance_mapper.py
chmod +x distance_reducer.py
 ```
The sample data to test the python files is available in test_sample.txt file.
Test the two python files locally before running them using Hadoop:
```bash
cat project_sample.txt | /home/student23/distance_mapper.py
cat project_sample.txt | /home/student23/distance_mapper.py | /home/student23/distance_reducer.py
 ```
Execute the mapper and reducer using Hadoop streaming:
```bash
hadoop jar hadoop-streaming-2.7.3.jar -file /home/student23/distance_mapper.py
-mapper /home/student23/distance_mapper.py -file /home/student23/distance_reducer.py
-reducer /home/student23/distance_reducer.py
-input /home/23student23/input_project/Project_Data/*/*
-output /home/23student23/output_distance
 ```
After successful execution the output file should be in output_distance directory in hdfs.
Command to check the output file:
```bash
hdfs dfs -ls /home/23student23/output_distance
```
![image](https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/9f76abcb-3394-4606-8088-8118ac7cc25f)

The ouput data is stored in part-00000.txt file in output_distance directory.
We use the data generated in part-00000.txt file for the part-4 process.

### **Part-4**
#### **Loading the data generated from part-3 into Pig and Hive to retrieve the range of visibility distance and average visibility distance for each USAF weather station ID.**

Loading the data into Pig:
```bash
records = LOAD'/home/23student23/output_distance/part-00000'
    AS (ID:chararray, distance:int);

DUMP records;

DESCRIBE records;
```
Getting the range of visibility distance for each USAF weather station ID.
```bash
range = FOREACH grouped_records GENERATE group AS ID,
    (MAX(records.distance) - MIN(records.distance)) AS range;

DUMP range;
```
Output:
![image](https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/85d50d16-6e8d-474f-aa82-091b5b1f74b7)

Creating a Table in Hive:
```bash
DROP TABLE IF EXISTS project_records23;

CREATE TABLE project_records23 (Id STRING, distance INT)
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY '\t';
```
Loading the data into the table:
```bash
LOAD DATA LOCAL INPATH 'output_distance/part-00000'
OVERWRITE INTO TABLE project_records23;
```
Retreiving the top-20 rows:
```bash
select * from project_records23
limit 20;
```
Getting the average visibility distance for each USAF weather station ID.
```bash
SELECT Id, Avg(distance)
FROM project_records23
GROUP BY Id;
```
Output:
![image](https://github.com/KolanHarsha/Big-Data-Applications-in-USAF-Weather-Station-Analytics/assets/110462466/83379e65-683a-4613-9807-1c1f0b7dbcfe)

## **Contributors**
- Sai Harsha Vardhan Reddy, Kolan- skolan@horizon.csueastbay.edu, harsha62334@gmail.com

Thanks for reading!


