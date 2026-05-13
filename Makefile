#

include PID

-include ../template/Makefile.PID


# addition PID specific targets can be created here

hack:
	# step1: only bank=1
	grep _freq2 *run1a > hack1a.run
	grep _freq2 *run1b > hack1b.run
	grep _freq2 *run2  > hack1c.run
	@echo rename 155800_155812  to __CO
	@echo rename 156134_156499  to __CN
	# step2: only bank=0
	grep MWC1_13co *run1a > hack2a.run
	grep MWC1_13co *run1b > hack2b.run
	grep MWC1_13co *run2  > hack2c.run
	@echo rename 155800_156499 to __13CO
	# step3: only bank=0
	grep MWC1_c18o *run1a > hack3a.run
	grep MWC1_c18o *run1b > hack3b.run
	grep MWC1_c18o *run2  > hack3c.run
	@echo rename 155800_156499 to __C18O

