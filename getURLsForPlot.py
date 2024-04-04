# this script 
numExperiment="6"
experimentId = "029d36af33d84ea09ccfb6fbf78098e2"
strSeed="605"
ipExperiment="192.168.23.203"
portExperiment="5000"
outputFile = "urlsForPlotRAPzs.txt"

listAttributesPA100k= ['Hat','Glasses','ShortSleeve','LongSleeve','UpperStride','UpperLogo','UpperPlaid','UpperSplice','LowerStripe','LowerPattern','LongCoat','Trousers','Shorts','SkirtDress','boots', 'HandBag','ShoulderBag','Backpack','HoldObjectsInFront','AgeOver60','Age18-60','AgeLess18','Female','Front','Side','Back']
listAttributesPETA = ['accessoryHat','accessoryMuffler','accessoryNothing','accessorySunglasses','hairLong', 'upperBodyCasual', 'upperBodyFormal', 'upperBodyJacket', 'upperBodyLogo', 'upperBodyPlaid', 'upperBodyShortSleeve', 'upperBodyThinStripes', 'upperBodyTshirt','upperBodyOther','upperBodyVNeck','lowerBodyCasual', 'lowerBodyFormal', 'lowerBodyJeans', 'lowerBodyShorts', 'lowerBodyShortSkirt','lowerBodyTrousers','footwearLeatherShoes', 'footwearSandals', 'footwearShoes', 'footwearSneaker','carryingBackpack', 'carryingOther', 'carryingMessengerBag', 'carryingNothing', 'carryingPlasticBags','personalLess30','personalLess45','personalLess60','personalLarger60','personalMale']
listAttributesPETAzs = listAttributesPETA
listAttributesRAPv1 = ['hs-BaldHead','hs-LongHair','hs-BlackHair','hs-Hat','hs-Glasses','hs-Muffler','ub-Shirt','ub-Sweater','ub-Vest','ub-TShirt','ub-Cotton','ub-Jacket','ub-SuitUp','ub-Tight','ub-ShortSleeve','lb-LongTrousers','lb-Skirt','lb-ShortSkirt','lb-Dress','lb-Jeans','lb-TightTrousers','shoes-Leather','shoes-Sport','shoes-Boots','shoes-Cloth','shoes-Casual','attach-Backpack','attach-SingleShoulderBag','attach-HandBag','attach-Box','attach-PlasticBag','attach-PaperBag','attach-HandTrunk','attach-Other','AgeLess16','Age17-30','Age31-45','Female','BodyFat','BodyNormal','BodyThin','Customer','Clerk','action-Calling','action-Talking','action-Gathering','action-Holding','action-Pusing','action-Pulling','action-CarrybyArm','action-CarrybyHand']
listAttributesRAPv2 = ['hs-BaldHead', 'hs-LongHair', 'hs-BlackHair', 'hs-Hat', 'hs-Glasses','ub-Shirt','ub-Sweater','ub-Vest','ub-TShirt','ub-Cotton','ub-Jacket','ub-SuitUp','ub-Tight','ub-ShortSleeve','ub-Others','lb-LongTrousers','lb-Skirt','lb-ShortSkirt','lb-Dress','lb-Jeans','lb-TightTrousers','shoes-Leather', 'shoes-Sports', 'shoes-Boots', 'shoes-Cloth', 'shoes-Casual', 'shoes-Other','attachment-Backpack','attachment-ShoulderBag','attachment-HandBag','attachment-Box','attachment-PlasticBag','attachment-PaperBag','attachment-HandTrunk','attachment-Other','AgeLess16', 'Age17-30', 'Age31-45', 'Age46-60','Female','BodyFat','BodyNormal','BodyThin','Customer','Employee','action-Calling','action-Talking','action-Gathering','action-Holding','action-Pushing','action-Pulling','action-CarryingByArm','action-CarryingByHand','action-Other']
listAttributesRAPzs = listAttributesRAPv2

listOfAttributes = listAttributesRAPzs



