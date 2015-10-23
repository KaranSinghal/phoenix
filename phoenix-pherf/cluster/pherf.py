#!/usr/bin/env python

import config/env.py
import sys
import os

HBASE_CLASSPATH=HBASE_PATH+"/bin/hbase classpath"

PHERF_HOME=os.path.dirname(os.path.abspath(__file__))
CLASSPATH=HBASE_CLASSPATH
CLASSPATH=PHERF_HOME+"/config:"+CLASSPATH

for f in PHERF_HOME/lib/*.jar
  CLASSPATH=CLASSPATH+":"+f


CMD="time "+JAVA_HOME+"/bin/java "+REMOTE_DEBUG + " -Dapp.home="+PHERF_HOME + ENV_PROPS "-Xms512m -Xmx3072m -cp "+CLASSPATH + "org.apache.phoenix.pherf.Pherf"+sys.argv[1:]

eval(CMD)







