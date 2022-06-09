import os
from os import listdir
from os.path import isfile, join
import pystray
import PIL.Image
from plyer import notification
import hashlib


def is_almost_similar(integer_1,integer_2):
    
    min = integer_1 * 0.8
    max = integer_1 * 1.2
    
    if max >= integer_2 >= min:
        return True
    elif not max >= integer_2 >= min:
        return False
    else:
        print('something went wrong in is_almost_similar function')  
    
    
    
    
def have_similar_extensions(path_1,path_2):
    
    first_file_name, first_file_extension = os.path.splitext(path_1)
    second_file_name, second_file_extension = os.path.splitext(path_2)
    
    
    if first_file_extension == second_file_extension:
        return True
    elif not first_file_extension == second_file_extension:
        return False
    else:
        print('something went wrong in has_similar_extensions function')      
        
     
     
        
def have_similar_sizes(path_1,path_2):
    
    size_1 = os.path.getsize(path_1)
    size_2 = os.path.getsize(path_2)
    
    return is_almost_similar(size_1,size_2)




def is_potentially_the_same(path_1,path_2): 
    
    if have_similar_sizes(path_1,path_2) and have_similar_extensions(path_1,path_2):
        return True
    elif not(have_similar_sizes(path_1,path_2) and have_similar_extensions(path_1,path_2)):
        return False
    else:
        print('something went wrong in is_potentially_the_same function')
        
        
        
def md5(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

     
        
def sending(statement):     
    if statement:
        f1_checksum = str(md5(os.path.dirname(__file__)+'\comparing directory\_first file/'+ file_1))
        f2_checksum = str(md5(os.path.dirname(__file__)+'\comparing directory/second file/'+ file_2))
        
        return 'file 1: ' + f1_checksum + '\n' + 'file 2: ' + f2_checksum
    elif not statement:
        return 'we already know that these files are not the same so there is no need to convert them to checksum code and send them to our servers'
        
    else:
        return 'something went wrong in sending function'
        
        
        
       
def notifyMe(message):
    notification.notify(
        title = 'ARTEMIS Client',
        message = message,
        app_icon = None, 
        timeout = 10,
    )
        
        

_1_list = os.listdir(os.path.dirname(__file__)+'\comparing directory/_first file')
_2_list = os.listdir(os.path.dirname(__file__)+'\comparing directory/second file')
file_1 = str(_1_list[0])
file_2 = str(_2_list[0])


       
def on_click (icon,item):
    if str(item) == 'Compare':
        notifyMe(sending(is_potentially_the_same(os.path.dirname(__file__)+'\comparing directory\_first file/'+ file_1 , os.path.dirname(__file__)+'\comparing directory/second file/'+ file_2)))
    elif str(item) == 'Exit':
        icon.stop()
        
        
        
icon_image = PIL.Image.open(os.path.dirname(__file__)+'/_artemis logo.png')   
tray = pystray.Icon ('ARTEMIS CLIENT MVP' , icon_image , menu=pystray.Menu(pystray.MenuItem('Compare',on_click),pystray.MenuItem('Exit',on_click)))
tray.run()






    
    
    
    
        



    
    


