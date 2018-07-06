import os

mypath = "/Users/ishaqidris/desktop/" #change to desktop directory
desktop = os.listdir(mypath)

#add output folders
screenshot_folder = "/Users/ishaqidris/desktop/screenshots/"
media_folder = "/Users/ishaqidris/desktop/media/"

for file in desktop:
    
    #Tidy up screenshot files
    if file.startswith("Screen Shot"):
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)

        os.rename(mypath + file, screenshot_folder + file )

    #Tidy up media files
    elif file.lower().endswith((('.png', '.jpg', '.mp4', '.mov' ))):
        if not os.path.exists(media_folder):
            os.makedirs(media_folder)
        
        os.rename(mypath + file, media_folder + file )

