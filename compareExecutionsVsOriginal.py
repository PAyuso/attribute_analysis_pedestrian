
import json
import pandas as pd


pathWhereExecutionsAre="/mnt/rhome/paa/pedestrian/Rethinking_of_PAR/mlruns/"


dictExecutions ={
    'hs-BaldHead-0': 27,
    'hs-BaldHead--1': 26,
    'lb-Skirt-0': 31,
    'lb-Skirt--1': 28,
    'action-CarryinByArm-0': 37,
    'action-CarryinByArm--1': 36,
    'attachment-PaperBag-0': 33,
    'attachment-PaperBag--1': 32,
    'action-Talking-0': 39,
    'action-Talking--1': 38,
    'lb-ShortSkirt-0': 35,
    'lb-ShortSkirt--1': 34,
    'ub-Sweater-0': 30,
    'ub-Sweater--1': 29,
    'multiattribute': 41,
    'weightedloss': 40
}

pathDataOriginal="RAPzs/testOKGithub2/"


listImportantFiles = ['training_metrics.json', 'testing_metrics.json']

import os
#syn
def getExecutionsFromAttribute(attribute, vector):
    global dictExecutions

    if attribute == 'multiattribute' or attribute =='weightedloss':
        pathExecutions = pathWhereExecutionsAre+str(dictExecutions[attribute])+"/"
        listDirs=os.listdir(pathExecutions)
    else:
        pathExecutions = pathWhereExecutionsAre+str(dictExecutions[attribute+"-"+str(vector)])+"/"
        listDirs=os.listdir(pathExecutions)

    executions=[]
    for dirs in listDirs:
        if os.path.isdir(pathExecutions+dirs):
            files = os.listdir(pathExecutions+dirs+"/artifacts/")
            if len(files) > 0:
                cont=0
                for importantFile in listImportantFiles:
                    if importantFile in files:
                        cont+=1
                if cont==2:
                    executions.append(pathExecutions+dirs+"/artifacts/")

    #executions = [pathExecutions+directory+"/artifacts/" for directory in listDirs if os.path.isdir(pathExecutions+directory)]

    return executions

def getEpochLRDecay(pathExecution):
    searchLR = 0.00001
    fileNameWhereLR = 'training_metrics.json'

    fileTraining = open(pathExecution+fileNameWhereLR)
    jsonTraining = json.load(fileTraining)

    listLr=list(jsonTraining['lr'])
    epochDecay=listLr.index(searchLR)
    fileTraining.close()

    return epochDecay

def getGeneralMetricsTraining(pathExecution, epoch):
    fileNameWhereLR = 'training_metrics.json'

    fileTraining = open(pathExecution+fileNameWhereLR)
    jsonTraining = json.load(fileTraining)

    ma=list(jsonTraining['ma'])[epoch]
    f1=list(jsonTraining['f1'])[epoch]
    acc=list(jsonTraining['acc'])[epoch]
    fileTraining.close()
    return ma, f1, acc

def getGeneralMetricsTesting(pathExecution, epoch):
    fileNameWhereLR = 'testing_metrics.json'

    fileTraining = open(pathExecution+fileNameWhereLR)
    jsonTraining = json.load(fileTraining)

    ma=list(jsonTraining['ma'])[epoch]
    f1=list(jsonTraining['f1'])[epoch]
    acc=list(jsonTraining['acc'])[epoch]
    fileTraining.close()
    return ma, f1, acc

def getAttributeMetricsTraining(jsonTrainingLabels, attrib, epoch):
    
    ma=jsonTrainingLabels['ma'+"_"+attrib][epoch]
    f1=jsonTrainingLabels['f1'+"_"+attrib][epoch]
    acc=jsonTrainingLabels['acc'+"_"+attrib][epoch]

    return ma, f1, acc

def getAttributeMetricsTesting(jsonTestingLabels, attrib, epoch):
    
    ma=jsonTestingLabels['ma'+"_"+attrib][epoch]
    f1=jsonTestingLabels['f1'+"_"+attrib][epoch]
    acc=jsonTestingLabels['acc'+"_"+attrib][epoch]

    return ma, f1, acc

