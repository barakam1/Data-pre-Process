#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:02:47 2019

@author: prudhvi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#importing the dataset
DS=pd.read_csv("Data.csv")
X=DS.iloc[:,:-1].values
Y=DS.iloc[:,3].values
X
Y
