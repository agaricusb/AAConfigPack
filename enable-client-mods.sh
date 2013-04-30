#!/bin/sh -x

# enable client-only mods

mv clientmods/GuiAPI* coremods/
mv clientmods/*ReiMinimap* mods/
mv mods/Dynmap* servermods/
