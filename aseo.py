#!/usr/bin/python
# 2013 - 2014 | by A. Felipe Cabargas <felipe@cabargas.com>
# This program was published under GPL 3 License
# Please visit http://aseo.cabargas.com/ for more info about this program.
# Beta Release ! Use at your own risk

import os
import re
import shutil

welcome = 'ASEO: Proudly cleaning your files for you. - by @juanpintoduran'
print welcome

note = 'NOTE: Subtitle files founded will be rearranged with video files.'
note2 = 'IMPORTANT: DO NOT USE THIS PROGRAM UNDER SYSTEM FOLDERS.'
print note
print note2

path_required = raw_input('Please write the basepath of the files to be ordered: ')

if os.path.exists(path_required):
    print 'Looking on the path', '\n'
    filenames = os.listdir(path_required)

    print 'Counting files under:', path_required
    files_count = len([item for item in os.listdir(path_required) if os.path.join(path_required, item)])

    print files_count, 'files & folders found. Looking each file extension', '\n'

    for fileindex in range(files_count):

		extension = os.path.splitext(filenames[fileindex])
		extension = extension[1].lower()

		img_ext = ['.jpg', '.png', '.jpeg', '.psd', '.ai', '.bmp', '.tiff', '.svg', '.gif', '.icns']
		media_ext = ['.avi', '.mov', '.mp4', '.flv', '.mpg', '.mpeg', '.wmv', '.rmvb', '.3gp', '.mkv', '.srt']
		audio_ext = ['.mp3', '.flac', '.m4a', '.wav', '.ogg']
		book_ext = ['.epub', '.awz', '.mobi']
		docs_ext = ['.xls', '.doc', '.ppt', '.odt', '.ods', '.xlsx', '.docx', '.pptx']
		pdf_ext = ['.pdf']
		comp_ext = ['.gz', '.zip', '.rar', '.7z', '.tar.gz']
		app_ext = ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.pkg', '.iso']
		dev_ext = ['.py', '.sh', '.rb', '.sql', '.c', '.html', '.css', '.md', '.swf', '.h', '.js', '.java', '.xml', '.yml']
		txt_ext = ['.txt']

		av_exts = [img_ext, media_ext, audio_ext, book_ext, docs_ext, pdf_ext, comp_ext, app_ext, dev_ext, txt_ext]
		av_exts_folders = ['/Images', '/Videos', '/Audio', '/Books', '/Documents', '/PDFs', '/CompressedFolders', '/ApplicationInstallers', '/Developer', '/PlainText']

		or_path = path_required+'/'+filenames[fileindex]

		for i in range(len(av_exts)):
			current_type = av_exts[i]
			current_folder = av_exts_folders[i]
			if extension in current_type:
				dest_path = path_required+current_folder
				if os.path.exists(dest_path):
					shutil.move(or_path, dest_path)
				else:
					os.mkdir(dest_path)
					shutil.move(or_path, dest_path)
else:
	print 'The path given does not exists, try another one later.'