"""Deliberately broken: it never finishes."""

import time

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
while True:
    time.sleep(60)
