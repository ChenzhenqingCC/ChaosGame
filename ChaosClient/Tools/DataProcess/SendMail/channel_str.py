#coding=utf-8
import os
import sys

if __name__ == '__main__':
	no_sdk = sys.argv[1]
	and_sdk = sys.argv[2]
	ios_sdk = sys.argv[3]
	LANGUAGE = sys.argv[4]
	channel = ''
	if no_sdk == 'true':
		channel = 'android-' + LANGUAGE + '.develop'
		
	if and_sdk == 'true':
		if channel <> '':
			channel = channel + '_'
		channel = channel + 'android-' + LANGUAGE + '.' + LANGUAGE
		
	if ios_sdk == 'true':
		if channel <> '':
			channel = channel + '_'
		channel = channel + 'ios-' + LANGUAGE + '.' + LANGUAGE + 'ios'
	#print(channel)
	#os.environ["CHANNEL_STR"]=channel
	#os.system('set channel=' + channel)
	fp = open("test.txt",'w')
	fp.write('CHANNEL=' + channel)
	fp.close()