# plot training vs testing, url for plot in attributeAnalysis.txt
metricsTrainingVSTesting=[]
# plot general testing, url for plot in ttributeAnalysis.txt
metricsGeneralTesting = []
# plot general training, url for plot in ttributeAnalysis.txt
metricsGeneralTraining = []
# plot training labels, url for plot in ttributeAnalysis.txt
metricsTrainingLabels = []

metricsTrainingLabelsMa = []
metricsTrainingLabelsF1 = []
metricsTrainingLabelsPosRecall = []
metricsTrainingLabelsNegRecall = []
metricsTrainingLabelsAcc = []
metricsTrainingLabelsPrec = []

# plot testing labels, url for plot in ttributeAnalysis.txt
metricsTestingLabels = []

metricsTestingLabelsMA = []
metricsTestingLabelsF1 = []
metricsTestingLabelsPosRecall = []
metricsTestingLabelsNegRecall = []
metricsTestingLabelsAcc = []
metricsTestingLabelsPrec = []


# plot training instance, url for plot in ttributeAnalysis.txt
metricsTrainingInstance = []

metricsTrainingInstanceAcc = []
metricsTrainingInstancePrec = []
metricsTrainingInstanceRecall = []
metricsTrainingInstanceF1 = []

# plot testing instance, url for plot in ttributeAnalysis.txt
metricsTestingInstance = []

metricsTestingInstanceAcc = []
metricsTestingInstancePrec = []
metricsTestingInstanceRecall = []
metricsTestingInstanceF1 = []



metricsTrainingVSTesting.append("training_ma_"+strSeed)
metricsTrainingVSTesting.append("testing_ma_"+strSeed)

metricsGeneralTesting.append("testing_ma_"+strSeed)
metricsGeneralTesting.append("testing_label_f1_"+strSeed)
metricsGeneralTesting.append("testing_pos_recall_"+strSeed)
metricsGeneralTesting.append("testing_neg_recall_"+strSeed)
metricsGeneralTesting.append("testing_acc_"+strSeed)
metricsGeneralTesting.append("testing_prec_"+strSeed)
metricsGeneralTesting.append("testing_rec_"+strSeed)
metricsGeneralTesting.append("testing_f1_"+strSeed)

metricsGeneralTraining.append("training_ma_"+strSeed)
metricsGeneralTraining.append("training_label_f1_"+strSeed)
metricsGeneralTraining.append("training_pos_recall_"+strSeed)
metricsGeneralTraining.append("training_neg_recall_"+strSeed)
metricsGeneralTraining.append("training_acc_"+strSeed)
metricsGeneralTraining.append("training_prec_"+strSeed)
metricsGeneralTraining.append("training_rec_"+strSeed)
metricsGeneralTraining.append("training_f1_"+strSeed)

for attribute in listOfAttributes:

    metricsTrainingLabelsMa.append("training_"+attribute+"_ma_"+strSeed)
    metricsTrainingLabelsF1.append("training_"+attribute+"_label_f1_"+strSeed)
    metricsTrainingLabelsPosRecall.append("training_"+attribute+"_label_pos_recall_"+strSeed)
    metricsTrainingLabelsNegRecall.append("training_"+attribute+"_label_neg_recall_"+strSeed)
    metricsTrainingLabelsAcc.append("training_"+attribute+"_label_acc_"+strSeed)
    metricsTrainingLabelsPrec.append("training_"+attribute+"_label_prec_"+strSeed)

    metricsTrainingInstanceAcc.append("training_"+attribute+"_instance_acc_label_"+strSeed)
    metricsTrainingInstancePrec.append("training_"+attribute+"_instance_prec_label_"+strSeed)
    metricsTrainingInstanceRecall.append("training_"+attribute+"_instance_recall_label_"+strSeed)
    metricsTrainingInstanceF1.append("training_"+attribute+"_instance_f1_label_"+strSeed)

    metricsTestingLabelsMA.append("testing_"+attribute+"_ma_"+strSeed)
    metricsTestingLabelsF1.append("testing_"+attribute+"_label_f1_"+strSeed)
    metricsTestingLabelsPosRecall.append("testing_"+attribute+"_label_pos_recall_"+strSeed)
    metricsTestingLabelsNegRecall.append("testing_"+attribute+"_label_neg_recall_"+strSeed)
    metricsTestingLabelsAcc.append("testing_"+attribute+"_label_acc_"+strSeed)
    metricsTestingLabelsPrec.append("testing_"+attribute+"_label_prec_"+strSeed)
                            
    metricsTestingInstanceAcc.append("testing_"+attribute+"_instance_acc_label_"+strSeed)
    metricsTestingInstancePrec.append("testing_"+attribute+"_instance_prec_label_"+strSeed)
    metricsTestingInstanceRecall.append("testing_"+attribute+"_instance_recall_label_"+strSeed)
    metricsTestingInstanceF1.append("testing_"+attribute+"_instance_f1_label_"+strSeed)





