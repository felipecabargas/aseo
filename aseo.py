#!/usr/bin/python
# 2013 - by A. Felipe Cabargas <felipe@cabargas.com>
# This program was published under GPL 3 License
# Please visit http://www.cabargas.com/ for more info about this program.
# Beta Release ! Use at your own risk

import os
import re
import shutil

welcome = "(Re)Arrange files on folders by extension - by @juanpintoduran"
print welcome

note = "NOTE: Subtitle files founded will be rearranged with video files"
print note

path_required = raw_input("Please write the basepath of the files to be ordered: ")

if os.path.exists(path_required):
    print "Looking on the path", "\n"
    filenames = os.listdir(path_required)
    
    print "Counting files under:", path_required
    files_count = len([item for item in os.listdir(path_required) if os.path.isfile(os.path.join(path_required, item))])
    
    print files_count, "files found. Looking each file extension", "\n"
    
    for fileindex in range(files_count+1):
        
        extension = os.path.splitext(filenames[fileindex])[1]
        
        img_ext = [".jpg", ".png", ".psd", ".ai", ".bmp", ".tiff"]
        media_ext = [".avi", ".mov", ".mp4", ".flv", ".mpg", ".mpeg", ".wmv", ".rmvb", ".3gp", ".mkv", ".srv"]
        audio_ext = [".mp3", ".flac", ".m4a", ".wav", ".ogg"]
        book_ext = [".epub", ".awz", ".mobi"]
        docs_ext = [".xls", ".doc", ".ppt", ".odt", ".ods", ".odp", ".xlsx", ".docx", ".pptx"]
        pdf_ext = [".pdf"]
        comp_ext = [".gz", ".zip", ".rar", ".7z"]
        app_ext = [".exe", ".msi", ".deb", ".rpm", ".dmg", ".pkg", ".iso"]
        
        img_path = "/Images"
        media_path = "/Videos"
        audio_path = "/Audio"
        book_path = "/Books"
        docs_path = "/Documents"
        pdf_path = "/PDFs"
        comp_path = "/CompressedFolders"
        app_path = "/ApplicationInstallers"
        
        or_path = path_required+"/"+filenames[fileindex]
        
        if extension in img_ext:
            dest_path = path_required+img_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension in media_ext:
            dest_path = path_required+media_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension in audio_ext:
            dest_path = path_required+audio_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension in book_ext:
            dest_path = path_required+book_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension in docs_ext:
            dest_path = path_required+docs_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension in pdf_ext:
            dest_path = path_required+pdf_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension in comp_ext:
            dest_path = path_required+comp_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension in app_ext:
            dest_path = path_required+app_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)                
        else:
            print "This file cannot be moved. I don't know this extension."
            
else:
    print "The path given doesn't exists, try another one later."
