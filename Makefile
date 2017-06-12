generate_assignment_3 : ph20_hw3_updated.py ph20_hw3.tex
	mkdir plots
	python $<
	pdflatex ph20_hw3.tex

.PHONY : clean
clean :
	rm -f ph20_hw3.pdf
	rm -f ph20_hw3.aux
	rm -f ph20_hw3.log
	rm -r plots
