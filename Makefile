#
# based on Kevin Webb's asciidoc setup
#
all: index.html

index.html: *.adoc
	asciidoctor -a linkcss -a stylesheet=cs21.css -a stylesdir=./style -v -o index.html index.adoc

.PHONY: all clean 

clean:
	-rm index.html

