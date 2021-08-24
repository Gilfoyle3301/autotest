import lib
import os

os.mkdir('Result')
os.mkdir('data')
os.system(lib.ACTION.inst)
os.system(lib.ACTION.instf)
os.system(lib.ACTION.instl)

lib.logs()
lib.net()
lib.stress()
lib.res()