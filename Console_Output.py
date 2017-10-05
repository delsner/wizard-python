import click


def print_separating_line():
    click.echo(click.style('--------------------------------', fg='black', bold='black'))


def print_new_round_info(nr_hand_cards, trump_color):
    click.echo(click.style(
        'Cards have been shuffled. New round with %d cards. Trump is: %s' % (
            nr_hand_cards, trump_color),
        fg='black', bold='black'))


def choose_card_dialog(player_name):
    return click.prompt("%s, choose card index" % player_name, type=int)


def guess_tricks_dialog(player_name):
    return click.prompt('%s, how many tricks will you make?' % player_name, type=int)


def print_winner(player_name):
    click.echo(click.style("%s you're the fucking man!" % player_name, fg='black', bold='black'))


def print_trick_winner(player_name):
    print_separating_line()
    click.echo(click.style('%s won the trick.' % player_name, fg='black', bold='black'))


def print_hand_card_information(player_name, hand_cards):
    print_separating_line()
    click.echo('%s, these are your current cards:' % player_name)
    click.echo(hand_cards.print_cards_with_index())


def print_current_scores(players):
    click.echo(click.style('------------CURRENT SCORE-----------------', fg='black', bold='black'))
    for p in players:
        click.echo(click.style('%s: %d points.' % (p.name, p.score), fg='black', bold='black'))
