import numpy as np
def compression(VTarget, compPathway, compTime, timestep):
    totalSteps = compTime/timestep
    compSteps = np.arange(totalSteps)
    if compPathway == "linear":
        m = (VTarget-1) / totalSteps
        compVol = (m * compSteps) + 1
    if compPathway == "quadratic":
        m = (VTarget-1) / (totalSteps**2)
        compVol = (m * compSteps ** 2) + 1
    if compPathway == "squareroot":
        m = (VTarget-1) / (totalSteps**0.5)
        compVol = (m * compSteps ** 0.5) + 1
    if compPathway == "cubic":
        m = (VTarget-1) / (totalSteps**3)
        compVol = (m * compSteps ** 3) + 1
    if compPathway == "sigmoid":
        compVol = (-( 1 - VTarget) / (1 + np.exp(-(compSteps-(totalSteps/2))/(compSteps/(1000*timestep)))) ) + 1
    return compVol
    
