generate_assignment_3 : ph20_hw3.tex plot_1.png plot_2.png plot_3.png \
plot_4.png plot_5.png plot_6.png plot_7.png plot_8.png plot_9.png plot_10.png \
plot_11.png plot_12.png plot_13.png plot_14.png plot_15.png plot_16.png \
plot_17.png plot_18.png plot_19.png
	pdflatex ph20_hw3.tex

%.png : ph20_hw3_updated.py
	mkdir -p plots
	python ph20_hw3_updated.py $*.png

.PHONY : clean
clean :
	rm -f ph20_hw3.pdf
	rm -f ph20_hw3.aux
	rm -f ph20_hw3.log
	rm -r -f plots
