#!/usr/bin/python

# collectd_cpu_all.py

# collectd cpu_all exec plugin

# usage:
# cpu_all RS_INSTANCE_UUID Interval
#
# e.g. cpu_all 01-06A0KORKK0I1E 15

import psutil
import time
import sys

x = 1

while True:
	cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
	cpu_avg = sum(cpu_usage) / float(len(cpu_usage))
	timenow = str(time.time()).split('.')[0]

	#print 'CPU cores count: '+str(len(cpu_usage))
	#print cpu_avg

	print 'PUTVAL '+sys.argv[1]+'/cpu_all/gauge-average '+timenow+':'+str(cpu_avg)
	print 'PUTVAL '+sys.argv[1]+'/cpu_all/gauge-cores '+timenow+':'+str(len(cpu_usage))

	x += 1
	time.sleep(float(sys.argv[2]))