import unittest.mock as mock

import click


def test_module_init():
    import trade_republic_api.__main__

    with mock.patch.object(trade_republic_api.__main__, "__name__", "__main__"):
        with mock.patch.object(click.core.sys, "exit") as mock_exit:
            trade_republic_api.__main__.init()

            assert mock_exit.call_args[0][0] == 0
