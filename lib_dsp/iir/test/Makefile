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

iir:			## run IIR filter tests once
	pytest $(opts) test_iir_regression.py  --num 2

sanity:			## run all available files once for sanity
	python3 $(opts) test_iir_regression.py
	python3 $(opts) test_iir_single.py

