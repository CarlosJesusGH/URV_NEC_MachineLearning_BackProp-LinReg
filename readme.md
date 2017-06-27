# General description
Prediction with Back-Propagation and Linear Regression

### Objective
Prediction of the power of the turbine of a hydro-electrical plant, using the following
algorithms:
* Back-Propagation (BP), implemented by the student
* Multiple Linear Regression (MLR), using free software

### Data
* File: turbine.txt
* Columns: 4 variables, 1 value t	- predict
	- Variables:
		- Height above sea level
		- Fall
		- Net fall
		- Flux
	- Prediction:
		- Power of the turbine
* Patterns: 451 patterns
	- Training and Validation (and cross-validation): the first 401 patterns
	- Test: the remaining 50 patterns

### Parameters
* Try different values of the training parameters and select those with the best
results:
	- Architecture of the neural network
	- Type of scaling of the data
	- Initial range of weights and thresholds
	- Learning rate and Momentum
	- Batched/online
	- Number of training epochs
