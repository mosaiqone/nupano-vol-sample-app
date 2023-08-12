#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#python main.py
#py main.py

import asyncio

CYCLE_TIME_APP = 1.0

#read file
try:
    #Prio 1: machine config
    configFile = open('machine_config/machine_config.txt','r')
    text_to_print = "Using machine configuration: " + configFile.read()

except:
    try: 
        #Prio 2: default app config
        configFile = open('app_config/app_config.txt','r')
        text_to_print = "Using app configuration: " + configFile.read()

    except:
        #Prio 3: fall back
        text_to_print = "config.txt not found :-("


async def cyclic(cycleTime):
    print("App started")
    while True:
        await asyncio.sleep(cycleTime)
        print(text_to_print);
        

""" CYCLIC SYSTEM """
try:
    """ START CYCLIC EXECUTION """
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(cyclic(CYCLE_TIME_APP))
    loop.run_forever()

except Exception as e:
    print("Event loop failed: {0}".format(e))
    
finally:
    print("Event loop stopped")
    loop.close()

