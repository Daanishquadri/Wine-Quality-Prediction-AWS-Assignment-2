
import sys
from typing import List, Union

import numpy as np
import pyspark
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.sql import DataFrame
from pyspark.sql.functions import col
from pyspark.sql.session import SparkSession
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score

# Starting the spark session
conf = pyspark.SparkConf().setAppName('winequality').setMaster('local')
sc = pyspark.SparkContext(conf=conf)
spark = SparkSession(sc)

path: Union[str, List[str]] = sys.argv[1:]
# loading the validation dataset
val: DataFrame = spark.read.format(".csv").load(path, header=True, sep=";")
val.printSchema()
val.show()

# changing the 'quality' column name to 'label'
for col_name in val.columns[1:-1] + ['quality']:
    val = val.withColumn(col_name, col(col_name).cast('float'))
val = val.withColumnRenamed('quality', "label")

# creating the feature vector
vector_assembler = VectorAssembler(inputCols=val.columns[1:-1], outputCol='features')
df_tr = vector_assembler.transform(val)
df_tr = df_tr.select(['features', 'label'])

# loading the model from s3
RFModel = RandomForestClassificationModel.load("/winepredict/trainingmodel.model/")

print("model loaded successfully")
predictions = RFModel.transform(df_tr).select('prediction')

# getting a RDD of label and predictions
labelsAndPredictions = df_tr.select('label').join(predictions, df_tr.index == predictions.index)
labelsAndPredictions_df = labelsAndPredictions.toDF("label", "Prediction")
labelpred_df = labelsAndPredictions_df.toPandas()

# Calculating the F1 score
F1score = f1_score(labelpred_df['label'], labelpred_df['Prediction'], average='weighted')
print("F1- score: ", F1score)
print(confusion_matrix(labelpred_df['label'], labelpred_df['Prediction']))
print(classification_report(labelpred_df['label'], labelpred_df['Prediction']))
print("Accuracy", accuracy_score(labelpred_df['label'], labelpred_df['Prediction']))

# calculating the test error
testErr = labelsAndPredictions.filter(
    lambda lp: lp.label != lp.Prediction).count() / float(df_tr.count())
print('Test Error =', testErr)
