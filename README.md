# psysimg
Python command line utility to make manipulation of RomWBW USCD p-System disk images with Ciderpress a bit easier.

## Overview
The [RomWBW](https://github.com/wwarthen/RomWBW) USCD p-System implemenation doesn't have an easy way to get files on and off the storage device. The distributed disk image includes two .vol files with can be read and written to using [Ciderpress](https://a2ciderpress.com/). It is also possible to create a further 4 disk units from within p-System. This script attempts to make accessing these disk units and editing them with Ciderpress bit easier.

## Usage
I've only tested on Windows 11 with Python 3.10 as (afaik) Ciderpress is a Windows only application, so it's likely you'll want to run the script on a Windows machine, though there's no reason it won't work on other platforms. To run USCD p-System I'm using the [RomWBW 3.2.1 release](https://github.com/wwarthen/RomWBW/releases/tag/v3.2.1) running on a [SC130](https://smallcomputercentral.com/sc130-z180-motherboard/).

Use [Win32Diskimager](https://sourceforge.net/projects/win32diskimager/) or similar tool to make an image of your storage device, e.g. SD card.

Then you can use the `-e` option to extract one of the possible disk units (4,5,9,10,11 or 12) - this extracted image can then be read and written to within Ciderpress.
If your intention is just backup, then you are done - however, using the `-u` option, if you have added or altered some files you can patch the changes back on to the disk image.
The patched image can then be written back to the storage device.

### Examples

Extract disk unit \#5 from disk image sc130.img and save it as unit5.vol

`python .\psysimg -e sc130.img unit5.vol 5`

The .vol file can then be read/written using Ciderpress.

Once you have finished you can then patch the modified .vol image back in to the main orginal disk image, which can be subsequently written back to your SD card:

`python .\psysing -u sc130.img unit5.vol 5`
