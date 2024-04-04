
import scipy.io

import pandas as pd
import matplotlib.pyplot as plt

import argparse

maxSplitPETA=5

pathDataSet="/mnt/rhome/paa/pedestrian/Rethinking_of_PAR/data/PETA/"
annotationFile = "PETA.mat"

folderToSave = "PETA/"

def fromMatToCSV():
    global maxSplitPETA

    global pathDataSet
    global annotationFile
    global folderToSave

    mat = scipy.io.loadmat(pathDataSet+annotationFile)


    array_attrib_values = mat['peta'][0][0][0][:,:]
    len_array_attrib_values = len(array_attrib_values)

    attrib_values_list = []
    for attrib_value in array_attrib_values:
        attrib_values_list.append(attrib_value.tolist())

    attrib_name_list = []
    array_attributes_name = mat['peta'][0][0][1]
    len_array_attrib_name = len(array_attributes_name)
    for attrib_name in array_attributes_name:
        attrib_name_list.append(attrib_name.tolist()[0][0])


    attributes_from_rethinking_used=['accessoryHat','accessoryMuffler','accessoryNothing','accessorySunglasses','hairLong','upperBodyCasual', 'upperBodyFormal', 'upperBodyJacket', 'upperBodyLogo', 'upperBodyPlaid', 'upperBodyShortSleeve', 'upperBodyThinStripes', 'upperBodyTshirt','upperBodyOther','upperBodyVNeck', 'lowerBodyCasual', 'lowerBodyFormal', 'lowerBodyJeans', 'lowerBodyShorts', 'lowerBodyShortSkirt','lowerBodyTrousers','footwearLeatherShoes', 'footwearSandals', 'footwearShoes', 'footwearSneaker','carryingBackpack', 'carryingOther', 'carryingMessengerBag', 'carryingNothing', 'carryingPlasticBags','personalLess30','personalLess45','personalLess60','personalLarger60','personalMale']


    values_for_train = []
    values_for_val = []
    values_for_test = []

    idxTrain = []
    idxVal = []
    idxTest = []
    for idx in range(5):
        print(idx)
        train = mat['peta'][0][0][3][idx][0][0][0][0][:, 0] - 1
        for value_train in train:
            idxTrain.append(value_train)
        
        val = mat['peta'][0][0][3][idx][0][0][0][1][:, 0] - 1
        for value_val in val:
            idxVal.append(value_val)

        test = mat['peta'][0][0][3][idx][0][0][0][2][:, 0] - 1
        for value_test in test:
            idxTest.append(value_test)

        for item in attrib_values_list:
            if item[0] in idxTrain:
                values_for_train.append(item)
            elif item[0] in idxVal:
                values_for_val.append(item)
            else:
                values_for_test.append(item)

        columnsDs = ['idx', 'gidentity', 'idorigds', 'orgidentity'] + attrib_name_list
        ds_train = pd.DataFrame(values_for_train, columns=columnsDs)
        ds_val = pd.DataFrame(values_for_val, columns=columnsDs)
        ds_test = pd.DataFrame(values_for_test, columns=columnsDs)

        ds_train.to_csv(folderToSave+'PETA_train'+str(idx)+'.csv', sep='\t')
        ds_val.to_csv(folderToSave+'PETA_val'+str(idx)+'.csv', sep='\t')
        ds_test.to_csv(folderToSave+'PETA_test'+str(idx)+'.csv', sep='\t')


        idxTrain = []
        idxVal = []
        idxTest = []

        values_for_train = []
        values_for_val = []
        values_for_test = []


# values and attributes should be list
def plotBarRepresentation(fig_size, values, attributes, namePlot, legendName):

    # Figure Size
    fig, ax = plt.subplots(figsize = fig_size)
    
    # Horizontal Bar Plot
    ax.barh(attributes, values)
    
    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    
    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    
    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    
    # Add x, y gridlines
    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)
    
    # Show top values 
    ax.invert_yaxis()
    
    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5, 
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight ='bold',
                color ='grey')
    
    # Add Plot Title
    ax.set_title(legendName,
                loc ='left', )
    

    plt.savefig(namePlot) 


