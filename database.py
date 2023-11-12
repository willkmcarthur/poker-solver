#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 00:02:36 2022

@author: willmcarthur

This file is for testing the database.py file
"""

import sqlite3

# Make connection to data.db file
connection = sqlite3.connect("data.db")

connection.commit()