#!/usr/bin/env python -i

from lammps import lammps

import sys

from random import randint

argv = sys.argv
if len(argv) != 4:
  print(argv)
  print("Syntax: runLammps.py runName totalSteps voidSize")
  sys.exit()

runName = argv[1]
totalSteps = argv[2]
voidSize = argv[3]

print('runName: '+runName)
print('totalSteps: '+totalSteps)
print("Running Lammps")

lmp = lammps()
lmp.file("in.part1a")
lmp.command("velocity all create 600 "+str(randint(1, 99999))+" rot yes dist gaussian")
lmp.file("in.part1b")
lmp.command("variable run_name string "+runName)
lmp.command("variable fvol1 file volratio.txt")
lmp.command("variable normvol equal v_fvol1")
lmp.command("variable normvoladvance equal next(fvol1)")
lmp.command("variable frate1 file volrate.txt")
lmp.command("variable rate equal v_frate1")
lmp.command("variable rateadvance equal next(frate1)")
lmp.file("in.part2")
lmp.command("variable voidSize equal "+str(voidSize))
lmp.command("region void1 sphere 70.0 130.0 90.0 "+str(voidSize)+" side in units box")
lmp.command("group void1 region void1")
lmp.command("delete_atoms group void1")
lmp.command("run "+totalSteps)
lmp.close()


