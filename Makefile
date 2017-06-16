generate_assignment_3 : ph20_hw4.tex plots/figure_1.png plots/figure_2.png \
plots/figure_3.png plots/figure_4.png plots/figure_5.png plots/figure_6.png \
plots/figure_7.png plots/figure_8.png plots/figure_9.png plots/figure_10.png \
plots/figure_11.png plots/figure_12.png plots/figure_13.png \
plots/figure_14.png plots/figure_15.png plots/figure_16.png \
plots/figure_17.png plots/figure_18.png plots/figure_19.png
	touch commandLineOutput.txt >> commandLineOutput.txt
	git log > ph_20_assignment_4_git_log.txt
	cp Makefile makefile_source_code.txt >> commandLineOutput.txt
	cp ph20_hw3_updated.py hw3_source_code.txt >> commandLineOutput.txt
	pdflatex $< >> commandLineOutput.txt

%.png : ph20_hw3_updated.py
	touch commandLineOutput.txt >> commandLineOutput.txt
	mkdir -p plots >> commandLineOutput.txt
	python $< $*.png >> commandLineOutput.txt

.PHONY : clean
clean :
	rm -f ph20_hw4.pdf
	rm -f ph20_hw3.aux
	rm -f ph20_hw3.log
	rm -f ph_20_assignment_4_git_log.txt
	rm -f makefile_source_code.txt
	rm -f hw3_source_code.txt
	rm -f commandLineOutput.txt
	rm -f ph20_hw3.synctex.gz
	rm -r -f plots
