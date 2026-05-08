#

include PID

-include ../template/Makefile.PID


# addition PID specific targets can be created here

hack:
	# step1
	grep _freq *run1a > hack1a.run
	grep _freq *run2  > hack1b.run
	@echo rename 155800_155812  to __CO
	@echo rename 156134_156163  to __CN
	# step2
	grep MWC1_13co *run1a > hack2a.run
	grep MWC1_13co *run2  > hack2b.run
	@echo rename 155800_156163 to __13CO
	# step3
	grep MWC1_c18o *run1a > hack3a.run
	grep MWC1_c18o *run2  > hack3b.run
	@echo rename 155800_156163 to __C18O

