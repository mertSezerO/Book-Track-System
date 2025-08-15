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