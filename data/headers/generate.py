"""this script creates a HTML header for every ABF file in the parent folder."""

import sys
sys.path.append("../../src/")
sys.path.insert(0,sys.path.pop())
import pyabf
import glob

if __name__=="__main__":
    out="# Sample ABFs\n"
    out+="This is a small collection of various ABFs I practice developing with.\n\n"    
    out+="File Name | Header | First Value | Ch | swpCnt | swpLen | Protocol\n"
    out+="--- | --- | --- | --- | --- | --- | ---\n"
    for fname in sorted(glob.glob("../*.abf")):
        print(fname)
        abf=pyabf.ABF(fname)
        abf._abfHeader.saveHTML(abf.ID+".html")
        abf._abfHeader.saveMarkdown(abf.ID+".md")
        #out+="* [%s](headers/%s)\n"%(os.path.basename(abf.filename),)
        out+="**%s.abf** | "%(abf.ID)
        out+="[view](%s.md) | "%(abf.ID)
        out+="%s %s | "%(abf.dataY[0],abf.units)
        out+="%s | "%(abf.dataChannels)
        out+="%d | "%(abf.sweepCount)
        out+="%.01f s | "%(abf.sweepLengthSec)
        out+="%s | "%(abf.protocol)
        out+="\n"
    out+="\n\n_This list was automatically generated by [generate.py](headers/generate.py)_\n\n"
    with open('../readme.md','w') as f:
        f.write(out)
    print("updated ../readme.md")