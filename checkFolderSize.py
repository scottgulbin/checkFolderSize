import os


def checkFolder(dir, size):
    try:
        for filename in os.listdir(dir):
            fullDir = os.path.join(dir, filename)
            if os.path.isdir(fullDir):
                size += checkFolder(fullDir, 0)
            else:
                size += os.path.getsize(fullDir)
    except Exception as inst:
        # Alerts if there was an error accessing a specific directory
        print(f'Error accessing {dir} because of {inst}')
        return 0
    return size

directorySize = {}

# get directory sizes and add them to a dictionary
dir = 'C:\\Program Files'
for filename in os.listdir(dir): 
    size = 0
    fullDir = os.path.join(dir, filename)
    if os.path.isdir(fullDir):
        size += checkFolder(fullDir, 0)
    else:
        size += os.path.getsize(fullDir)
    directorySize[filename] = size
    
    # Gives status on which folders in the main directory have been searched
    print(f'Done with {fullDir}')        
    
    
print('Done searching, sorting has started')
# Number of results
largestN = 5

#Sort dictionary
sorted_directory_size = sorted(directorySize.items(), key=lambda x:x[1], reverse=True)
print(sorted_directory_size[:largestN-1])
            
        
            