.PHONY: help
opts =
logdir = "build/pytest.log"

help:           ## Show this help.
	## options:
		## opts=<pytest options (default options like '-x' '-s' etc...)>
			## '--num=10' -> number of seeds to run per test
			## '--random=1' -> run randomized seeds
			## '--seed=1234' -> run specific seed
			## '--cosim=0' -> disable cosim, by default enabled
		## logdir=<location where to save log>
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


fir_regr:		## run IIR filter test in a regression
	pytest test_fir_regression.py::test_fir_random --num=1 
	pytest test_fir_regression.py::test_fir_random_type --num=50 --random=1 
	pytest test_fir_regression.py::test_fir_limits --num=3 --random=1 
	pytest test_fir_regression.py::test_fir_sine --num=3 --random=1 


sanity:			## run all available files once for sanity
	python3 $(opts) test_fir_regression.py
	python3 $(opts) test_fir_single.py

