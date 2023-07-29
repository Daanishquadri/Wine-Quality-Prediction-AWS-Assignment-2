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
<img width="1440" alt="Screenshot 2023-07-28 at 10 46 36 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/52f893f5-b888-4ce3-b801-f1f3f59fb173">




