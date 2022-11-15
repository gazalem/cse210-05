import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Snake(Actor):
    """
    A long limbless reptile.
<<<<<<< HEAD

    The responsibility of Snake is to move itself.
=======
    
    The responsibility of Cycle is to move itself.
>>>>>>> PlayerTwo

    Attributes:
        _points (int): The number of points the food is worth.
    """
<<<<<<< HEAD

    def __init__(self, a, b, color):
        super().__init__()
        self._segments = []
        self._prepare_body(a, b, color)
=======
    def __init__(self, start_position):
        super().__init__()
        self._segments = []
        self._color = Color(255, 255, 255)
        self._prepare_body(start_position)
>>>>>>> PlayerTwo

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments, color):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

        return self

    def turn_head(self, velocity):
<<<<<<< HEAD
        self._segments[1].set_velocity(velocity)

        return self

    def _prepare_body(self, a, b, bcolor):

        for i in range(constants.SNAKE_LENGTH):
            position = Point(a, b - i * constants.CELL_SIZE)
            velocity = Point(0, 1 * constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else color

=======
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, position):
        x = position.get_x()
        y = position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, 1 * -constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            self._color = constants.YELLOW if i == 0 else constants.GREEN
            
>>>>>>> PlayerTwo
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
<<<<<<< HEAD
            segment.set_color(color)
            self._segments.append(segment)
=======
            segment.set_color(self._color)
            self._segments.append(segment)


    def set_cycle_color(self, color):
        """Set the Color of the Cycle
        Arguments:
            color(Color): Color of the Cycle RGB
        """
        self._color = color

        for segment in self._segments:
            segment.set_color(self._color)
>>>>>>> PlayerTwo
