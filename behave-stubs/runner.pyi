from _typeshed import Incomplete
from behave._types import ExceptionUtil as ExceptionUtil
from behave.capture import CaptureController as CaptureController
from behave.configuration import ConfigError as ConfigError
from behave.formatter._registry import make_formatters as make_formatters
from behave.runner_util import PathManager as PathManager, collect_feature_locations as collect_feature_locations, exec_file as exec_file, load_step_modules as load_step_modules, parse_features as parse_features
from collections.abc import Generator

class CleanupError(RuntimeError): ...
class ContextMaskWarning(UserWarning): ...

class Context:
    BEHAVE: str
    USER: str
    FAIL_ON_CLEANUP_ERRORS: bool
    feature: Incomplete
    text: Incomplete
    table: Incomplete
    stdout_capture: Incomplete
    stderr_capture: Incomplete
    log_capture: Incomplete
    fail_on_cleanup_errors: Incomplete
    def __init__(self, runner) -> None: ...
    @staticmethod
    def ignore_cleanup_error(context, cleanup_func, exception) -> None: ...
    @staticmethod
    def print_cleanup_error(context, cleanup_func, exception) -> None: ...
    def use_with_user_mode(self): ...
    def user_mode(self): ...
    def __getattr__(self, attr): ...
    def __setattr__(self, attr, value) -> None: ...
    def __delattr__(self, attr) -> None: ...
    def __contains__(self, attr) -> bool: ...
    def execute_steps(self, steps_text): ...
    def add_cleanup(self, cleanup_func, *args, **kwargs) -> None: ...

def use_context_with_mode(context, mode) -> Generator[None]: ...
def scoped_context_layer(context, layer_name: Incomplete | None = None) -> Generator[Incomplete]: ...
def path_getrootdir(path): ...

class ModelRunner:
    config: Incomplete
    features: Incomplete
    hooks: Incomplete
    formatters: Incomplete
    undefined_steps: Incomplete
    step_registry: Incomplete
    capture_controller: Incomplete
    context: Incomplete
    feature: Incomplete
    hook_failures: int
    def __init__(self, config, features: Incomplete | None = None, step_registry: Incomplete | None = None) -> None: ...
    aborted: Incomplete
    def run_hook(self, name, context, *args) -> None: ...
    def setup_capture(self) -> None: ...
    def start_capture(self) -> None: ...
    def stop_capture(self) -> None: ...
    def teardown_capture(self) -> None: ...
    def run_model(self, features: Incomplete | None = None): ...
    def run(self): ...

class Runner(ModelRunner):
    path_manager: Incomplete
    base_dir: Incomplete
    def __init__(self, config) -> None: ...
    def setup_paths(self) -> None: ...
    def before_all_default_hook(self, context) -> None: ...
    def load_hooks(self, filename: Incomplete | None = None) -> None: ...
    def load_step_definitions(self, extra_step_paths: Incomplete | None = None) -> None: ...
    def feature_locations(self): ...
    def run(self): ...
    context: Incomplete
    formatters: Incomplete
    def run_with_paths(self): ...
