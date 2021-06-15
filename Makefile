#
# based on Kevin Webb's asciidoc setup
#
all: README.html

README.html: *.adoc
	asciidoctor -a linkcss -a stylesheet=cs21.css -a stylesdir=./style -v -o README.html README.adoc

.PHONY: all clean 

clean:
	-rm README.html

