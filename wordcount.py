import sys
from random import random
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":
    
    sc = SparkContext(appName="Python")
    text_file = sc.textFile("/Users/liuxiaoxiao/python/word.txt")
    counts = text_file.flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b) \
    .sortBy(lambda x: x[1],False)
    counts.saveAsTextFile("/Users/liuxiaoxiao/python/log1")
    
    sc.stop()