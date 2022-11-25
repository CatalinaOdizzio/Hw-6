import pandas as pd
from abc import ABC, abstractmethod

class structure:

  def __init__(self,df,column):
        self.df = df
        self.column = list(column)

  @abstractmethod
  def process(self):
        return NotImplementedError 

class gen_dummy(structure):

  def process(self):
      return pd.get_dummies(self.df, columns=self.column, drop_first=True)

class transform_kg(structure):

  def process(self):
      self.df[self.column] = self.df[self.column]*2.2
      return self.df