import tarfile
import argparse, logging, os, sys, struct, re

		
def recover(name):
    return unicode(name, 'utf-8')
	
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputtar", default=".",help="tarball file address")
parser.add_argument("-o", "--outdir", default=".",help="Output directory address.")
args = parser.parse_args()
tar = tarfile.open(name=args.inputtar, mode='r', bufsize=16*1024)
updated = []
for m in tar.getmembers():
    m.name = recover(m.name)
    updated.append(m)
	
tar.extractall('\\\\?\\'+args.outdir, members=updated)
tar.close()