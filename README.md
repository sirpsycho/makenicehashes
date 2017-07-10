# makenicehashes
A short Python script to automate management of hashes - to be used with Responder

# Description
I recently started using the tool Responder (learn more [here](https://github.com/SpiderLabs/Responder)).  Responder makes it really easy to pull NTLM credentials from Windows domains but I didn't like the way that the hashes are stored by default (the Responder that is built into Kali stores discovered credentials in /usr/share/responder/logs/).  The hashes are all mushed together in log files with not-very-meaningful names.  I wrote this script to pull out any hashes from this directory and put them into their own directory and rename them using the corresponding username.

Simply create a directory you would like your hashes to go and define it using the "hashloc" variable. Then, run ./gethashes.py as Responder collects credentials.  It will recognize any new hashes and add them to the directory that was defined.

Note: This could probably be customized fairly easily for other similar situations; I just created it specifically with Responder in mind.
