import numpy as np


def analyze_data(DataSet, stock_type, analyze_type, col):
    """
    Manipulating Col Array

    :param DataSet: Array Data Set
    :param analyze_type: type analyze
    :param col: Array column to analyze
    """

    data = np.array(DataSet)
    data = data[...,col] 

    if analyze_type == "sort":
    	val = data[::-1].sort()
    elif analyze_type == "mean":
    	return {"mean":np.mean(data)}
    elif analyze_type == "median":
    	return {"median":np.median(data)}
    elif analyze_type == "std":
    	return {"std":np.std(data)}
    elif analyze_type == "var":
    	return {"var":np.var(data)}
    elif analyze_type == "average":
    	return {"average":np.average(data)}
    elif analyze_type == "min":
    	return {"min":np.min(data)}
    elif analyze_type == "max":
    	return {"max":np.max(data)}
    else:
    	return data.tolist()
