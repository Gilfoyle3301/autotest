import tqdm
import time
import MExam

execute = [MExam.logs(),MExam.net(),MExam.stress(),MExam.res()]

for i in tqdm(range(execute)):
    time.sleep(1)