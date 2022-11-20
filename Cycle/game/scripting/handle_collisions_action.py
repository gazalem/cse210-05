import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.gameover import handleGameOver


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the player_one collides
    with the player_two, or the player_one collides with its segments, or the game is over.

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
            self._handle_player_two_collision(cast)
            self._handle_segment_collision(cast)

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

        player_two = cast.get_first_actor("player_two")
        second_head = player_two.get_segments()[0]
        second_segments = player_two.get_segments()[1:]

        for segment in segments:
            if second_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for second_segment in second_segments:
            if head.get_position().equals(second_segment.get_position()):
                self._is_game_over = True

    