# import findspark
# findspark.init()
# findspark.find()

import sys
from typing import List

import numpy as np
# Loading the libraries
import pyspark
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import RandomForestModel
from pyspark.sql import DataFrame
from pyspark.sql.functions import col
from pyspark.sql.session import SparkSession
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import f1_score

# Starting the spark session
conf = pyspark.SparkConf().setAppName('winequality').setMaster('local')
sc = pyspark.SparkContext(conf=conf)
spark = SparkSession(sc)

path: str | list[str] = sys.argv[1:]
# loading the validation dataset
val: DataFrame = spark.read.format(".csv").load(path, header=True, sep=";")
val.printSchema()
val.show()

# changing the 'quality' column name to 'label'
for col_name in val.columns[1:-1] + ['""""quality"""""']:
    val = val.withColumn(col_name, col(col_name).cast('float'))
val = val.withColumnRenamed('""""quality"""""', "label")

# getting the features and label separately and converting it to numpy array
features = np.array(val.select(val.columns[1:-1]).collect())
label = np.array(val.select('label').collect())

# creating the feature vector
VectorAssembler = VectorAssembler(inputCols=val.columns[1:-1], outputCol='features')
df_tr = VectorAssembler.transform(val)
df_tr = df_tr.select(['features', 'label'])


# The following function creates the labeled-point and parallelize it to convert it into RDD
def to_labeled_point(scan, feature, labels):
    labeled_points = []
    for x, y in zip(feature, labels):
        lp = LabeledPoint(y, x)
        labeled_points.append(lp)
    return scan.parallelize(labeled_points)


# rdd converted dataset
dataset = to_labeled_point(sc, features, label)

# loading the model from s3
RFModel = RandomForestModel.load(sc, "/winepredict/trainingmodel.model/")

print("model loaded successfully")
predictions = RFModel.predict(dataset.map(lambda x: x.features))

# getting a RDD of label and predictions
labelsAndPredictions = dataset.map(lambda lp: lp.label).zip(predictions)

labelsAndPredictions_df = labelsAndPredictions.toDF()
# converting rdd ==> spark dataframe ==> pandas dataframe
labelpred = labelsAndPredictions.toDF(["label", "Prediction"])
labelpred.show()
labelpred_df = labelpred.toPandas()

# Calculating the F1score
F1score = f1_score(labelpred_df['label'], labelpred_df['Prediction'], average='micro')
print("F1- score: ", F1score)
print(confusion_matrix(labelpred_df['label'], labelpred_df['Prediction']))
print(classification_report(labelpred_df['label'], labelpred_df['Prediction']))
print("Accuracy", accuracy_score(labelpred_df['label'], labelpred_df['Prediction']))

# calculating the test error
testErr = labelsAndPredictions.filter(
    lambda lp: lp[0] != lp[1]).count() / float(dataset.count())
print('Test Error = ' + path(testErr))
