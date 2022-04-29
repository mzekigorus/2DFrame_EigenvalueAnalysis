# 2DFrame_EigenvalueAnalysis

In this self-study , I code a basic script to calculate and verify free vibration(eigenvalue)analysis which gives the natural vibration properties based on the distribution of stiffness and mass and also, I want to show OpenSees can give the same periods and mode shapes reported in the ETABS verification example.

Modeling assumptions such as;

- Neglect shear and axial deformation in the columns
- Beams are infinitely rigid
- Columns have rigid joint offsets equal to the beam depth
- Columns are completely fixed at their base

After the creation model, with this distribution of mass,the natural periods are calculated.

According to the results, OpenSees model is a bit stiffer in all modes compared to the ETABS values. So then, if you can make overtures and bring a different approach such as rigid offset,axial rigidity,beam stiffness,mass distribution,etc. you will get conservative results in comparison with the theoretical results.

Lastly, if you pursue OpenSees like go chasing the white rabbit, you can have control over how you store the matrices and the solvers used to calculate equilibria, you can have an idea of the overall concept of defining time series in combination with any kind of load patterns to apply a sequence of loading conditions on a structure,the formulation of the force-based or displacement-based frame elements. And so many other well-rounded things.
