class Retry:
    def __init__(self, backoff, retries, supported_errors=...) -> None: ...
    def update_supported_erros(self, specified_errors) -> None: ...
    def call_with_retry(self, do, fail): ...
