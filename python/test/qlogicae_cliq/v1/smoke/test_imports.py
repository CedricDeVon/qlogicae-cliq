
from qlogicae_cliq.v1.library.cli_app_manager import CliAppManager
from qlogicae_cliq.v1.library.cli_command_manager import CliCommandManager
from qlogicae_cliq.v1.library.cli_database_manager import CliDatabaseManager
from qlogicae_cliq.v1.library.cli_log_manager import CliLogManager
from qlogicae_cliq.v1.library.cli_plugin_manager import CliPluginManager


def test_should_import_and_initialize_all_public_components():
    CliAppManager().get_singleton()
    CliCommandManager().get_singleton()
    CliDatabaseManager().get_singleton()
    CliLogManager().get_singleton()
    CliPluginManager().get_singleton()
