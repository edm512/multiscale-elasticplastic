import numpy as np
def expansion(VTarget, ExpV, expPathway, expTime, timestep):
    totalSteps = expTime/timestep
    expSteps = np.arange(totalSteps)
    if expPathway == "linear":
        m = (ExpV - VTarget) / totalSteps
        expVol = (m * expSteps) + VTarget
    if expPathway == "quadratic":
        m = (ExpV - VTarget) / totalSteps**2
        expVol = (m * expSteps ** 2) + VTarget
    if expPathway == "squareroot":
        m = (ExpV - VTarget) / totalSteps**0.5
        expVol = (m * expSteps ** 0.5) + VTarget
    if expPathway == "cubic":
        m = (ExpV - VTarget) / totalSteps**3
        expVol = (m * expSteps ** 3) + VTarget
    if expPathway == "sigmoid":
            expVol = (ExpV - VTarget)/(1 + np.exp(-(expSteps-(totalSteps/2))/(totalSteps/(1000*timestep)))) + VTarget
    return expVol
