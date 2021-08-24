import lib
import os
import time
from tqdm import tqdm

for i in tqdm(range(10), desc = 'WARNING!!! LOADING TEST SCRIPT', unit= ' init', unit_scale=1):
    time.sleep(0.01)
print('Install additional package')
os.system(lib.ACTION.inst)
os.system(lib.ACTION.instf)
os.system(lib.ACTION.instl)

lib.logs()
lib.net()
lib.stress()
lib.res()