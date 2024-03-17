def writeInput(modelName):
	inputScript = open("inputs/in."+modelName, "w")
	inputScript.write("integrateML 2E-9 8960 0.46E11 6.0 ./models/"+str(modelName)+"\n")
	inputScript.write("velocityRamp 1100 1.0e-10\n")
	inputScript.write("dump time 10E-12 "+modelName+ " sigma_r U r V epsilonDot1 s1 s2 s3 q E P Pzz P2d T dPzzdt dP2ddt\n")
	inputScript.write("celldump 100 "+modelName+" sigma_r U r V epsilonDot1 s1 s2 s3 q E P Pzz P2d dPzzdt dP2ddt\n")
	inputScript.write("mesh 500\n")
	inputScript.write("log 100 time-elapsed energy-sum\n")
	inputScript.write("run time 130e-12\n")
	inputScript.close()



