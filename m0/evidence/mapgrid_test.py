import os, struct, math, sys
from coot import *
SYMOPS = ["X,Y,Z","-X,-Y,Z+1/2","-Y+1/2,X+1/2,Z+3/4","Y+1/2,-X+1/2,Z+1/4","-X+1/2,Y+1/2,-Z+1/4","X+1/2,-Y+1/2,-Z+3/4","Y,X,-Z","-Y,-X,-Z+1/2"]
def write_map(path, n, cell, ispg, nsymbt=None):
    sym = b"".join(s.encode().ljust(80) for s in SYMOPS)
    nsymbt = len(sym)
    nx, ny, nz = n
    words = [0]*256
    hdr = bytearray(1024)
    def pi(i, v): struct.pack_into("<i", hdr, 4*i, v)
    def pf(i, v): struct.pack_into("<f", hdr, 4*i, v)
    pi(0,nx); pi(1,ny); pi(2,nz); pi(3,2)
    pi(4,0); pi(5,0); pi(6,0); pi(7,nx); pi(8,ny); pi(9,nz)
    for k,v in enumerate(cell): pf(10+k, v)
    pi(16,1); pi(17,2); pi(18,3)
    pf(19,-1.0); pf(20,1.0); pf(21,0.0)
    pi(22,ispg); pi(23,nsymbt)
    hdr[208:212] = b"MAP "
    hdr[212:216] = bytes([0x44,0x44,0,0])
    pf(54, 0.1); pi(55,0)
    data = bytearray()
    for k in range(nz):
        for j in range(ny):
            for i in range(nx):
                data += struct.pack("<f", math.sin(2*math.pi*i/nx)*math.cos(2*math.pi*j/ny)*math.sin(2*math.pi*k/nz))
    open(path,"wb").write(bytes(hdr)+sym+bytes(data))
d = sys.argv[-1] if os.path.isdir(sys.argv[-1]) else "/tmp"
good = os.path.join(d,"p43212_good.map"); bad = os.path.join(d,"p43212_bad.map")
write_map(good,(36,36,64),(13.177,13.177,23.837,90,90,90),96)
write_map(bad,(45,45,80),(13.177,13.177,23.837,90,90,90),96)
for label,f in (("good",good),("bad",bad)):
    im = handle_read_ccp4_map(f, 0)
    print("MAP", label, "imol", im, "valid", is_valid_map_molecule(im), flush=True)
    if is_valid_map_molecule(im):
        set_rotation_centre(3.0,4.0,5.0)
        print("  recentred", flush=True)
        if label=="good":
            for fac in (1.25, 1.1, 2.0):
                ism = smooth_map(im, fac)
                print("  smooth", fac, "->", ism, flush=True)
                set_rotation_centre(5.0*fac,6.0,7.0)
                print("  recentred after smooth", fac, flush=True)
print("DONE", flush=True)
coot_real_exit(0)
