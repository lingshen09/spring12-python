#!/usr/bin/env python
# coding: utf-8

# In[3]:


#! /usr/bin/env python 
#coding: utf-8
# env "planet_engine"

# Permission: CN-2082-2
# Author: Li.Yi
# 春节十二响 biu biu biu!
import time
ENGINE_ALL = ["2082001","2082002","2082003"]
FUNERAL_FULL = "TOP LEVEL"
CURVE_NATURAL = "CURVE_NATURAL"

def set_engine_number_mask(engin_num):
    print("set_engine_number_mask start")
    for n in engin_num:
        print("engin no:%s mask set" % n) 
    print("set_engine_number_mask finish")
    return 

def set_funeral_level(level):
    print("set_funeral_level: %s" % level)
    return

def engine_check_init():
    for i in range(0,110,10):
        print("engine check state: %d %%" % i)
        time.sleep(1)
    return 1

def set_curve(curve_name):
    print("set curve to：%s" % curve_name)

def engine_ensure_shutdown():
    print("engine shutdown: OK")

def engine_start():
    print("BOOM!")
    time.sleep(1)
    
def engine_stop(): 
    print(".......")
    time.sleep(2)    
    
def init():
    print("Now time is 2082-1-28 23:59:50")
    set_engine_number_mask(ENGINE_ALL)
    set_funeral_level(FUNERAL_FULL)
    return engine_check_init()

def main():
    set_curve(CURVE_NATURAL); 
    for i in range(12):
        engine_start()
        engine_stop()
    return 0

def final():
    engine_ensure_shutdown()
    
if __name__ == '__main__':
    init()
    main()
    final()





