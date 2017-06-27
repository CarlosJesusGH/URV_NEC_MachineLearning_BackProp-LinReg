from NeuralNetwork import *

# --- Initialize NN object ---------------------
NN = NeuralNetwork()
# Network architecture
NN.inputLayerSize = 4
NN.outputLayerSize = 1
NN.numberHiddenLayer = 2
NN.hiddenLayerSizes = [9,3]         #9,3
#
NN.epochs = 1000000 #1000000
NN.scalar = 0.3
NN.momentum = 0.9
NN.batchSize = 1    # 0 means entire data
# Other settings
# NN.training = False
NN.verbose = 1      # 1 prints cost for every 1000 epochs / 2 prints everything
NN.plot = True
NN.checkWithNumericalGradients = False
NN.randomSeed = 1  # Seed random numbers
# NN.trainDataFile = './input/turbine-input-train'
# NN.validataDataFile = './input/turbine-input-validate'
# NN.trainDataFile = './input/turbine-input-complete'
# NN.trainDataFile = './input/train'
# NN.validataDataFile = './input/validate'
# NN.readDataAndNormalize(NN.trainDataFile, True)
