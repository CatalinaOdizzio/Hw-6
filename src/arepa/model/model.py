from sklearn.ensemble import RandomForestClassifier
import numpy as np

class model:
       
    def __init__(self, modeltype, data, features, target, hyper, testdata):
        self.data = data
        self.__features = data.loc[:,features]
        self.__target = data.loc[:,target]
        self.modeltype = modeltype
        self.__hyper = hyper
        self.train()
        self.testdata = testdata
        
    def train(self):
        X = self.__features
        y = self.__target
        self.rf = self.modeltype(self.__hyper['n_estimators'],max_depth=self.__hyper['max_depth'],
                                 random_state=self.__hyper['random_state'])
        self.train = self.rf.fit(X, np.ravel(y))
        return None
    
    def predict(self, testdata, features):
        X_test = testdata.loc[:, features]
        predict = np.max(self.train.predict_proba(X_test), axis=1)
        return predict