import os
import shutil
from pathlib import Path
import platform

#input file path that needs to be repacked
pack = input('what needs repacking, kid? ')
folders = os.listdir(pack)

for root, dirs, files in os.walk(pack, topdown=True):
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
                        if not platform.system() == 'Windows':
                            os.system('rsync -a -h --progress --stats --checksum --exclude=".*" --exclude="~*" --log-file='
                            + os.path.join(pack, 'rsync.log')
                            + " " + fpath + " " + newmeta)
                        else:
                            shutil.move(fpath, newmeta)

                else:
                    objfold = str(Path(fpath).parents[2])
                    objfold = os.path.split(objfold)
                    objname = objfold[1]
                    newsubdoc = os.path.join(pack, 'metadata', 'submissionDocumentation', objname)
                    if not os.path.exists(newsubdoc):
                        os.makedirs(newsubdoc)
                    if not os.path.exists(os.path.join(newsubdoc, name)):
                        if not platform.system() == 'Windows':
                            os.system('rsync -a -h --progress --stats --checksum --exclude=".*" --exclude="~*" --log-file='
                            + os.path.join(pack, 'rsync.log')
                            + " " + fpath + " " + newsubdoc)
                        else:
                            shutil.move(fpath, newsubdoc)
        else:
            if 'access' not in fpath:
                parent_dir = str(Path(fpath).parents[1])
                if not platform.system() == 'Windows':
                    os.system('rsync -a -h --progress --stats --checksum --exclude=".*" --exclude="~*" --log-file='
                    + os.path.join(pack, 'rsync.log')
                    + " " + fpath + " " + parent_dir)
                else:
                    shutil.move(fpath, parent_dir)
            else:
                objfold = str(Path(fpath).parents[2])
                objfold = os.path.split(objfold)
                objname = objfold[1]
                newaccess = os.path.join(pack, 'access', objname)
                if not os.path.exists(newaccess):
                    os.makedirs(newaccess)
                if not os.path.exists(os.path.join(newaccess, name)):
                    if not platform.system() == 'Windows':
                        os.system('rsync -a -h --progress --stats --checksum --exclude=".*" --exclude="~*" --log-file='
                        + os.path.join(pack, 'rsync.log')
                        + " " + fpath + " " + newaccess)
                    else:
                        shutil.move(fpath, newaccess)

for fname in folders:
    shutil.rmtree(os.path.join(pack, fname, 'objects'))
    shutil.rmtree(os.path.join(pack, fname, 'metadata'))

if os.path.exists(os.path.join(pack, 'rsync.log')):
    shutil.move(os.path.join(pack, 'rsync.log'), os.path.join(pack, 'metadata', 'submissionDocumentation'))
