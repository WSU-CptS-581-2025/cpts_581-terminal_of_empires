import os
import sys
from collections import defaultdict
import click
from GameLogic.game_manager import ToE
import src
BANNED_BOTS = {"orden66"}

def parse_player_info(player_info):
    try:
        parts = player_info.split(":")
        if len(parts) == 2:
            name, bot_type = parts
            castle_position = None
        elif len(parts) == 3:
            name, bot_type, position = parts
            x, y = position.split(".")
            castle_position = (int(x), int(y))
        else:
            raise ValueError()
        return name, bot_type.lower(), castle_position
    except ValueError:
        print(f"Invalid player info: {player_info}. Should be name:bot_type or name:bot_type:x.y")
        sys.exit(1)

def game_setup(toe, players, ignore_bans):
    for player_info in players.split(","):
        name, bot_type, castle_position = parse_player_info(player_info)
        if bot_type in BANNED_BOTS and not ignore_bans:
            print(f"Bot {bot_type} is banned for being dangerous. Use --ignore-bans to override.")
            sys.exit(1)
        toe.add_player(name, bot_type, castle_position=castle_position)


@click.command()
@click.option("--width", type=int, default=40, help="The width of the map.")
@click.option("--height", type=int, default=20, help="The height of the map.")
@click.option(
    "--players",
    type=str,
    help="Players, specified as a comma separated list of player_name:bot_type (or optionally with the initial position as player_name:bot_type:x.y).",
)
@click.option(
    "--no-ui",
    is_flag=True,
    help="Don't show the UI, just run the game until the end and inform the winner.",
)
@click.option(
    "--ui-turn-delay",
    type=float,
    default=0.2,
    help="Seconds to wait between turns when showing the UI.",
)
@click.option(
    "--turn-timeout",
    type=float,
    default=0.5,
    help="Maximum seconds a player can take to think its turn.",
)
@click.option(
    "--log-path",
    type=click.Path(),
    default="./toe.log",
    help="Path for the log file of the game.",
)
@click.option(
    "--max-turns",
    type=int,
    default=None,
    help="Maximum number of turns to play (no limit if not specified).",
)
@click.option(
    "--debug",
    is_flag=True,
    help="In debug mode, any errors in the bot will stop the game and the traceback will be shown.",
)
@click.option(
    "--repeat",
    type=int,
    default=1,
    help="Repeat the game N times and return stats about winners of the games.",
)
@click.option(
    "--ignore-bans",
    is_flag=True,
    help="Ignore bots banned for being dangerous code.",
)
def main(width, height, players, no_ui, ui_turn_delay, log_path, turn_timeout, max_turns, debug, repeat, ignore_bans):
    """
    Run a game of Terminal of Empires.
    Optionally, repeat the game N times and return stats about winners.
    """
    scoreboard = defaultdict(int)

    for game_number in range(repeat):
        if no_ui:
            print(f"Playing game {game_number + 1} of {repeat}...")
            ui = None
        else:
            from src.Renderer.ui import ToEUI 
            ui = ToEUI(ui_turn_delay)

        toe = ToE(
            width,
            height,
            ui=ui,
            log_path=log_path,
            turn_timeout=turn_timeout,
            debug=debug,
        )

        for game_number in range(repeat):
            if no_ui:
                print(f"Playing game {game_number + 1} of {repeat}...")
                ui = None
            else:
                from src.Renderer.ui import ToEUI  
                ui = ToEUI(ui_turn_delay)

        toe = ToE(
            width=width,
            height=height,
            ui=ui,
            log_path=log_path,
            turn_timeout=turn_timeout,
            debug=debug,
        )

        try:
            game_setup(toe, players, ignore_bans)
        except click.UsageError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

        if ui:
            with ui.show():
                result = toe.play(max_turns=max_turns)
        else:
            result = toe.play(max_turns=max_turns)

        if result:
            winners, turns_played = result
            print(f"Game {game_number + 1} ended in {turns_played} turns!")
            print("Winners:", ",".join(player.name for player in winners))
            score = 1 / len(winners)
            for winner in winners:
                scoreboard[winner.name] += score

    if repeat > 1:
        print("\n📊 Final Scoreboard:")
        for player, score in sorted(scoreboard.items(), key=lambda x: x[1], reverse=True):
            print(f"{player}: {score}")

if __name__ == '__main__':
    main()
