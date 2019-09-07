from pathlib import Path
from textwrap import dedent

import toml

import blackini


def test_version():
    assert (
        blackini.__version__
        == toml.load(Path(__file__).parent.parent.joinpath("pyproject.toml"))[
            "tool"
        ]["poetry"]["version"]
    )


def test_black(tmpdir):
    root = tmpdir.mkdir("project_root")

    pyproject_file = root.join("tox.ini")
    pyproject_file.write(
        dedent(
            """
            """
        )
    )

    script_file_ = root.join("test_script.py")
    script_file_.write(
        dedent(
            """
            """
        )
    )
