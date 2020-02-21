import click
import sys
import h5cv
from .core import Core


class Mash(object):
    pass


@click.group(invoke_without_command=True)
@click.option("--config", "-c", type=str, help="config file.")
@click.option("--profile", "-p", type=str, help="aws profile name.")
@click.option(
    "--hdf5", "-H", type=str, help="hdf5 file path.",
)
@click.option(
    "--store", type=str, help="store option",
)
@click.option("--debug/--no-debug", default=False, help="enable debug logging")
@click.option(
    "--version/--no-version", "-v", default=False, help="show version. (default: False)"
)
@click.pass_context
def cli(ctx, config, profile, hdf5, store, debug, version):
    ctx.obj = Mash()
    ctx.obj.core = Core(
        hdf5=hdf5, store=store, config=config, profile=profile, debug=debug
    )

    if version:
        print(h5cv.VERSION)
        sys.exit()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@cli.command(help="list hdf5 keys")
@click.option(
    "--recursive/--no-recursive", "-r", default=False, help="recursive files. (default: False)"
)
@click.argument("key", required=False)
@click.pass_context
def ls(ctx, recursive, key):
    ctx.obj.core.list(key, recursive)


@cli.command(help="write")
@click.option(
    "--glob", "-g", type=str, help="files.",
)
@click.option(
    "--compression", type=str, help="compression",
)
@click.option(
    "--append/--no-append", "-a", default=False, help="append mode. (default: False)"
)
@click.pass_context
def write(ctx, glob, compression, append):
    ctx.obj.core.write(glob, append, compression=compression)


@cli.command(help="imgcat in hdf5 dataset.")
@click.argument("key")
@click.pass_context
def imgcat(ctx, key):
    ctx.obj.core.imgcat(key)


@cli.command(help="show in hdf5 dataset")
@click.argument("key")
@click.pass_context
def show(ctx, key):
    ctx.obj.core.show(key)


def main():
    cli(obj={})
