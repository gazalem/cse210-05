import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class handleGameOver(Action):

    def _handle_game_over(self, cast):
            """Shows the 'game over' message and turns the player_one and player_two white if the game is over.

            Args:
                cast (Cast): The cast of Actors in the game.
            """
            if self._is_game_over:
                player_one = cast.get_first_actor("player_one")
                player_one.set_cycle_color(constants.WHITE)
                player_one_segments = player_one.get_segments()
                player_two = cast.get_first_actor("player_two")
                player_two.set_cycle_color(constants.WHITE)
                player_two_segments = player_two.get_segments()

                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)

                message = Actor()
                message.set_text("Game Over!")
                message.set_position(position)
                cast.add_actor("messages", message)

                for segment in player_one_segments:
                    segment.set_color(constants.WHITE)

                for segment in player_two_segments:
                    segment.set_color(constants.WHITE)
