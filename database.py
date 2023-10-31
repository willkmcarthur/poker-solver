#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 00:02:36 2022

@author: willmcarthur
"""

import sqlite3

connection = sqlite3.connect("data.db")
         
# connection.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

# connection.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

# connection.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

# connection.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
      
# connection.execute("DELETE from COMPANY where ID = 1;")
# connection.execute("DELETE from COMPANY where ID = 2;")
# connection.execute("DELETE from COMPANY where ID = 3;")
# connection.execute("DELETE from COMPANY where ID = 4;")

connection.commit()

# cursor = connection.execute("SELECT id, name, address, salary from COMPANY")

# for row in cursor:
#    print ("ID = ", row[0])
#    print ("NAME = ", row[1])
#    print ("ADDRESS = ", row[2])
#    print ("SALARY = ", row[3], "\n")
