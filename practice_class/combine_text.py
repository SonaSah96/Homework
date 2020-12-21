import os

def combine_all_textes():
    abs_path = os.getcwd()
    with open(os.path.join(abs_path, "combine.txt"), "w") as f:
        for root, directories, files in os.walk("."):
            for name in files:
                if name.endswith(".txt"):
                    #if root != ".":
                        #name = root[2:] + "/" + name
                    with open(os.path.normpath(f'{root}/{name}'), 'r') as rf:
                        context = rf.read()
                        f.write(context)



combine_all_textes()