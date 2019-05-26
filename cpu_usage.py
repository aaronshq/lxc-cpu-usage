#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: shanhanqiang

import time
import sys
import subprocess


class CPU():

    def __init__(self, cpuacct_file):
        self.cpuacct_file = cpuacct_file
        self.last_total_time = self.get_total_time()
        self.last_use_time = self.get_use_time()

    def get_total_time(self):
        """get total time elapsed, in nanoseconds
        """
        try:
            # time_ns() only supported by python 3.7
            use_time = time.time_ns()
        except Exception:
            use_time = subprocess.check_output(['date', '+%s%N'])

        return int(use_time)

    def get_use_time(self):
        """get use time elapsed, in nanoseconds
        """
        with open(self.cpuacct_file, 'r') as f:
            total_time = int(f.read())
        return total_time

    def get_cpu_usage(self):
        current_total_time = self.get_total_time()
        current_use_time = self.get_use_time()

        incr_use_time = current_use_time - self.last_use_time
        incr_total_time = current_total_time - self.last_total_time
        usage = incr_use_time / incr_total_time

        self.last_total_time = current_total_time
        self.last_use_time = current_use_time

        return usage

def main():

    if len(sys.argv) < 2:
        print("Error: need a name of lxc")
        print("python cpu_usage.py lxc_name")

    lxc_name = sys.argv[1]
    cpuacct_usage_file = "/sys/fs/cgroup/cpu/lxc/{}/cpuacct.usage".format(lxc_name)
    cpu = CPU(cpuacct_usage_file)
    while True:
        cpu_usage = round(cpu.get_cpu_usage() * 100, 2)
        print("{} CPU Usage: {}".format(lxc_name, cpu_usage))
        time.sleep(1)

if __name__ == '__main__':
    main()

