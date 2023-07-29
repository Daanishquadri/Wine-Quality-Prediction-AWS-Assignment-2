FROM openjdk:8-jre-slim

ARG BUILD_DATE
ARG SPARK_VERSION=3.4.0

LABEL org.label-schema.name="Apache PySpark $SPARK_VERSION" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.version=$SPARK_VERSION

ENV PATH="/Python/PythonProject:${PATH}"
ENV PYSPARK_PYTHON="//Python/PythonProject"


#RUN mkdir /predict
ENV PROG_DIR /winepredict
COPY test.py /winepredict/
COPY ValidationDataset.csv /winepredict/
COPY trainingmodel.model /winepredict/

ENV PROG_NAME test.py
ADD ${PROG_NAME} .

ENTRYPOINT ["spark-submit","test.py"]
CMD ["ValidationDataset.csv"]
