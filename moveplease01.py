#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/mycode/')
shutil.move('raynor.odj', 'ceph_storage/')
xname = input('What is the new name for kerrigan.odj?')
shutil.move('ceph_storage/kerrigan.odj', 'ceph_storage/' + xname)

# The following line will rename a file
