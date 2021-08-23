#!/bin/python3
# -*- coding: utf-8 -*
import os
import subprocess
import lib
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
    CreatIPERF = "script -c 'iperf -c 10.77.80.77 -P 100 -r -t 100' > Result/ip_info.txt" 

class ACTION:
    MV = 'mv /tmp/astra-logs-* Result/'
    ARH = 'tar -czf Result.tar.gz Result/*'
    CallTrace = 'grep -i calltrace /var/log/kern.log'
    GRAPHICS = 'phoronix-test-suite benchmark gputest < Ans#1.txt > Graph_info.txt '
    CPU = 'MONITOR=cpu.temp,cpu.voltage phoronix-test-suite benchmark openssl < Ans#2.txt > Result/TestCPU_info.txt'
    RAM = 'phoronix-test-suite benchmark sqlite < Ans#3.txt > Result/TestGPU_info.txt'
    TST = 'phoronix-test-suite benchmark pybench < Ans#3.txt > Result/TestTST_info.txt'

#INFO AND LOG
def logs():
    if (os.system(lib.ACTION.CallTrace)) != 256:
           print ("Обнаруженны CallTraces")
    else:
        os.system(lib.LOG.CreatLog)
        os.system(lib.ACTION.MV)

    #SYSTEM INFORMATION
    os.system(lib.LOG.CreatLSHW)  
    os.system(lib.LOG.CreatCPUINFO)
    os.system(lib.LOG.CreatCPUl)
    os.system(lib.LOG.CreatLSPCI_NET)
    #SOUND
    os.system(lib.LOG.CreatAPLAY)
    #GRAPHICS
    os.system(lib.LOG.CreatLSPCI_VGA)
    os.system(lib.LOG.GLX_INF)
    os.system(lib.LOG.GL)
    os.system(lib.INFO.GLX)
    
#NETWORK
def net():
    try:
        subprocess.check_output(shlex.split(lib.NET.CreatPing))
        print('Соединение установлено, производится анализ пропускной способности сети')
        subprocess.check_output(shlex.split(lib.NET.CreatIPERF))
        print('connection close')
    except subprocess.CalledProcessError: 
        print('Соединение не установленно или разорвано, устраните проблему')

#STRESS TESTING
def stress():
    os.system(lib.ACTION.GRAPHICS)
    os.system(lib.ACTION.RAM)
    os.system(lib.ACTION.TST)
    os.system(lib.ACTION.CPU)

#CREAT RESULT
def res():
    os.system(lib.ACTION.ARH)





   