str1="http://{}:{}/#/metric/learning_rate?runs=[\"{}\"]&experiments=[\"{}\"]&plot_metric_keys=[".format(ipExperiment,portExperiment,experimentId, numExperiment)

#"testing_ma_605","training_ma_605","learning_rate","testing_Age18-60_label_acc_605"

str2="]&plot_layout={\"autosize\":true,\"xaxis\":{\"autorange\":true,\"type\":\"linear\"},\"yaxis\":{}}&x_axis=step&y_axis_scale=linear&line_smoothness=1&show_point=false&deselected_curves=[]&last_linear_y_axis_range=[]"

with open(outputFile, "w") as f:
    f.write("metricsTrainingVSTesting\n")
    strToCombine = ""
    for metric in metricsTrainingVSTesting:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsGeneralTesting\n")
    strToCombine = ""
    for metric in metricsGeneralTesting:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")
    
    f.write("metricsGeneralTraining\n")
    strToCombine = ""
    for metric in metricsGeneralTraining:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTrainingLabelsMa\n")
    strToCombine = ""
    for metric in metricsTrainingLabelsMa:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTrainingLabelsF1\n")
    strToCombine = ""
    for metric in metricsTrainingLabelsF1:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTrainingLabelsPosRecall\n")
    strToCombine = ""
    for metric in metricsTrainingLabelsPosRecall:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTrainingLabelsNegRecall\n")
    strToCombine = ""
    for metric in metricsTrainingLabelsNegRecall:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTrainingLabelsAcc\n")
    strToCombine = ""
    for metric in metricsTrainingLabelsAcc:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTrainingLabelsPrec\n")
    strToCombine = ""
    for metric in metricsTrainingLabelsPrec:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTrainingInstanceAcc\n")
    strToCombine = ""
    for metric in metricsTrainingInstanceAcc:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTrainingInstancePrec\n")
    strToCombine = ""
    for metric in metricsTrainingInstancePrec:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTrainingInstanceRecall\n")
    strToCombine = ""
    for metric in metricsTrainingInstanceRecall:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")
    
    f.write("metricsTrainingInstanceF1\n")
    strToCombine = ""
    for metric in metricsTrainingInstanceF1:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingLabelsMA\n")
    strToCombine = ""
    for metric in metricsTestingLabelsMA:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingLabelsF1\n")
    strToCombine = ""
    for metric in metricsTestingLabelsF1:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingLabelsPosRecall\n")
    strToCombine = ""
    for metric in metricsTestingLabelsPosRecall:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingLabelsNegRecall\n")
    strToCombine = ""
    for metric in metricsTestingLabelsNegRecall:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingLabelsAcc\n")
    strToCombine = ""
    for metric in metricsTestingLabelsAcc:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingLabelsPrec\n")
    strToCombine = ""
    for metric in metricsTestingLabelsPrec:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingInstanceAcc\n")
    strToCombine = ""
    for metric in metricsTestingInstanceAcc:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingInstancePrec\n")
    strToCombine = ""
    for metric in metricsTestingInstancePrec:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingInstanceRecall\n")
    strToCombine = ""
    for metric in metricsTestingInstanceRecall:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")

    f.write("metricsTestingInstanceF1\n")
    strToCombine = ""
    for metric in metricsTestingInstanceF1:
        if strToCombine == "":
            strToCombine = strToCombine + "\"" + metric + "\""
        else:
            strToCombine = strToCombine + ",\"" + metric + "\""
    f.write(str1+strToCombine+str2+"\n")
