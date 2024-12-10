class Vector2:
    def __init__(this, x, y):
        this.x = x
        this.y = y
    
    def __repr__(this):
        return f"({this.x},{this.y})"
    
    def __eq__(this, other):
        return (this.x == other.x) and (this.y == other.y)
    
    def __ne__(this,other):
        return not (this == other)
    
    def __add__(this, other):
        return Vector2(this.x + other.x, this.y + other.y)

    def __sub__(this, other):
        return Vector2(this.x - other.x, this.y - other.y)
    
    def __mul__(this, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector2(this.x * other, this.y * other)
    def __rmul__(this, other):
        return this.__mul__(other)