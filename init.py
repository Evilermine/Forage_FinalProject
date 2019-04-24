import numpy as np
import pickle
import pandas as pd

class Unpickler:

    def __init__(self, filePath):
        self.CreateDataset(filePath)

    def CreateDataset(self, filePath):
        with open(filePath, 'rb') as datasetFile:
            self.dataset = pickle.load(datasetFile)

    def GetData(self):
        return self.dataset

if __name__ == "__main__":
    unpickler = Unpickler('InformationFile5.pickle')
    Data = unpickler.GetData()

    print(Data)
