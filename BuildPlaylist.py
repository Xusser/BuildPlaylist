#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys, getopt

def main(argv):
    rewrite = False
    detail = False
    path = os.getcwd()
    OutputPath = os.getcwd() + '/Playlist.m3u8'
    try:
        opts, args = getopt.getopt(argv,"hvr:d:o:")
    except getopt.GetoptError:
        print ("get opts error!")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("Example:\n /path/to/BuildPlaylist.py -d /path/to/Music/ -r https://example.com/Music -o /path/to/Playlist-JP.m3u8 -v")
            sys.exit()
        elif opt == '-o':
            OutputPath = arg
        elif opt == '-d':
            path = arg
        elif opt == '-r':
            URL = arg
            rewrite = True
            print ("Path Rewrite:["+URL+"]")
        elif opt == '-v':
            detail = True
            print ("Print Details")
    print ('Dir:['+path+']')
    print ('OutputPath:['+OutputPath+']')
    f = open(OutputPath, 'w+')
    if detail:
        print ('#EXTM3U\n')
    print ('#EXTM3U\n', file=f)
    for root, dirs, files in os.walk(path):
        for name in files:
            Music = os.path.join(root, name)
            if name.endswith('.m3u8'):
                if detail:
                    print (name + ': Ignored')
                continue
            if rewrite:
                Music = Music.replace(path,URL)
            if detail:
                print (Music) 
            print (Music, file=f)

if __name__ == "__main__":
    main(sys.argv[1:])

