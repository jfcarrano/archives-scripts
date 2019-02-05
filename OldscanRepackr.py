import os
import shutil
import bagit
from pathlib import Path


#input file path that needs to be repacked
pack = input('what needs repacking, kid? Point to the data in the bag if you need to, got it? ')
folders = os.listdir(pack)

for root, dirs, files in os.walk(pack, topdown=True):
    for names in dirs:
        dpath = os.path.join(root, names)
        #print(dpath)
    for name in files:
        fpath = os.path.join(root, name)
        #gets full path to filenames
        if 'objects' not in fpath:
            if os.path.join(pack, 'metadata') not in fpath:
                if 'submissionDocumentation' not in fpath:
                    objfold = str(Path(fpath).parents[1])
                    objfold = os.path.split(objfold)
                    objname = objfold[1]
                    newmeta = os.path.join(pack, 'metadata', objname)
                    if not os.path.exists(newmeta):
                        os.makedirs(newmeta)
                    if not os.path.exists(os.path.join(newmeta, name)):
                        shutil.move(fpath, newmeta)

                else:
                    objfold = str(Path(fpath).parents[2])
                    objfold = os.path.split(objfold)
                    objname = objfold[1]
                    newsubdoc = os.path.join(pack, 'metadata', 'submissionDocumentation', objname)
                    if not os.path.exists(newsubdoc):
                        os.makedirs(newsubdoc)
                    if not os.path.exists(os.path.join(newsubdoc, name)):
                        shutil.move(fpath, newsubdoc)
        else:
            if 'access' not in fpath:
                parent_dir = str(Path(fpath).parents[1])
                shutil.move(fpath, parent_dir)
            else:
                parent_dir = str(Path(fpath).parents[2])
                access = str(Path(fpath).parents[0])
                shutil.move(access, parent_dir)

for fname in folders:
    if 'metadata' not in fname:
        os.rmdir(os.path.join(pack, fname, 'objects'))
        shutil.rmtree(os.path.join(pack, fname, 'metadata'))
