#!/bin/sh

# run server

# move these client-only mods out of the way since they crash server :(
mv coremods/GuiAPI* clientmods/
mv mods/*ReiMinimap* clientmods/

# run server
#java -Dfml.debugClassLoading=true -Dfml.debugClassLoadingFiner=true -mx2G -jar snapshot.jar
java -mx2G -jar snapshot.jar
#java -mx2G -jar 354+sm13.jar

. enable-client-mods.sh
