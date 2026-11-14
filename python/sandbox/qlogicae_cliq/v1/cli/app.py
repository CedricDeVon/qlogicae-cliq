
from qlogicae_cor.v3.library.external_dependency_manager import (
    ExternalDependencyManager
)
from qlogicae_cliq.v1.library.cli_app_manager import (
    CliAppManager    
)
from qlogicae_cliq.v1.library.cli_command_manager import (
    CliCommandManager    
)

CliAppManager().get_singleton().run(
    external_dependency={
        "is_pre_allocated": False,
    },
    plugin={
        "target_filesystem_paths": (
            "./sandbox/qlogicae_cliq/v1/cli/plugin",
        ),
        "is_recursive": True,
        "imported_modules": (),
        "raw_export_data": (),
        # "initial_export_data": {},
    },
)

CliCommandManager().get_singleton().command_collection["print-any-message"](
    {
        "target": ["Hello"]
    }
)

