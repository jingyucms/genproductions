import os, sys

binning = "PtLL"
#binning = "inclusive"

if binning == "PtLL":
    bins = ["0to50", "50to150", "150to250", "250to400", "400to600", "600to800", "800to1200", "1200toInf"]
elif binning == "inclusive":
    bins = [""]

for b in bins:
    if b == "":
        bstring = ""
    else:
        bstring = binning+"-"+b+"_"

    jname = "DYJetsToLL_M-1to10_"+bstring+"13TeV-madgraphMLM-pythia8"
    fDir = "cards/mycards/DYJetsToLL_M-1to10_"+bstring+"13TeV-madgraphMLM-pythia8/"
    log = "mysub_DYJetsToLL_M-1to10_"+bstring+"13TeV-madgraphMLM-pythia8.log"

    cmd = 'nohup ./submit_cmsconnect_gridpack_generation.sh '+jname+' '+fDir+' 4 "4 Gb" > '+log+' 2>&1 &'

    print cmd

    #os.system(cmd)
