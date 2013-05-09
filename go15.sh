#!/bin/sh

# run server

# move these client-only mods out of the way since they crash server :(
mv coremods/GuiAPI* clientmods/
mv mods/*ReiMinimap* clientmods/
mv mods/*StatusEffectHUD* clientmods/
mv servermods/* mods/

# run server
#java -Dfml.debugClassLoading=true -Dfml.debugClassLoadingFiner=true -mx2G -jar snapshot.jar
java -mx4G -XX:MaxPermSize=256m -jar snapshot.jar
#java -mx4G -XX:MaxPermSize=256m -jar mcpc-plus-151compat-1.5.2-R0.2-SNAPSHOT-f686-C0.jar
#java -mx2G -jar 354+sm13.jar
#java -Dorg.spigotmc.netty.disabled=true -mx2G -jar snapshot.jar
#java -agentpath:/Users/admin/Downloads/YourKit_Java_Profiler_12.0.5.app/bin/mac/libyjpagent.jnilib -mx2G -jar snapshot.jar

. enable-client-mods.sh
