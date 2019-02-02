import os
import json
import requests
import numpy as np

import time
from datetime import datetime

def listOrder(data):
    """
    Manipulating Col Array

    :param data: Requests data
    """

    DataSet = []
    KeySet = []
    for key in data:
        values = []
        timestmp = time.mktime(datetime.strptime(key, "%Y-%m-%d %H:%M:%S").timetuple())
        values.append(timestmp)
        values.append(float(data[key]['1. open']))
        values.append(float(data[key]['2. high']))
        values.append(float(data[key]['3. low']))
        values.append(float(data[key]['4. close']))
        values.append(float(data[key]['5. volume']))

        DataSet.append(values)
        KeySet.append(timestmp)

    return [KeySet,DataSet]

def apiRequests(data):
    """
    Manipulating Col Array

    :param data: Requests data
    """

    url = os.environ.get('API_URL')
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

    try:
        r = requests.get(url, headers=headers, params=data)
        response = r.json()
    except:
        return {"msg": "request failed"}

    return response

def show_data(DataSet, col):
    """
    Manipulating Col Array

    :param DataSet: Array Data Set
    :param analyze_type: type analyze
    :param col: Array column to analyze
    """

    data = np.array(DataSet)
    data = data[...,col] 

    ret = {
        'mean': npMean(data),
        'median': npMedian(data),
        'std': npStd(data),
        'var': npVar(data),
        'average': npAvg(data),
        'min': npMin(data),
        'max': npMax(data)
    }

    return ret

def show_data_load(results):

    dataSet = []
    for value in results:
        ret = {
            "mean": value.mean,
            "median": value.median,
            "std": value.std,
            "var": value.var,
            "average": value.average,
            "min": value.min,
            "max": value.max,
            "function": value.function,
            "symbol": value.symbol,
            "analyze": value.analyze,
            "start_time": value.start_time,
            "end_time": value.end_time,
            "interval": value.interval,
            "user_id": value.user_id
        }
        dataSet.append(ret)

    return dataSet

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
    	return {"mean":npMean(data)}
    elif analyze_type == "median":
    	return {"median":npMedian(data)}
    elif analyze_type == "std":
    	return {"std":npStd(data)}
    elif analyze_type == "var":
    	return {"var":npVar(data)}
    elif analyze_type == "average":
    	return {"average":npAvg(data)}
    elif analyze_type == "min":
    	return {"min":npMin(data)}
    elif analyze_type == "max":
    	return {"max":npMax(data)}
    else:
    	return data.tolist()

def npMean(data):
	return np.mean(data)

def npMedian(data):
	return np.median(data)

def npStd(data):
	return np.std(data)

def npVar(data):
	return np.var(data)

def npAvg(data):
	return np.average(data)

def npMin(data):
	return np.min(data)

def npMax(data):
	return np.max(data)