# Wine-Quality-Prediction-AWS-Assignment-2
# Aim of the project: 

The main objective of this individual task is to gain knowledge in building parallel machine learning (ML) applications on the Amazon AWS cloud platform. The focus will be on acquiring three essential skills:
Utilizing Apache Spark to train ML models concurrently across multiple EC2 instances.
Implementing Spark's MLlib to develop and leverage ML models in the cloud environment.
Mastering Docker to create a container for the ML model, streamlining the process of model deployment.

# Creation of 4 Ec2 Instances for running the model

First, I logged into the AWS website and went to the learners lab. Then, I clicked on the "Start Lab" button to begin the lab. Once it started, I clicked on the AWS tab, and it took me to the AWS website. There, I looked for EC2 instances and created four new instances, giving them names like a1, a2, a3, and a4. The steps for creating the instances were similar to what I did in Project 1. But at the end, I changed the role from "labrole" to "EMR role."

<img width="1440" alt="Screenshot 2023-07-28 at 10 45 54 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/bec7b7db-d90b-4635-9f20-e46e0f5e168e">
<img width="1440" alt="Screenshot 2023-07-28 at 10 45 43 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/834688b5-40f7-4446-bc24-a124913a426c">




# Creation of a single Amazon S3 Bucket

I went to the search tab and searched for Amazon S3. When I found it, I had the option to create a new bucket. I went ahead and created a new bucket named "eca1". After creating the S3 bucket, I uploaded all my CSV files and .py files into it. Once the files were uploaded, I continued with the next steps of creating an Amazon EMR for EC2 instances, which creates clusters for the EC2 instances.
<img width="1440" alt="Screenshot 2023-07-28 at 10 46 42 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/e74570cb-d0d0-4072-a8cf-1919cc2457fa">
<img width="1440" alt="Screenshot 2023-07-28 at 11 21 34 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/ec5eaeb8-2299-4d05-b538-36a2d1152462">




# Creation of Amazon EMR clusters on EC2 instnaces

Once I went to the Amazon EMR tab I got an option to create a cluster.
So, I created the cluster using the following method:
Choose "Step execution" in Launch mode.
Select "Spark application" for Step type and click on "Configure."
Set "Deploy mode" to "Client," "Spark-submit options" to "spark-submit --deploy-mode client https://s3.console.aws.amazon.com/s3/buckets/eca1?region=us-east-1&tab=objects," and "Application location" to spark-submit --deploy-mode client https://s3.console.aws.amazon.com/s3/buckets/eca1?region=us-east-1&tab=objects" Also, set "Action on failure" to "Terminate Cluster" (it will stop the cluster after the step is completed successfully).
Choose "Spark" for Software configuration.
For Hardware configuration, select "Number of instances" as 4.
Click on "Create Cluster," and it will take about 30 minutes to finish.
To check the progress, go to the Step tab and click "View logs" for the Spark application.
So, I created 3 clusters and all of them were terminated with errors 
I have tried to google why I was getting errors tried all the videos I checked and it didn't work

<img width="1440" alt="Screenshot 2023-07-28 at 10 46 42 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/3849e4b1-2115-4e0a-a14c-bccaa0d18d1f">

<img width="1440" alt="Screenshot 2023-07-28 at 10 53 54 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/49c85858-0b47-4198-8f48-f337263637aa">


# Tried to run the code

After setting up the EC2 instances, S3 buckets, and Amazon EMR clusters, I attempted to run the .csv and .py files, but encountered an error. Even when running the code via Docker, the same error persisted. However, when I ran the code in the PyCharm IDE, I was able to retrieve the first 20 numbers from the file successfully. Unfortunately, I'm facing difficulties in running the program on my AWS console.

<img width="1440" alt="Screenshot 2023-07-28 at 11 03 38 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/4f8d1e29-8fbc-4c61-a9a6-eaa7a77d76ec">
<img width="1440" alt="Screenshot 2023-07-28 at 11 03 47 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/b0b8dc0a-0a54-428e-91e3-ea6a868137be">

# Running Model Prediction on Single EC2 instance with Docker.

You have created an EC2 instance with Docker installed on it. To work with your application, you can log in to the EC2 instance. Once logged in, you can download a Docker image and run it interactively using the latest version. When running the image, you can pass the S3 link of the "ValidationDataset.csv" file as a test to the Docker container. This will help you test your application using the data from the "S3 bucket you have created" storage on AWS.




