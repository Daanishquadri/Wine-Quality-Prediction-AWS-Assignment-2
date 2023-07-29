# Wine-Quality-Prediction-AWS-Assignment-2
# Aim of the project: 

The main objective of this individual task is to gain knowledge in building parallel machine learning (ML) applications on the Amazon AWS cloud platform. The focus will be on acquiring three essential skills:
Utilizing Apache Spark to train ML models concurrently across multiple EC2 instances.
Implementing Spark's MLlib to develop and leverage ML models in the cloud environment.
Mastering Docker to create a container for the ML model, streamlining the process of model deployment.

# Creation of 4 Ec2 Instances for running the model

First, I logged into the AWS website and went to the learners lab. Then, I clicked on the "Start Lab" button to begin the lab. Once it started, I clicked on the AWS tab, and it took me to the AWS website. There, I looked for EC2 instances and created four new instances, giving them names like a1, a2, a3, and a4. The steps for creating the instances were similar to what I did in Project 1. But at the end, I changed the role from "labrole" to "EMR role."

<img width="1440" alt="Screenshot 2023-07-28 at 10 33 34 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/604cf329-8cd6-49b4-92ab-cf60e3aa7d47">
<img width="1440" alt="Screenshot 2023-07-28 at 10 33 47 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/db8f108d-75e3-461c-82b4-405548d91cfe">

# Creation of a single Amazon S3 Bucket

I went to the search tab and searched for Amazon S3. When I found it, I had the option to create a new bucket. I went ahead and created a new bucket named "eca1". After creating the S3 bucket, I uploaded all my CSV files and .py files into it. Once the files were uploaded, I continued with the next steps of creating an Amazon EMR for EC2 instances, which creates clusters for the EC2 instances.
<img width="1440" alt="Screenshot 2023-07-28 at 10 33 47 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/df127fb5-d9fa-4464-a3d3-a9f09e2cd5ea">

<img width="1440" alt="Screenshot 2023-07-28 at 10 39 58 PM" src="https://github.com/Daanishquadri/Wine-Quality-Prediction-AWS-Assignment-2/assets/84735952/e4ec3cfd-fc32-429e-92bc-242f9f33d9b5">




