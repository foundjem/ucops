import sys
print sys.argv
header=""
pathName=""
def fileHeader(pathName):
   
    header = """ /*******************************************************************************
    * Copyright (c) {DATE} {INITIAL COPYRIGHT OWNER} {OTHER COPYRIGHT OWNERS}.
    * All rights reserved. This program and the accompanying materials
    * are made available under the terms of the Eclipse Public License v1.0
    * which accompanies this distribution, and is available at
    * http://www.eclipse.org/legal/epl-v10.html
    *
    * Contributors:
    *    {INITIAL AUTHOR} - initial API and implementation and/or initial documentation
    *******************************************************************************/ """

    with open(pathName, 'r') as myfile:
             msg = myfile.read()
             myfile.closed

    writeback = header + "\n\n" + msg 

    f =  open(pathName, 'w')
    f.write(writeback)
    f.close()
#============END OF FUNCTION fileHeader()==============#
if __name__ == '__main__':
    fileHeader("/home/foundjem/UCOSP/Python/anything.txt")
    
    
    
    