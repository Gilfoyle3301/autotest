#!/bin/python3
# -*- coding: utf-8 -*
import os
import subprocess
import shlex

class LOG:
    CreatLog = 'astra-create-debug-logs'
    CreatLSHW = 'lshw -html -sanitize -numeric > Result/lswh_info.html'
    CreatLSPCI_NET = 'lspci -k | grep -i -EA2 net > Result/pci_info.txt'
    CreatLSPCI_VGA = 'lspci -v | grep -i VGA > Result/vga_info.txt'
    CreatAPLAY = 'aplay -l >  Result/aplay_info.txt'
    CreatCPUINFO = 'cat /proc/cpuinfo > Result/base_cpu.txt'
    CreatCPUl= 'lscpu > Result/info_lscpu.txt'
    GLX_INF = 'glxinfo | grep -i renderer > Result/info_renderer.txt'
    GL = 'glxinfo -B > Result/glxinfo.txt'

class INFO:
    CallTrace = 'grep -i calltrace /var/log/kern.log'
    GLX = 'glxinfo | grep -i Accelerated'
    GLX_GL = 'glxinfo | grep OpenGL > Result/glxinfo.txt'

class NET:
    CreatPing = 'ping -s 1400 -i 0.1 -c 10 10.77.80.77'
    CreatIPERF = "script -c 'iperf -c 10.77.80.77 -P 100 -r -t 100' Result/ip_info.txt" 

class ACTION:
    MV = 'mv /tmp/astra-logs-* Result/'
    ARH = 'tar -czf Result.tar.gz Result/*'
    CallTrace = 'grep -i calltrace /var/log/kern.log'
    GRAPHICS = 'phoronix-test-suite benchmark gputest < Ans#1.txt > Result/Graph_info.txt '
    CPU = 'MONITOR=cpu.temp phoronix-test-suite benchmark cryptopp < Ans#2.txt > Result/TestCPU_info.txt'
    RAM = 'phoronix-test-suite benchmark sqlite < Ans#3.txt > Result/TestGPU_info.txt'
     
    
class install:
    inst = 'cd data && sudo apt -y install ./*.deb && sudo apt -y install -f' 
    instnet = 'sudo apt -y install lshw iperf'
    

#INFO AND LOG
def logs():
    if (os.system(ACTION.CallTrace)) != 256:
           print ("Обнаруженны CallTraces")
    else:
        os.system(LOG.CreatLog)
        os.system(ACTION.MV)

    #SYSTEM INFORMATION
    os.system(LOG.CreatLSHW)  
    os.system(LOG.CreatCPUINFO)
    os.system(LOG.CreatCPUl)
    os.system(LOG.CreatLSPCI_NET)
    #SOUND
    os.system(LOG.CreatAPLAY)
    #GRAPHICS
    os.system(LOG.CreatLSPCI_VGA)
    os.system(LOG.GLX_INF)
    os.system(LOG.GL)
    os.system(INFO.GLX)
    
#NETWORK
def net():
    try:
        subprocess.check_output(shlex.split(NET.CreatPing))
        print('Соединение установлено, производится анализ пропускной способности сети')
        subprocess.check_output(shlex.split(NET.CreatIPERF))
        print('connection close')
    except subprocess.CalledProcessError: 
        print('Соединение не установленно или разорвано, устраните проблему')

#STRESS TESTING
def stress():
    print("RUN TEST GRAPHICS")
    os.system(ACTION.GRAPHICS)
    print("RUN TEST RAM")
    os.system(ACTION.RAM)
    print("RUN TEST CPU")
    os.system(ACTION.CPU)


#CREAT RESULT
def res():
    os.system(ACTION.ARH)





   