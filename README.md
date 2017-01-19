# pms5003-g5
read pm data from pms5003 g5 sensor with python

# install and run

install python modules

    apt-get install python-pip python-serial

choose your tty device (ttyUSB0 or ttyAMA0)
update g5.py last line

    print air.read("/dev/ttyAMA0") // update device

give a try

    python g5.py

output data format:

    [pm10_cf,pm25_cf,pm100_cf,pm10,pm25,pm100,particle03,particle05,particle10,particle25,particle50,particle100]

read sensor data periodically:

    python monitor.py

# to stop  sysrq: SysRq : HELP : ...... messag
    echo 0 > /proc/sys/kernel/sysrq
