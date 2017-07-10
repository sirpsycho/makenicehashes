#!/usr/bin/python

import sys
import os

logloc = "/usr/share/responder/logs/"
hashloc = "/root/crack/hash/responder/"
newentries = False

# Loop through the files in the logloc directory and put individual hashes into a list
def getHashes(logloc):
    hashes = []
    for i in os.listdir(logloc):
	if i.endswith(".txt"):
	    with open("%s%s" % (logloc, i), "r") as f:
		contents = f.readlines()
		for hash in contents:
		    hashes.append(hash)
    return hashes

# Make a dictionary of hashes with distinct usernames as keys
def getUsernames(hashes):
    global newentries
    usernames = {}
    for hash in hashes:
	username = hash.split(':', 1)[0]
	while username in usernames and usernames[username] != hash:
	    username += "."
	if not os.path.isfile("%s%s" % (hashloc, username)):
	    print "[+] Found new hash! - %s" % (username)
	    newentries = True
	usernames[username] = hash
    return usernames

# Get hashes
hashes = getHashes(logloc)

# Make hash dictionary
hashdict = getUsernames(hashes)

# If there are not more new hashes than old hashes, exit
if not newentries:
    print("[!] No new hashes, exiting...")
    sys.exit()

# Populate the hashloc directory with the new hashes
print("[-] populating new hashes from '%s' to '%s'..." % (logloc, hashloc))
for key in hashdict:
    f = open("%s%s" % (hashloc, key), 'w')
    f.write(hashdict[key])

print("[-] Done.")
