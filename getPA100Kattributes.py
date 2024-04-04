
import scipy.io

import pandas as pd
import matplotlib.pyplot as plt

import argparse

def main(type, save, dataset_name, dataset_annotation_filename):
    
    attributes_label = 'attributes'


    value_label = type+'_label'

    pathDataSet = "/mnt/rhome/paa/pedestrian/Rethinking_of_PAR/data/"+dataset_name+"/"
    annotationFile = dataset_annotation_filename

    mat = scipy.io.loadmat(pathDataSet+annotationFile)

    ds = getDataframeValuesAndAttributes(mat, value_label, attributes_label)

    if save:
        fileCSV = dataset_name + '_'+type+'.csv'
        ds.to_csv(fileCSV, sep='\t')
    
    values = list(ds.sum())
    attributes = ds.columns

    namePlot = type+'_'+dataset_name+'_bar.png'
    legendName = type+' label representation '+dataset_name
    plotBarRepresentation(values, attributes, namePlot, legendName)

    return


def getDataframeValuesAndAttributes(mat, value_label, attributes_label):


    attributes_array = mat[attributes_label].tolist()
    
    attributes_list = []
    for atrib in attributes_array:
        attributes_list.append(atrib[0].tolist()[0])

    list_attrib_values = mat[value_label].tolist()

    ds = pd.DataFrame(list_attrib_values, columns=attributes_list)
    
    return ds

# values and attributes should be list
def plotBarRepresentation(values, attributes, namePlot, legendName):

    # Figure Size
    fig, ax = plt.subplots(figsize =(16, 9))
    
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

"""
x_test_for_bar = list(ds_test[attributes_list].sum())
values = x_test_for_bar

attributes = attributes_list
namePlot = 'test_labels_bar.png'
legendName = 'Test labels representations'

"""


#plotBarRepresentation(values, attributes, namePlot, legendName)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('-t', '--type', required=True)           # the type of the data (train, val, test)
    parser.add_argument('-s', '--save', action='store_true')      # save the dataset
    parser.add_argument('-d', '--dataset', required=True) # PA100K
    parser.add_argument('-a', '--annotations', required=True) #annotations.mat

    args = parser.parse_args()
    #print(args.type, args.save)
    main(args.type, args.save, args.dataset, args.annotations)


