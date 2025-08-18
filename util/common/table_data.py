from dataclasses import dataclass

@dataclass
class TableData:
    columns: list[str]
    data_list: list[tuple]

    def get_data(self) -> list[list]:
        table_instances = []

        for instance in self.data_list:
            data = [*instance]
            table_instances.append(data)

        return table_instances
    
    def sort_by_column(self, column_name: str):
        field_index = self.columns.index(column_name)
        sorted_data = sorted(self.get_data(), key=lambda row: row[field_index])
        return sorted_data