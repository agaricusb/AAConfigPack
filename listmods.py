#!/usr/bin/python

# Generate list of mods

import os, hashlib, zipfile, json, pprint

MOD_DB = "mods.json"

# Get filenames for each installed mod
def getModFiles():
    dirs = ["minecraft/mods", "minecraft/coremods", "instMods"]
    mods = []
    for d in dirs:
        mods.extend([os.path.join(d, mod) for mod in os.listdir(d)])
    mods = filter(lambda x: x.endswith(".jar") or x.endswith(".zip"), mods)
    mods.append("minecraft/bin/minecraft.jar")
    return sorted(mods)

# Get list of mods with their filenames, hashes, and other metadata
def getMods():
    mods = []

    for modFile in getModFiles():
        # If present, get mcmod metadata
        z = zipfile.ZipFile(modFile)
        namelist = z.namelist()
        if "mcmod.info" in namelist:

            raw_json = z.read("mcmod.info")
            try:
                mcmod = json.loads(raw_json)
            except ValueError as e:
                # https://github.com/cpw/compactsolars/pull/6 & https://github.com/cpw/ironchest/pull/14
                #print "BROKEN JSON!",e,modFile
                mcmod = []
        else:
            mcmod = []

        # Filename and hash is essential
        h = hashlib.sha256(file(modFile).read()).hexdigest()
        mod = {"filename":modFile, "sha256":h, "info":mcmod}

        mods.append(mod)
    return mods

# Get (almost) all configuration files on disk
# Note this only includes the 'config' directory; if a mod decides
# to place its config files elsewhere, it won't be checked.
def getConfigs(roots=["minecraft/config"]):
    configs = []
    for d in roots:
        for config in os.listdir(d):
            path = os.path.join(d, config)
            configs.append(path)
            if os.path.isdir(path): # recurse
                configs.extend(getConfigs(roots=[path]))
    return sorted(configs)

# Get the mod file responsible for the given config file, if any
def getModForConfig(config, mods):
    for mod in mods:
        if not mod.has_key("configs"): continue
        if config in mod["configs"]:
            return mod
    return None

def main():
    # Load existing database
    if os.path.exists(MOD_DB):
        mods = json.loads(file(MOD_DB).read())
    else:
        mods = []

    # Add new mods
    knownModHashes = [m["sha256"] for m in mods]

    for mod in getMods():
        if mod["sha256"] in knownModHashes:
            continue
      
        print "Adding new mod %s" % (mod["filename"],)
        mods.append(mod)

    mods.sort(lambda a, b: cmp(a["filename"], b["filename"]))

    # Check configs are all paired up with mods
    configs = getConfigs()
    for config in configs:
        mod = getModForConfig(config, mods)
        if mod is None:
            print "No mod associated with config: %s" % (config,)
    # .. and that each config exists
    configCount = 0
    for mod in mods:
        for config in mod.get("configs", []):
            if not os.path.exists(config):
                print "Mod %s associated with config '%s' but file does not exist!" % (mod, config)
            configCount += 1

    # Ensure mods still exist
    haveMods = []
    for mod in mods:
        if not os.path.exists(mod["filename"]):
            print "Mod %s deleted! Removing..." % (mod["filename"])
        else:
            haveMods.append(mod)
    mods = haveMods
    
    # Save
    file(MOD_DB, "w").write(json.dumps(mods, indent=4, sort_keys=True))
    print "Total %s mod, %s config files" % (len(mods), configCount)

if __name__ == "__main__":
    main()

