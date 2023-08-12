#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#python main.py
import asyncio

CYCLE_TIME_APP = 3.0

async def cyclic(cycleTime):
    print("App started")
    while True:
        await asyncio.sleep(cycleTime)
        print("One Mississipi");
        

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

