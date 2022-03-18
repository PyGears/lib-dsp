.PHONY: help
opts =

help:           ## Show this help.
	## options:
		## opts=<pytest options (default options like '-x' '-s' etc...)>
			## '--num=10' -> number of seeds to run per test
			## '--random=1' -> run randomized seeds
			## '--seed=1234' -> run specific seed
			## '--cosim=0' -> disable cosim, by default enabled
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


sanity:			## run all available files once for sanity
	python3 cordic/test/test_cordic_single.py 

	python3 fir/test/test_fir_single.py
	python3 fir/test/test_fir_regression.py

	python3 iir/test/test_iir_regression.py
	python3 iir/test/test_iir_single.py

	python3 matrix_ops/test/test_matrix_ops_regression.py
	python3 matrix_ops/test/test_matrix_ops_single.py

	python3 fft_bf/test/test_fft_bf_single.py

