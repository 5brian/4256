def midpoint(self, point):
    mid_x = (self.x + point.x) / 2
    mid_y = (self.y + point.y) / 2

    return Point(mid_x, mid_y)
