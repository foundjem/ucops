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
    try:
     with open(pathName, 'r') as myfile:
             msg = myfile.read()
             myfile.closed
    except IOError:
        print "File or Path doesn't exist, exiting application"
        exit(1)

    writeback = header + "\n\n" + msg 
    try:
        f =  open(pathName, 'w')
        f.write(writeback)
        f.close()
    except IOError:
        print "File or Path doesn't exist, exiting application"
        exit(2)  
def main():
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='Processing File paath to script.')
    fileHeader(sys.argv[1])
    
#============END OF FUNCTION fileHeader()==============#insertHeaderFile.py
if __name__ == '__main__':
     main()         
    
    
    
    
    
    