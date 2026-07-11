import argparse

class Application:
    def __init__(self, description):
        super().__init__()  # Continue MRO chain first
        from .glogger import GLogger
        self._arg_parser = argparse.ArgumentParser(description=description)
        self._arg_parse(self._arg_parser)
        self.args = self._arg_parser.parse_args()
        self.logger = GLogger(self.__class__.__name__)
        self.config = self._config_load()

    def _arg_parse(self, parser):
        parser.add_argument("--config_json", action="append", default=[], help="Path to the configuration JSON file")
        parser.add_argument("--config", action="append", help="config parameters in the form of key=value that will override the config JSON file")
        parser.add_argument("--debug", action="store_true", help="Enable debug mode")
        return parser

    def _config_load(self):
        from .gjson import GJSON
        """
        Load configuration from JSON files. If multiple files are provided, they will be merged with later files overriding earlier ones.
        """
        config = {}
        if not (hasattr(self.args, 'config_json') and self.args.config_json):
            return config
        for path in self.args.config_json:
            config.update(GJSON.load(path))
        if self.args.config:
            for config_item in self.args.config:
                key, value = config_item.split("=")
                config[key] = value
        return config

    def app_run(self):
        print("Running the application...")