from statistics import median
def createDataFrameGeneralMetrics(synExecutions):
    global pathDataOriginal
    # columns execution | ma | high | lower | f1 | high | lower | acc | high | lower
    columns = ['execution', 'ma', 'high ma', 'lower ma', 'f1', 'high f1', 'lower f1', 'acc', 'high acc', 'lower acc']
    listData=[]
    bestEpochOrig = getEpochLRDecay(pathDataOriginal)
    maTrainOrig, f1TrainOrig, accTrainOrig = getGeneralMetricsTraining(pathDataOriginal, bestEpochOrig)
    listData.append(['training original', maTrainOrig, 0, 0, f1TrainOrig, 0, 0, accTrainOrig, 0, 0])
    
    listmaTrainSyn =[]
    listf1TrainSyn =[]
    listaccTrainSyn =[]
    for execution in synExecutions:
        bestEpochExec = getEpochLRDecay(execution)
        maTrainSyn, f1TrainSyn, accTrainSyn = getGeneralMetricsTraining(execution, bestEpochExec)
        listmaTrainSyn.append(maTrainSyn)
        listf1TrainSyn.append(f1TrainSyn)
        listaccTrainSyn.append(accTrainSyn)

    medianMaTrainSyn=median(listmaTrainSyn)
    highMaTrainSyn=max(listmaTrainSyn)
    lowerMaTrainSyn=min(listmaTrainSyn)
    medianF1TrainSyn=median(listf1TrainSyn)
    highF1TrainSyn=max(listf1TrainSyn)
    lowerF1TrainSyn=min(listf1TrainSyn)
    medianAccTrainSyn=median(listaccTrainSyn)
    highAccTrainSyn=max(listaccTrainSyn)
    lowerAccTrainSyn=min(listaccTrainSyn)
    listData.append(['training syn', medianMaTrainSyn, highMaTrainSyn, lowerMaTrainSyn, \
                    medianF1TrainSyn, highF1TrainSyn, lowerF1TrainSyn, medianAccTrainSyn, \
                        highAccTrainSyn, lowerAccTrainSyn])

    ## testing
    bestEpochOrig = getEpochLRDecay(pathDataOriginal)
    maTestOrig, f1TestOrig, accTestOrig = getGeneralMetricsTesting(pathDataOriginal, bestEpochOrig)
    listData.append(['testing original', maTestOrig, 0, 0, f1TestOrig, 0, 0, accTestOrig, 0, 0])
    
    listmaTestSyn =[]
    listf1TestSyn =[]
    listaccTestSyn =[]
    for execution in synExecutions:
        bestEpochExec = getEpochLRDecay(execution)
        maTestSyn, f1TestSyn, accTestSyn = getGeneralMetricsTesting(execution, bestEpochExec)
        listmaTestSyn.append(maTestSyn)
        listf1TestSyn.append(f1TestSyn)
        listaccTestSyn.append(accTestSyn)

    medianMaTestSyn=median(listmaTestSyn)
    highMaTestSyn=max(listmaTestSyn)
    lowerMaTestSyn=min(listmaTestSyn)
    medianF1TestSyn=median(listf1TestSyn)
    highF1TestSyn=max(listf1TestSyn)
    lowerF1TestSyn=min(listf1TestSyn)
    medianAccTestSyn=median(listaccTestSyn)
    highAccTestSyn=max(listaccTestSyn)
    lowerAccTestSyn=min(listaccTestSyn)
    listData.append(['testing syn', medianMaTestSyn, highMaTestSyn, lowerMaTestSyn, \
                    medianF1TestSyn, highF1TestSyn, lowerF1TestSyn, medianAccTestSyn, \
                        highAccTestSyn, lowerAccTestSyn])

    dfGeneral = pd.DataFrame(columns=columns, data=listData)
    return dfGeneral

