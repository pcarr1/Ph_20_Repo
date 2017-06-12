generate_assignment_3 : ph20_hw3.tex plot_1.png plot_2.png plot_3.png \
plot_4.png plot_5.png plot_6.png plot_7.png plot_8.png plot_9.png plot_10.png \
plot_11.png plot_12.png plot_13.png plot_14.png plot_15.png plot_16.png \
plot_17.png plot_18.png plot_19.png
	touch commandLineOutput.txt >> commandLineOutput.txt
	git log > ph_20_assignment_4_git_log.txt
	cp Makefile makefile_source_code.txt >> commandLineOutput.txt
	cp ph20_hw3_updated.py hw3_source_code.txt >> commandLineOutput.txt
	pdflatex ph20_hw3.tex >> commandLineOutput.txt

%.png : ph20_hw3_updated.py
	touch commandLineOutput.txt >> commandLineOutput.txt
	mkdir -p plots >> commandLineOutput.txt
	python ph20_hw3_updated.py $*.png >> commandLineOutput.txt

.PHONY : clean
clean :
	rm -f ph20_hw3.pdf
	rm -f ph20_hw3.aux
	rm -f ph20_hw3.log
	rm -f ph_20_assignment_4_git_log.txt
	rm -f makefile_source_code.txt
	rm -f hw3_source_code.txt
	rm -f commandLineOutput.txt
	rm -f ph20_hw3.synctex.gz
	rm -r -f plots
