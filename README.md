# iTerm2 Change Background Image Script

## Overview

This is an iTerm2 script. It changes the 
terminal background image by updating
the current profile's preferences. 

The script is designed to be triggered
manually from the top menu. When it is
the preferences are updated to point
to a specific file. 

## Installation

Installing the script is done by putting
it in:

```
~/Library/ApplicationSupport/iTerm2/Scripts
```

Restart iTerm2 after the script is in 
place to complete the installation. 

## Usage

Once you've put the script in place you trigger
it by selecting it from the "Scripts" menu
in the top bar.


## Image File

The script is a prototype. It's hard-coded to 
point at:

```
~/Desktop/iterm2-background.jpg
```

You'll want to have an image at that
path before running the script.


## Changing The Image

There are two ways to change the image:

1. Update the `image_path` variable
   in the script to point to a new location.

2. Overwrite the `~/Desktop/iterm2-background.jpg`
   file with a new image.

If you do the overwrite the new image
will show up the next time you open a new
tab. That behavior can be used to automatically
change images without having to update the
preferences.

I've got a project to do that too.

TODO: Link up to 2ly1b8hlmbfd when it's ready


## References

- (iTerm2 Profile Docs)[https://iterm2.com/python-api/profile.html#iterm2.Profile.async_set_background_image_location]
