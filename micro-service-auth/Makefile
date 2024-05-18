ifeq (revision,$(firstword $(MAKECMDGOALS)))
	# use the rest as arguments for run
	RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
	# ... and turn them into do-nothing targets
	$(eval $(RUN_ARGS):;@:)
endif

.PHONY: start revision migrate

start:
	python src/main.py

rev:
	alembic revision --autogenerate -m "Added account table"

mig:
	alembic upgrade head

st:
	ruff . --fix

test:
	python seed/create_data_test.py
