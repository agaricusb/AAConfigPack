#!/bin/sh -x
# Neutralize useless differences
find minecraft/config -type f -exec perl -pe's/(Generated on ).*/$1X/g' -i {} \;
perl -pe's/(lastLaunch)=.*/$1=1357703735/' -i instance.cfg
sort minecraft/config/redpower/redpower.lang | sponge minecraft/config/redpower/redpower.lang
