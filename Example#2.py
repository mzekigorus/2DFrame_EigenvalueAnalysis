
import openseespy.opensees as ops
import numpy as np

import openseespy.postprocessing.ops_vis as opsv
import matplotlib.pyplot as plt



inch = 1.0
kip = 1.0
sec = 1.0

g = 386.4*inch/sec**2

ft = 12*inch
lb = kip/1000
ksi = kip/inch**2

E = 29500*ksi
v = 0.3
G = 0.5*E/(1+v)


L = 36*ft
H = 36*ft

m = 0.4*kip*sec**2/inch

ops.wipe()
ops.model('basic','-ndm',2,'-ndf',3)

ops.node(1,0,0); ops.fix(1,1,1,1)
ops.node(2,L,0); ops.fix(2,1,1,1)
ops.node(3,0,H/3)
ops.node(4,L,H/3)
ops.node(5,0,2*H/3)
ops.node(6,L,2*H/3)
ops.node(7,0,H)
ops.node(8,L,H)


# Beam depth

d = 24*inch


# Columns(W14X90)

Ac = 26.5*inch**2
Icz = 999*inch**4
Icy = 362*inch**4
J = 4.06*inch**4

ops.section('Elastic',1,E,1000*Ac,Icz,Icy,G,J)
ops.beamIntegration('Legendre',1,1,2)


ops.geomTransf('Linear',1,'-jntOffset',0,0,0,-2*d)



ops.element('forceBeamColumn',1,1,3,1,1)
ops.element('forceBeamColumn',2,3,5,1,1)
ops.element('forceBeamColumn',3,5,7,1,1)
ops.element('forceBeamColumn',4,8,6,1,1)
ops.element('forceBeamColumn',5,6,4,1,1)
ops.element('forceBeamColumn',6,4,2,1,1)


# Beams

b = 12*inch
Ab = b*d
Ibz = b*d**3/12
Iby = d*b**3/12
Jb = Ibz+Iby

ops.section('Elastic',3,1000*E,Ab,Ibz,Iby,1000*G,Jb)
ops.beamIntegration('Legendre',3,3,3)

ops.element('forceBeamColumn',7,3,4,1,3)
ops.element('forceBeamColumn',8,5,6,1,3)
ops.element('forceBeamColumn',9,7,8,1,3)


ops.mass(3,m/2,0,0)
ops.mass(4,m/2,0,0)
ops.mass(5,m/2,0,0)
ops.mass(6,m/2,0,0)
ops.mass(7,m/2,0,0)
ops.mass(8,m/2,0,0)


ops.equalDOF(3,4,2,3)
ops.equalDOF(5,6,2,3)
ops.equalDOF(7,8,2,3)

# Eigenvalue Analysis
omegaSquared = ops.eigen('fullGenLapack',3)
omega1 = (omegaSquared[0])**0.5
omega2 = (omegaSquared[1])**0.5
omega3 = (omegaSquared[2])**0.5
# Natural Periods
T1 = 2*np.pi/omega1
T2 = 2*np.pi/omega2
T3 = 2*np.pi/omega3
print(T1,T2,T3)


opsv.plot_mode_shape(1)
#opsv.plot_mode_shape(2)
#opsv.plot_mode_shape(3)






