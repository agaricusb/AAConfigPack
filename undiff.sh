#!/bin/sh -x
# Neutralize useless differences

# timestamps
find minecraft/config -type f -exec perl -pe's/(Generated on ).*/$1X/g' -i {} \;
find minecraft/config -type f -exec perl -MPOSIX -pe '$d=POSIX::strftime("%a %b %d", localtime);s/$d.*/(timestamp removed)/' -i {} \;
perl -pe's/(lastLaunch)=.*/$1=1357703735/' -i instance.cfg

# unordered collection
sort minecraft/config/redpower/redpower.lang | sponge minecraft/config/redpower/redpower.lang

# workaround comment truncation bug
perl -pe's/^# set to true to clear chromosomes.*/# set to true to clear chromosomes which contain invalid alleles. might rescue your save if it is crashing after removal of a bee addon/' -i minecraft/config/forestry/common.conf
perl -e'undef $/; $_ = <>; s/(PROPOLISPIPE)\n[^\n]+\n[^\n]+/$1/; print' < minecraft/config/forestry/pipes.conf | sponge minecraft/config/forestry/pipes.conf
