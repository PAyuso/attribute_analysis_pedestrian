
import json
import pandas as pd

pathDataOriginal="RAPzs/testOKGithub2/"
pathDataSyn="RAPzs/weigthedLoss/"

#original
pathToTestingLabelsOriginal = '/mnt/rhome/paa/pedestrian/attribute_analysis_pedestrian/attribute_analysis_pedestrian/'+pathDataOriginal+'/testing_metrics_labels.json'
pathToTrainingLabelsOriginal =  '/mnt/rhome/paa/pedestrian/attribute_analysis_pedestrian/attribute_analysis_pedestrian/'+pathDataOriginal+'/training_metrics_labels.json'

fileTestingLabelsOrig = open(pathToTestingLabelsOriginal)
jsonTestingLabelsOrig = json.load(fileTestingLabelsOrig)

fileTrainingLabelsOrig = open(pathToTrainingLabelsOriginal)
jsonTrainingLabelsOrig = json.load(fileTrainingLabelsOrig)

#syn
pathToTestingLabelsSyn = '/mnt/rhome/paa/pedestrian/attribute_analysis_pedestrian/attribute_analysis_pedestrian/'+pathDataSyn+'/testing_metrics_labels.json'
pathToTrainingLabelsSyn =  '/mnt/rhome/paa/pedestrian/attribute_analysis_pedestrian/attribute_analysis_pedestrian/'+pathDataSyn+'/training_metrics_labels.json'

fileTestingLabelsSyn = open(pathToTestingLabelsSyn)
jsonTestingLabelsSyn = json.load(fileTestingLabelsSyn)

fileTrainingLabelsSyn = open(pathToTrainingLabelsSyn)
jsonTrainingLabelsSyn = json.load(fileTrainingLabelsSyn)



stepOrig=11
stepSyn=9

columns = ['attribute','training_ma_orig','training_ma_syn','diff_train_ma','testing_ma_orig','testing_ma_syn', 'diff_test_ma','training_f1_orig','training_f1_syn', 'diff_train_f1','testing_f1_orig','testing_f1_syn', 'diff_test_f1','training_acc_orig','training_acc_syn', 'diff_train_acc','testing_acc_orig','testing_acc_syn','diff_test_acc']
metrics = ['ma', 'f1', 'acc']
listAttributesRAPv2 = ['hs-BaldHead', 'hs-LongHair', 'hs-BlackHair', 'hs-Hat', 'hs-Glasses','ub-Shirt','ub-Sweater','ub-Vest','ub-TShirt','ub-Cotton','ub-Jacket','ub-SuitUp','ub-Tight','ub-ShortSleeve','ub-Others','lb-LongTrousers','lb-Skirt','lb-ShortSkirt','lb-Dress','lb-Jeans','lb-TightTrousers','shoes-Leather', 'shoes-Sports', 'shoes-Boots', 'shoes-Cloth', 'shoes-Casual', 'shoes-Other','attachment-Backpack','attachment-ShoulderBag','attachment-HandBag','attachment-Box','attachment-PlasticBag','attachment-PaperBag','attachment-HandTrunk','attachment-Other','AgeLess16', 'Age17-30', 'Age31-45', 'Age46-60','Femal','BodyFat','BodyNormal','BodyThin','Customer','Employee','action-Calling','action-Talking','action-Gathering','action-Holding','action-Pushing','action-Pulling','action-CarryingByArm','action-CarryingByHand','action-Other']
# from preprocess rethinking
listAttributesRAPv2.remove('Age46-60')
listAttributesRAPzs = listAttributesRAPv2
listData = []
for attrib in listAttributesRAPzs:
    listMetric=[]
    listMetric.append(attrib)
    for metric in metrics:
        valueTrainOrig = jsonTrainingLabelsOrig[metric+"_"+attrib][stepOrig]
        valueTestOrig = jsonTestingLabelsOrig[metric+"_"+attrib][stepOrig]

        valueTrainSyn= jsonTrainingLabelsSyn[metric+"_"+attrib][stepSyn]
        valueTestSyn = jsonTestingLabelsSyn[metric+"_"+attrib][stepSyn]

        listMetric.append(valueTrainOrig)
        listMetric.append(valueTrainSyn)

        listMetric.append(valueTrainSyn-valueTrainOrig)

        listMetric.append(valueTestOrig)
        listMetric.append(valueTestSyn)

        listMetric.append(valueTestSyn-valueTestOrig)
    listData.append(listMetric)


df_attrib_values = pd.DataFrame(data=listData, columns=columns)
pathToSave=pathDataSyn+"attributesWithValuesVsOriginal.csv"
df_attrib_values.to_csv(pathToSave)
