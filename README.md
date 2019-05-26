A script to calculate cpu usage of an LXC (linux containers). It should be easily adopted to Docker or other Cgroup based containers.

Usage:
```
lxc_name=MY_LXC
# Make sure "/sys/fs/cgroup/cpu/lxc/MY_LXC/cpuacct.usage" exists
python cpu_usage.py $lxc_name
```

example outputs:
```
MY_LXC CPU Usage: 0.0%
MY_LXC CPU Usage: 3.95%
MY_LXC CPU Usage: 6.43%
MY_LXC CPU Usage: 3.51%
MY_LXC CPU Usage: 3.65%
...
```
