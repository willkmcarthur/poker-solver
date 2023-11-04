#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 00:02:36 2022

@author: willmcarthur
"""

import sqlite3

connection = sqlite3.connect("data.db")

connection.commit()