from game.scripting.action import Action
import constants


# TODO: Implement MoveActorsAction class here!

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):
    """This Class will move the body of the Snake
    also will override the method execute from Action
    Class.
    """

    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast, script):

        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()

        player1 = cast.get_first_actor("snake")
        player2 = cast.get_second_actor("snake2")

        if script.get_actions("update")[1]._is_game_over:
            player1.grow_tail(1, constants.WHITE)
            player2.grow_tail(1, constants.WHITE)

        else:

            player1 = cast.get_first_actor("snake")
            player2 = cast.get_second_actor("snake2")

            player1.grow_tail(1, constants.RED)
            player2.grow_tail(1, constants.GREEN)
