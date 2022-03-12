.PHONY: start start_build stop unit_tests check_typing unit_tests_local

UNIT_TESTS=pytest tests --asyncio-mode=strict

start:
	@docker-compose up -d

start_build:
	@docker-compose up --build -d

stop:
	@docker-compose down

unit_tests:
	@docker-compose exec app-test \
	$(UNIT_TESTS)

unit_tests_local:
	@$(UNIT_TESTS)

check_lint:
	@docker-compose exec app-test mypy . && isort --check-only . && black --check .

fix_lint:
	@docker-compose exec app-test isort . && black .
