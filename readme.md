# Attribute analysis pedestrian

This repository is created for attribute analysis of pedestrian. This repository is used in paralel of this [repo](https://github.com/valencebond/Rethinking_of_PAR/tree/master).


In this repo we have several parts:
1. Get URLs for the metrics plots
2. Get attribute representation vs metrics of the experiments
3. Get attribute correlation between number of images and performance


## Get URLs for the metrics plots

This part is used to get the metrics plots from mlflow of the experiments results. The script is getURLsForPlot.py and user should change the initial parameters:

numExperiment="9" -> this is for the number of the experiment of mlflow
experimentId = "bd20347da41d4cc4a457cae9bbde4e78" -> experiment ID of mlflow
strSeed="605" -> the seed of the mlflow experiment
ipExperiment="192.168.23.203" -> Ip of the machine where mlflow server is working
portExperiment="5000" -> the port where mlflow server is working
outputFile = "urlsForPlotRAPzs.txt" -> outputfile name with the urls for the plots

The user should copy each url and make control + R to reload the web and geet the plot. Also, plot and csv could be downloaded.


## Usage

For each dataset there are jupyter notebooks to analyze the dataset and their performance. You should get the .jsons from MLFlow of training and testing from the previous step. Then, you will be able to sue the following scripts:

- XX_complexidentities.ipynb, XX_complexidentititesGetAttributes.ipynb : these script is to analyze the distributions performance in test and training related to the identities. To check if there are complex identities.
- XXAttribute.ipynb, XXAttributeAnalysis.ipynb : these script is used to analyze the attributes performance, to check the complex attributes.
- XXCompareExecutionsx.ipynb, compareTwoExecutions.py, compareExecutionsVsOriginal.py  : these scripts are related to compare the performance between executions, in order to check if there is improvement between them.


