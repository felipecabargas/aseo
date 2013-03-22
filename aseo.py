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
        
        img_ext = ".jpg" or ".png" or ".psd" or ".ai" or ".bmp" or ".tiff"
        media_ext = ".avi" or ".mov" or ".mp4" or ".flv" or ".mpg" or ".mpeg" or ".wmv" or ".rmvb" or ".3gp" or ".mkv" or ".srv"
        audio_ext = ".mp3" or ".flac" or ".m4a" or ".wav" or ".ogg"
        book_ext = ".epub" or ".awz" or ".mobi"
        docs_ext = ".xls" or ".doc" or ".ppt" or ".odt" or ".odf" or ".odp" or ".xlsx" or ".docx" or ".pptx"
        pdf_ext = ".pdf"
        comp_ext = ".gz" or ".zip" or ".rar" or ".7z"
        app_ext = ".exe" or ".msi" or ".deb" or ".rpm" or ".dmg" or ".pkg"
        
        img_path = "/Images"
        media_path = "/Videos"
        audio_path = "/Audio"
        book_path = "/Books"
        docs_path = "/Documents"
        pdf_path = "/PDFs"
        comp_path = "/CompressedFolders"
        app_path = "/ApplicationInstallers"
        
        or_path = path_required+"/"+filenames[fileindex]
        
        if extension==img_ext:
            dest_path = path_required+img_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension==media_ext:
            dest_path = path_required+media_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension==audio_ext:
            dest_path = path_required+audio_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension==book_ext:
            dest_path = path_required+book_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension==docs_ext:
            dest_path = path_required+docs_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension==pdf_ext:
            dest_path = path_required+pdf_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension==comp_ext:
            dest_path = path_required+comp_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)
        if extension==app_ext:
            dest_path = path_required+app_path
            if os.path.exists(dest_path):
                shutil.move(or_path, dest_path)
            else:
                os.mkdir(dest_path)
                shutil.move(or_path, dest_path)                
        else:
            print "This file cannot be moved. I don't know this extension."
            
        print "I finished cleaning this folder. Au revoir!"
else:
    print "The path given doesn't exists, try another one later."
