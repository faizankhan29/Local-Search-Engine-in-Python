import os
fn = open("Name.searchenginedb", "w")
fs = open("Size.searchenginedb", "w")
ff = open("Format.searchenginedb", "w")
fp = open("Path.searchenginedb", "w")
container = 'p'
my_list = []
for (dir, _, files) in os.walk("./"):
    for f in files:
        path = os.path.join(dir, f)
        if os.path.exists(path):
            container = path
            if(container.rsplit(".",1)[1] != "searchenginedb"):  
                fp.write(path)
                fp.write('\n')
                fsize = os.path.getsize(path)
                fname = container.rsplit( ".", 1 )[ 0 ]
                fs.write(str(fsize))
                fs.write('\n')                
                fname = container.rsplit( ".", 1 )[ 0 ]
                fname = fname.rsplit( "/", 1 )[ 1 ]
                if "\\" in fname:
                    fname = fname.rsplit( "\\", 1 )[ 1 ]
                fname = fname.lower()
                fn.write(fname)
                fn.write('\n')
                my_list.append(fname)                
                ext = container.rsplit( ".", 1 )[ 1 ]
                ext = ext.lower()
                ff.write(ext)
                ff.write('\n')
fp.close()
fs.close()
fn.close()
ff.close()
