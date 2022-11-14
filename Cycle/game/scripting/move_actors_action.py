import constants
from game.scripting.action import Action


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

    def execute(self, cast, script):

        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()

        snake1 = cast.get_first_actor("player_one")
        snake2 = cast.get_first_actor("player_two")

        if script.get_actions("update")[1]._is_game_over:
            snake1.grow_tail(1, constants.WHITE)
            snake2.grow_tail(1, constants.WHITE)

        else:

            snake1 = cast.get_first_actor("player_one")
            snake2 = cast.get_first_actor("player_two")

            snake1.grow_tail(1, constants.RED)
            snake2.grow_tail(1, constants.GREEN)
