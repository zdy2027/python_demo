#!/usr/bin/env python

class output:

    file_object = open('console.txt','w')
    
    def debug(self,string):
        self.file_object.write("debug:"+string+"\n")
    
    def info(self,string):
        self.file_object.write("info:"+string+"\n")
    
    def waring(self,string):
        self.file_object.write("waring:"+string+"\n")
    
    def error(self,string):
        self.file_object.write("error:"+string+"\n")
    
    def close(self):
        self.file_object.close()
