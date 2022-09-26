class TableMatrix:

    def set(self, row, col, value):
        i = self.__get_data_index(row, col)
        self.data[i] = value

    def get(self, row, col):
        i = self.__get_data_index(row, col)
        return self.data[i]


    def __get_data_index(self, row, col):
        if isinstance(col, str):
            col = self.cols.index(col)

        if isinstance(row, str):
            row = self.rows.index(row)

        assert row < self.height
        assert col < self.width

        return col + row*self.width

    def __init__(self, rows: list[str], cols: list[str]):
        self.rows = list(rows)
        self.cols = list(cols)
        self.width = len(self.cols)
        self.height = len(self.rows)

        data = list()

        for idc, c in enumerate(self.cols):
            for idr, r in enumerate(self.rows):
                data.append(None)

        self.data = data


    def markdown(self):
        s = "|  |"
        for c in self.cols:
            s += str(c) + " |"

        s += "\n|---|"
        for c in self.cols:
            s += "---|"

        for row in self.rows:
            s += "\n" +  str(row) + "|"

            for col in self.cols:
                value = self.get(row, col)
                if value is None:
                    s += "  |"
                else:
                    s += str(value) + " |"

        return s

