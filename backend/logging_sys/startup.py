def enable_ansi():
    import os
    import platform
    from global_varibles import Globals as G

    print("Enabling ANSI colors...")

    if os.name == "nt":
        import ctypes

        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        STD_OUTPUT_HANDLE = -11

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

        mode = ctypes.c_ulong()
        success = kernel32.GetConsoleMode(handle, ctypes.byref(mode))

        if success:
            new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
            if kernel32.SetConsoleMode(handle, new_mode):
                G.ansi_text = True
                print("ANSI enabled")
            else:
                G.ansi_text = False
                print("Failed to enable ANSI")
        else:
            G.ansi_text = False
            print("Failed to get console mode")
    else:
        # systems that have ANSI support by default
        good_systems = ["linux", "darwin", "freebsd", "postix"
                        "openbsd", "netbsd", "aix", "solaris"]
        if platform.system().lower() in good_systems:
            G.ansi_text = True
            print("ANSI enabled")
        else:
            G.ansi_text = False
            print("Failed to enable ANSI colors. "
                  "This system is not supported.")
