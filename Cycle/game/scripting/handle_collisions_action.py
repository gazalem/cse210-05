import constants
import itertools
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
<<<<<<< HEAD

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.
=======
    
    The responsibility of HandleCollisionsAction is to handle the situation when the player_one collides
    with the player_two, or the player_one collides with its segments, or the game is over.
>>>>>>> PlayerTwo

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
<<<<<<< HEAD
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake1 = cast.get_first_actor("player_one")
        head1 = snake1.get_segments()[0]
        segments1 = snake1.get_segments()[1:]

        snake2 = cast.get_first_actor("player_two")
        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]

        for seg1, seg2 in itertools.zip_longest(segments1, segments2):
            print("test text")
            print(
                f'h1x:{head1.get_position().get_x()},h1y:{head1.get_position().get_y()}')
            print(
                f'h2x:{head2.get_position().get_x()},h2y:{head2.get_position().get_y()}')
            print(
                f's1x:{seg1.get_position().get_x()},s1y:{seg1.get_position().get_y()}')
            print(
                f's2x:{seg2.get_position().get_x()},s2y:{seg2.get_position().get_y()}')

        # tolerance for the pixel
        a = 6

        head1Seg2X = (abs(head1.get_position().get_x() -
                      seg2.get_position().get_x()) < a)
        head1Seg2Y = (abs(head1.get_position().get_y() -
                      seg2.get_position().get_y()) < a)

        print(head1Seg2X, head1Seg2Y)

        head2Seg1X = (abs(head2.get_position().get_x() -
                      seg1.get_position().get_x()) < a)
        head2Seg1Y = (abs(head2.get_position().get_y() -
                          seg1.get_position().get_y()) < a)

        print(head2Seg1X, head2Seg1Y)

        if (head1Seg2X and head1Seg2Y
                or head2Seg1X and head2Seg1Y):

            print('GAME OVER')
            self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

=======
            self._handle_player_two_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_player_two_collision(self, cast):
        """Updates the score nd moves the player_two if the player_one collides with the player_two.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        player_two = cast.get_first_actor("player_two")
        player_one = cast.get_first_actor("player_one")
        head = player_one.get_head()

        if head.get_position().equals(player_two.get_position()):
            points = player_two.get_points()
            player_one.grow_tail(points)
            score.add_points(points)
            player_two.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the player_one collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player_one = cast.get_first_actor("player_one")
        head = player_one.get_segments()[0]
        segments = player_one.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the player_one and player_two white if the game is over.
        
>>>>>>> PlayerTwo
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
<<<<<<< HEAD
            snake1 = cast.get_first_actor("player_one")
            segments1 = snake1.get_segments()

            snake2 = cast.get_first_actor("player_two")
            segments2 = snake2.get_segments()
=======
            player_one = cast.get_first_actor("player_one")
            segments = player_one.get_segments()
            player_two = cast.get_first_actor("player_two")
>>>>>>> PlayerTwo

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)

            for segment in segments2:
                segment.set_color(constants.WHITE)
<<<<<<< HEAD
=======
            player_two.set_color(constants.WHITE)
>>>>>>> PlayerTwo
