#!/usr/bin/env python3
from datetime import datetime
import argparse, os, sys

github_path = 'git@github.com:poke/GitHub-Test.git'

parser = argparse.ArgumentParser( description='Sample gh-pages build tool', epilog=None )
parser.add_argument( '--init', '-i', action='store_true', help='initialize gh-pages subdirectory' )
parser.add_argument( '--commit', '-c', action='store_true', help='commit' )
parser.add_argument( '--publish', '-p', action='store_true', help='publish/push' )

args = parser.parse_args()

if args.init:
	if os.path.exists( 'bin/' ):
		parser.error( 'bin/ already exists, manually remove it' )
	
	os.system( 'git clone -b gh-pages {} bin'.format( github_path ) )
	parser.exit()

if args.commit:
	originalDir = os.getcwd()
	os.chdir( 'bin/' )
	os.system( 'git commit -am "Update, {}"'.format( datetime.utcnow().isoformat( ' ' ) ) )
	os.chdir( originalDir )
	parser.exit()

if args.publish:
	originalDir = os.getcwd()
	os.chdir( 'bin/' )
	os.system( 'git push' )
	os.chdir( originalDir )
	parser.exit()

# build
if not os.path.exists( 'bin/' ):
	parser.error( 'bin/ directory is missing, run the --init option first' )

fo = open( 'bin/data.html', 'w+' )
fi = open( 'data.txt' )

fo.write( '<!DOCTYPE html>\n<html>\n<head>\n  <meta charset="utf-8" />\n  <title>Test</title>\n</head>\n\n<body>\n' )
fo.write( '<h1>Test data</h1>\n<ul>\n' )

for line in fi:
	fo.write( '  <li>{}</li>\n'.format( line ) )

fo.write( '</ul>\n\n</body>\n</html>' )

fi.close()
fo.close()