def getMetricsByAttribute(synExecutions):
    
    global pathDataOriginal
    listAttributesRAPv2 = ['hs-BaldHead', 'hs-LongHair', 'hs-BlackHair', 'hs-Hat', 'hs-Glasses','ub-Shirt','ub-Sweater','ub-Vest','ub-TShirt','ub-Cotton','ub-Jacket','ub-SuitUp','ub-Tight','ub-ShortSleeve','ub-Others','lb-LongTrousers','lb-Skirt','lb-ShortSkirt','lb-Dress','lb-Jeans','lb-TightTrousers','shoes-Leather', 'shoes-Sports', 'shoes-Boots', 'shoes-Cloth', 'shoes-Casual', 'shoes-Other','attachment-Backpack','attachment-ShoulderBag','attachment-HandBag','attachment-Box','attachment-PlasticBag','attachment-PaperBag','attachment-HandTrunk','attachment-Other','AgeLess16', 'Age17-30', 'Age31-45', 'Age46-60','Femal','BodyFat','BodyNormal','BodyThin','Customer','Employee','action-Calling','action-Talking','action-Gathering','action-Holding','action-Pushing','action-Pulling','action-CarryingByArm','action-CarryingByHand','action-Other']
    # from preprocess rethinking
    listAttributesRAPv2.remove('Age46-60')
    listAttributesRAPzs = listAttributesRAPv2
    # columns execution | ma | high | lower | f1 | high | lower | acc | high | lower
    columns = ['execution', 'attribute', 'ma', 'high ma', 'lower ma', 'f1', 'high f1', 'lower f1', 'acc', 'high acc', 'lower acc']
    listData=[]
    for attrib in listAttributesRAPzs:
        
        bestEpochOrig = getEpochLRDecay(pathDataOriginal)
        fileNameWhereLR = 'training_metrics_labels.json'
        fileTraining = open(pathDataOriginal+fileNameWhereLR)
        jsonTraining = json.load(fileTraining)
        maTrainOrig, f1TrainOrig, accTrainOrig = getAttributeMetricsTraining(jsonTraining, attrib, bestEpochOrig)
        listData.append(['training original', attrib, maTrainOrig, 0, 0, f1TrainOrig, 0, 0, accTrainOrig, 0, 0])
        
        listmaTrainSyn =[]
        listf1TrainSyn =[]
        listaccTrainSyn =[]
        for execution in synExecutions:
            bestEpochExec = getEpochLRDecay(execution)
            fileNameWhereLR = 'training_metrics_labels.json'
            fileTraining = open(execution+fileNameWhereLR)
            jsonTraining = json.load(fileTraining)
            maTrainSyn, f1TrainSyn, accTrainSyn = getAttributeMetricsTraining(jsonTraining, attrib, bestEpochExec)
            listmaTrainSyn.append(maTrainSyn)
            listf1TrainSyn.append(f1TrainSyn)
            listaccTrainSyn.append(accTrainSyn)

        medianMaTrainSyn=median(listmaTrainSyn)
        highMaTrainSyn=max(listmaTrainSyn)
        lowerMaTrainSyn=min(listmaTrainSyn)
        medianF1TrainSyn=median(listf1TrainSyn)
        highF1TrainSyn=max(listf1TrainSyn)
        lowerF1TrainSyn=min(listf1TrainSyn)
        medianAccTrainSyn=median(listaccTrainSyn)
        highAccTrainSyn=max(listaccTrainSyn)
        lowerAccTrainSyn=min(listaccTrainSyn)
        listData.append(['training syn', attrib, medianMaTrainSyn, highMaTrainSyn, lowerMaTrainSyn, \
                        medianF1TrainSyn, highF1TrainSyn, lowerF1TrainSyn, medianAccTrainSyn, \
                            highAccTrainSyn, lowerAccTrainSyn])

        ## testing
        bestEpochOrig = getEpochLRDecay(pathDataOriginal)
        fileNameWhereLR = 'testing_metrics_labels.json'
        fileTesting = open(pathDataOriginal+fileNameWhereLR)
        jsonTesting = json.load(fileTesting)
        maTestOrig, f1TestOrig, accTestOrig = getAttributeMetricsTesting(jsonTesting, attrib, bestEpochOrig)
        listData.append(['testing original', attrib, maTestOrig, 0, 0, f1TestOrig, 0, 0, accTestOrig, 0, 0])
        
        listmaTestSyn =[]
        listf1TestSyn =[]
        listaccTestSyn =[]
        for execution in synExecutions:
            bestEpochExec = getEpochLRDecay(execution)
            fileNameWhereLR = 'testing_metrics_labels.json'
            fileTesting = open(execution+fileNameWhereLR)
            jsonTesting = json.load(fileTesting)
            maTestSyn, f1TestSyn, accTestSyn = getAttributeMetricsTesting(jsonTesting, attrib, bestEpochExec)
            listmaTestSyn.append(maTestSyn)
            listf1TestSyn.append(f1TestSyn)
            listaccTestSyn.append(accTestSyn)

        medianMaTestSyn=median(listmaTestSyn)
        highMaTestSyn=max(listmaTestSyn)
        lowerMaTestSyn=min(listmaTestSyn)
        medianF1TestSyn=median(listf1TestSyn)
        highF1TestSyn=max(listf1TestSyn)
        lowerF1TestSyn=min(listf1TestSyn)
        medianAccTestSyn=median(listaccTestSyn)
        highAccTestSyn=max(listaccTestSyn)
        lowerAccTestSyn=min(listaccTestSyn)
        listData.append(['testing syn', attrib, medianMaTestSyn, highMaTestSyn, lowerMaTestSyn, \
                        medianF1TestSyn, highF1TestSyn, lowerF1TestSyn, medianAccTestSyn, \
                            highAccTestSyn, lowerAccTestSyn])

    dfAttributos = pd.DataFrame(columns=columns, data=listData)
    return dfAttributos

import pandas as pd
import argparse

pathSynAnalysis="syntheticExecutionsAnalysis/"

def main(attribute, vector):
    listExecutions = getExecutionsFromAttribute(attribute, vector)

    dfGeneral = createDataFrameGeneralMetrics(listExecutions)
    dfAttributes = getMetricsByAttribute(listExecutions)

    pathToSave=pathSynAnalysis+"attributesWithValuesVsOriginal_{}_vector{}.xlsx".format(attribute, vector)
    with pd.ExcelWriter(pathToSave) as writer:
   
        # use to_excel function and specify the sheet_name and index 
        # to store the dataframe in specified sheet
        dfGeneral.to_excel(writer, sheet_name="General metrics", index=False)
        dfAttributes.to_excel(writer, sheet_name="Attribute metrics", index=False)

    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                    prog='transformPromptToVector',
                    description='Transform csv generated to add two columns for rethinking',
                    epilog='Text at the bottom of help')

    parser.add_argument('-a', '--attribute', required=True)
    parser.add_argument('-v', '--vector', required=True)
    args = parser.parse_args()

    main(args.attribute, args.vector)
