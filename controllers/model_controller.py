class ModelController:

    @staticmethod
    def get_model_columns(model):
        columns = model.__table__.columns
        result_columns = []
        for column in columns:
            if column.primary_key or column.foreign_keys:
                continue
            result_columns.append(column)

        return result_columns
