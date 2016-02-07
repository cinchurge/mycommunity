curr_checksum := $(shell md5 -q requirements.txt)
prev_checksum := $(shell [ -f ./env/MD5SUM ] && cat ./env/MD5SUM)

.PHONY: serve
serve: env
	./env/bin/python main.py

env: bootstrap

.PHONY: bootstrap
bootstrap:
	if [[ "$(curr_checksum)" != "$(prev_checksum)" ]]; then rm -rf env; fi
	if [[ ! -d env ]]; then virtualenv env && md5 -q requirements.txt > ./env/MD5SUM; fi
	./env/bin/pip install pip --upgrade
	./env/bin/pip install -r requirements.txt

