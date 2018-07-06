import os

mypath = "/Users/ishaqidris/desktop/" #change to desktop directory
desktop = os.listdir(mypath)
screenshot_folder = "/Users/ishaqidris/desktop/screenshots/"

for file in desktop:
    
    #Tidy up screenshot files
    if file.startswith("Screen Shot"):
        print (file)
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)

        os.rename(mypath + file, screenshot_folder + file )

