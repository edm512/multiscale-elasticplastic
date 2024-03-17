variable fvol1 file g4_280322_Cu_ts0.01scaledvol.txt
variable normvol equal v_fvol1
variable normvoladvance equal next(fvol1)

variable frate1 file g4_280322_Cu_ts0.01gradvol.txt
variable rate equal v_frate1
variable rateadvance equal next(frate1)

variable displace equal "-(v_L0 - (v_L0 * v_normvol))"
variable ddx equal "-(v_L0 * v_rate)"
fix 2 all deform 1 z variable v_displace v_ddx remap x

fix data2 all print 1 "${step}, ${normvoladvance}, ${rateadvance}" file test.output

thermo 100
thermo_style custom step pxx pyy pzz v_temp2d v_ramp_step v_normvol v_rate lz v_displace v_ddx
thermo_modify flush yes

fix data all print 10 "${step}, ${time}, ${volume}, ${temp2d}, ${Pxx}, ${Pyy}, ${Pzz}, ${Pxy}, ${Pxz}, ${Pyz}, ${Lz}, ${density}, ${tempall}, ${Vx}, ${Vy}, ${Vz}, ${displace}, ${ddx}, ${Sx}, ${Sy}, ${Sz}" file volmap_${run_name}.txt