def getPlotsFromCSV():
    global maxSplitPETA
    global pathDataSet
    global annotationFile

    mat = scipy.io.loadmat(pathDataSet+annotationFile)
    attrib_name_list = []
    array_attributes_name = mat['peta'][0][0][1]
    len_array_attrib_name = len(array_attributes_name)
    for attrib_name in array_attributes_name:
        attrib_name_list.append(attrib_name.tolist()[0][0])

    type = "PETA"

    attributes_from_rethinking_used=['accessoryHat','accessoryMuffler','accessoryNothing','accessorySunglasses','hairLong','upperBodyCasual', 'upperBodyFormal', 'upperBodyJacket', 'upperBodyLogo', 'upperBodyPlaid', 'upperBodyShortSleeve', 'upperBodyThinStripes', 'upperBodyTshirt','upperBodyOther','upperBodyVNeck', 'lowerBodyCasual', 'lowerBodyFormal', 'lowerBodyJeans', 'lowerBodyShorts', 'lowerBodyShortSkirt','lowerBodyTrousers','footwearLeatherShoes', 'footwearSandals', 'footwearShoes', 'footwearSneaker','carryingBackpack', 'carryingOther', 'carryingMessengerBag', 'carryingNothing', 'carryingPlasticBags','personalLess30','personalLess45','personalLess60','personalLarger60','personalMale']

    for idx in range(maxSplitPETA):
        ds_train = pd.read_csv(folderToSave+'PETA_train'+str(idx)+'.csv', sep='\t')
        ds_val = pd.read_csv(folderToSave+'PETA_val'+str(idx)+'.csv', sep='\t')
        ds_test = pd.read_csv(folderToSave+'PETA_test'+str(idx)+'.csv', sep='\t')

        values = list(ds_train[attrib_name_list].sum())
        attributes = attrib_name_list
        namePlot = folderToSave+type+'_train_bar'+str(idx)+'_all.png'
        legendName = type+' label representation '+str(idx)
        fig_size = (30, 30)
        plotBarRepresentation(fig_size, values, attributes, namePlot, legendName)

        
        values = list(ds_train[attributes_from_rethinking_used].sum())
        attributes = attributes_from_rethinking_used
        namePlot = folderToSave+type+'_train_bar'+str(idx)+'_rethinking.png'
        legendName = folderToSave+type+' label representation '+str(idx)
        fig_size = (16, 9)
        plotBarRepresentation(fig_size, values, attributes, namePlot, legendName)


        values = list(ds_val[attrib_name_list].sum())
        attributes = attrib_name_list
        namePlot = folderToSave+type+'_val_bar'+str(idx)+'_all.png'
        legendName = type+' label representation '+str(idx)
        fig_size = (30, 30)
        plotBarRepresentation(fig_size, values, attributes, namePlot, legendName)

        values = list(ds_val[attributes_from_rethinking_used].sum())
        attributes = attributes_from_rethinking_used
        namePlot = folderToSave+type+'_val_bar'+str(idx)+'_rethinking.png'
        legendName = type+' label representation '+str(idx)
        fig_size = (16, 9)
        plotBarRepresentation(fig_size, values, attributes, namePlot, legendName)


        values = list(ds_test[attrib_name_list].sum())
        attributes = attrib_name_list
        namePlot = folderToSave+type+'_test_bar'+str(idx)+'_all.png'
        legendName = type+' label representation '+str(idx)
        fig_size = (30, 30)
        plotBarRepresentation(fig_size, values, attributes, namePlot, legendName)

        values = list(ds_test[attributes_from_rethinking_used].sum())
        attributes = attributes_from_rethinking_used
        namePlot = folderToSave+type+'_test_bar'+str(idx)+'_rethinking.png'
        legendName = type+' label representation '+str(idx)
        fig_size = (16, 9)
        plotBarRepresentation(fig_size, values, attributes, namePlot, legendName)

    return

def main(csv, plot):
    if csv:
        fromMatToCSV()
    if plot:
        getPlotsFromCSV()

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('-c', '--csv', action='store_true')   # transform from mat to csv
    parser.add_argument('-p', '--plot', action='store_true')      # get plots from datasets

    args = parser.parse_args()
    #print(args.type, args.save)
    main(args.csv, args.plot)
