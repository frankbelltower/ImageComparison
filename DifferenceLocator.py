class DifferenceLocator:
    row: int
    pixel: int

    def set_row(self, row: int) -> None:
        self.row = row

    def set_pixel(self, pixel: int) -> None:
        self.pixel = pixel

    def get_row(self) -> int:
        return self.row

    def get_pixel(self) -> int:
        return self.pixel
