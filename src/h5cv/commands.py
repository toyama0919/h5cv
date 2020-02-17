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
        hdf5=hdf5,
        store=store,
        config=config,
        profile=profile,
        debug=debug
    )

    if version:
        print(h5cv.VERSION)
        sys.exit()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@cli.command(help="list hdf5 keys")
@click.argument("key")
@click.pass_context
def ls(ctx, key):
    ctx.obj.core.list(key)


@cli.command(help="append")
@click.option(
    "--globs", "-g", type=str, multiple=True, help="files.",
)
@click.option(
    "--compression", type=str, help="compression",
)
@click.pass_context
def append(ctx, globs, compression, store):
    ctx.obj.core.add_files(globs, compression)


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
