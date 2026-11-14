__all__ = (
    "export"
)

def print_message(arguments):
    targets = (
        arguments.get("target")
        if isinstance(arguments, dict)
        else getattr(arguments, "target", None)
    )

    for target in targets:
        print(target)



def on_pre_setup():
    print("exports - on_pre_setup")


def on_post_setup():
    print("exports - on_post_setup")


def on_pre_run():
    print("exports - on_pre_run")


def on_post_run():
    print("exports - on_post_run")


def export():
    data = {
        "object_merge": {
            "level": -1
        },
        "command": {
            "options": {
                "commands": [
                    {
                        "name": "print",
                        "args": (),
                        "kwargs": {
                            "help": "print commands",
                        },
                        "subcommands": [
                            {
                                "name": "any",
                                "args": (),
                                "kwargs": {
                                    "help": "print any",                                    
                                },
                                "subcommands": [
                                    {
                                        "name": "message",
                                        "kwargs": {
                                            "help": "print message",
                                        },
                                        "command_handler": print_message,
                                        "arguments": [
                                            {
                                                "args": (
                                                    "-t",
                                                    "--target",
                                                ),
                                                "kwargs": {
                                                    "help": "message to print",
                                                    "dest": "target",
                                                    "action": "append",
                                                    "type": str,
                                                    "required": True,
                                                    "nargs": "+",
                                                    "metavar": "TARGET",
                                                },
                                            },
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
            "callbacks": {
                "on_pre_setup": on_pre_setup,
                "on_post_setup": on_post_setup,
                "on_pre_run": on_pre_run,
                "on_post_run": on_post_run,
            },
        },
    }

    return data
