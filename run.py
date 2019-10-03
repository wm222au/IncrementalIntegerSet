import cli.log
from increment.increment import simulate
from xlsx.xlsx_wrapper import generate_output


@cli.log.LoggingApp
def incremental_integer_set(app):
    start = app.params.start
    end = app.params.end
    increments = app.params.increments
    starting_point = app.params.startpoint
    output = app.params.output
    name = app.params.name
    flex = True if app.params.fluctuate == 'flex' else None
    append = app.params.append
    static_columns = list(map(str, app.params.static_columns.split()))

    numbers = simulate(start, end, increments, starting_point, flex)
    for number in numbers:
        for column in static_columns:
            number.append(column)

    generate_output(output, name, numbers, append)


incremental_integer_set.add_param("start", help="", default=1, type=int)
incremental_integer_set.add_param("end", help="", default=1, type=int)
incremental_integer_set.add_param("increments", help="", default=1, type=int)
incremental_integer_set.add_param("-sp", "--startpoint", help="", default=1, type=int)
incremental_integer_set.add_param("-o", "--output", help="", default="cli", type=str)
incremental_integer_set.add_param("-n", "--name", help="", default="integer_set", type=str)
incremental_integer_set.add_param("-f", "--fluctuate", help="strict (moves strictly from startnumber to endnumber) / flex (can go over and under the startnumber / endnumber)", default="strict", type=str)
incremental_integer_set.add_param("-a", "--append", help="set if should append result to existing file", default=None, const=True, nargs="?")
incremental_integer_set.add_param("-sc", "--static_columns", help="static (i.e. not iterational) columns to be added to output", default='', const='', nargs="?")

if __name__ == "__main__":
    incremental_integer_set.run()
