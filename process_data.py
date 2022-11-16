import os
from pathlib import Path

# data  
shroomPath='D:\projects\mushrooms\mushrooms_train'
shroomNames=['Agaricus',
            'Amanita',
            'Boletus',
            'Cortinarius',
            'Entoloma',
            'Hygrocybe',
            'Lactarius',
            'Russula',
            'Suillus']
#6039 pictures
#endregion

def countPictures():
    shroomCnt=0
    for name in shroomNames:
        tempPath=Path(shroomPath+'/'+name)
        files=list(tempPath.rglob("*.*"))
        speciesCnt=0
        for file in files:
            speciesCnt+=1
        print(f"Found {speciesCnt} pictures of {str(name)}.")
        shroomCnt+=speciesCnt
    
    print(f"Found {shroomCnt} mushroom pictures in total.")

def renamePictures():
    for name in shroomNames:
        speciesCnt=0
        mushroomPath=Path(shroomPath+'/'+name)
        files=list(mushroomPath.rglob("*.*"))
        for file in files:
            newName= str(mushroomPath)+'/'+name+str(speciesCnt)+'.jpg'
            os.rename(file,newName)
            speciesCnt+=1
            
    
if __name__=="__main__":

    countPictures() #6039
    #renamePictures()
