#!/bin/sh
rm -rf *log*
#java -Dfml.debugClassLoading=true -Dfml.debugClassLoadingFiner=true -mx2G -jar snapshot.jar
java -mx2G -jar snapshot.jar

