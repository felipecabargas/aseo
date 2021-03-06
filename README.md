# ASEO - Proudly cleaning your folders for you
### "Assigning Stuff (by) Extensions" Organizer
#### v2.2.0
___

ABOUT
-----

ASEO (spanish word for "cleaning") is a little program written in Python that (re)arranges your files on folders by extensions.

Actually it supports most common file extensions for most common filetypes (Audio/Video, Documents, Images, Installers, etc).

Next versions will provide support for more extensions and filetypes ( ** currently working on that ** ).

EASY DOWNLOAD
-----

To download ASEO quickly via terminal:

```bash
$ curl -O https://raw.github.com/felipecabargas/aseo/master/aseo.py
```

USAGE
-----

Execute via terminal:

```bash
$ python aseo.py
```

To give a path to realocate files (for example with the Downloads folder):

MacOSX:

```
/Users/JohnDoe/Downloads
````

Linux:

```
/home/johndoe/Downloads
````

REQUIREMENTS
------------

UNIX based OS (Windows support will be added in the next version)

CHANGELOG
---------

[v2.2]

  - Out of Beta !
  - Add support for multiple extensions:
      - E-Books: .ibooks
      - Compressed: .tgz
      - Installers: .apk, .app, .img
  - Add support for Font files

[v2.1]

  - Minor bug fixes
  - Better implementation of the files scanner
  - Removed dotfile marks on output

[v2.0]

  - Minor bug fixes
  - Added support for OD Formats
  - New output for files not recognized by the program
  - [NOTE 1: dotfiles will show 'dotfile' entry on the last output line, if you wanna keep information secure please encrypt the files and do not use '.files']

[v1.1]

  - Minor bug fixes
  - Added support for ISO, TAR.GZ and SVG files
  - [NOTE 1: This version remains being tagged as "unstable" so use carefully and AT YOUR OWN RISK ]

[v1.0]

  - Initial Release

LICENSE
-------

Copyright (C) 2013  A. Felipe Cabargas M. <felipe.cabargas@gmail.com>

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.