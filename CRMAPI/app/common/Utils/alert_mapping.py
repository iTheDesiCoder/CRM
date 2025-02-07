import pandas as pd


class AlertMapping:
    _message_mapping = {}

    @classmethod
    def load_message_mappings(cls, file_path: str):
        """Load MessageCode to MessageDescription mapping from Excel."""
        df = pd.read_excel(file_path, sheet_name='Advisor Alerts')
        cls._message_mapping = dict(zip(df['MessageCode'], df['MessageDescription']))

    @classmethod
    def get_message_description(cls, message_code: int) -> str:
        """Return the MessageDescription for a given MessageCode."""
        return cls._message_mapping.get(message_code, "Unknown Message Code")
