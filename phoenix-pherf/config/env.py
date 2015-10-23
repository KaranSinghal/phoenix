#!/usr/bin/env python

# Required variable to point to Java installation
JAVA_HOME=

# Absolute path the the unzipped directory of the HBase installation
# This is required if you build using the default or cluster profile
# Cluster profile assumes you want to pick up dependencies from HBase classpath
# Not required in standalone.
HBASE_PATH=

# Add a space seperated list of -D environment args. "-Dkey1-val1 -Dkey2=val2"
ENV_PROPS=""

# Uncomment if you would like to remotely debug
#REMOTE_DEBUG="-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=6666"