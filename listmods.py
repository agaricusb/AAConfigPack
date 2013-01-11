#!/usr/bin/python

# Generate list of mods

import os, hashlib, zipfile, json, pprint

MOD_DB = "mods.json"

def getModFiles():
    dirs = ["minecraft/mods", "minecraft/coremods"]
    mods = []
    for d in dirs:
        mods.extend([os.path.join(d, mod) for mod in os.listdir(d)])
    mods = filter(lambda x: x.endswith(".jar") or x.endswith(".zip"), mods)
    return sorted(mods)

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

def main():
    if os.path.exists(MOD_DB):
        mods = json.loads(file(MOD_DB).read())
    else:
        mods = []

    knownModHashes = [m["sha256"] for m in mods]

    for mod in getMods():
        if mod["sha256"] in knownModHashes:
            continue
      
        print "Adding new mod %s" % (mod["filename"],)
        mods.append(mod)

    mods.sort(lambda a, b: cmp(a["filename"], b["filename"]))
    
    file(MOD_DB, "w").write(json.dumps(mods, indent=4, sort_keys=True))

    print "Total %s mod files" % (len(mods),)

if __name__ == "__main__":
    main()

