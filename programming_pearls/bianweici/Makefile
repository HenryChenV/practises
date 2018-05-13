all: build

build: sign squash

sign: sign.c
	clang $< -o $@

squash: squash.c
	clang $< -o $@

clean:
	rm -vf sign squash

test:
	./sign < dictionary | sort | ./squash > gramlist
	@echo
	@echo "gramlist:"
	@echo
	@cat gramlist
	@echo
