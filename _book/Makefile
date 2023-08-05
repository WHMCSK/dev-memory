common:
	rm -rf _book
	rm -rf book

serve gitbook:common
	gitbook build
	gitbook serve

gitbook-build:common
	gitbook build

serve mdbook:common
	mdbook build
	mdbook serve --open

mdbook-build:common
	mdbook build

build:common mdbook-build gitbook-build
	echo "build all"
