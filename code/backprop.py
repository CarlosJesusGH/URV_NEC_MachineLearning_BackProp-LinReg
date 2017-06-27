# source ~/Coding/venv/bin/activate

# Now i should create a method for training , another for validate and call them independently
# so I can check different architectures faster
from NeuralNetwork import *
from NN_Settings import *
import time
# Mark start time
startTime = time.clock()

# iniWeights = copy.deepcopy(NN.w)
# iniThresholds = copy.deepcopy(NN.t)
iniNN = copy.deepcopy(NN)
# -----------------------------------
# Default settings
for i in range (1): #(15,18):
    for j in range (1): #(2,21):
        if False:
            # Make a pause before starting new cicle for cooling processor
            time.sleep(5)
            # Changes before starting new cicle
            NN.hiddenLayerSizes[0] = i
            NN.hiddenLayerSizes[1] = j
        # ------------------------
        includeTraining = True
        includeValidate = True
        if includeTraining:
            costs, results, percsError = NN.trainNetwork(NN.epochs, './input/turbine-input-train', False)       # trainDataFile, useInteractivePlot
            NN.plotTraining(costs, percsError, True, True) # showPlot, savePlot
            # NN.plotValidate(results)
        if includeValidate:
            # Validate learning using new unknown set
            print "-----------------------------------"
            print "Now validating"
            results = NN.validateLearning('./input/turbine-input-validate')
            NN.plotValidate(results, True, True)           # showPlot, savePlot
        # ------------------------
        # Changes before next loop
        NN = copy.deepcopy(iniNN)
        # NN.batchSize = NN.batchSize + 20
        print "-----------------------------------"
        print "cicle %dx%d ending time: %f" %(i, j, (time.clock() - startTime))
        print "-----------------------------------"
# ------------------------
# Compute process time and print it
endTime = time.clock()
print "-----------------------------------"
print "Total Time: " + str(endTime - startTime) + "\n======================"
