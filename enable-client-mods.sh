#!/bin/sh -x

# enable client-only mods

mv clientmods/GuiAPI* coremods/
mv clientmods/*ReiMinimap* mods/
mv clientmods/*StatusEffectHUD* mods/
mv mods/Dynmap* servermods/
