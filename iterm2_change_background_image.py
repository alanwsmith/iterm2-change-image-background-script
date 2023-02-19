#!/usr/bin/env python3

import iterm2
import os.path

from pathlib import Path


image_path = os.path.join(
    Path.home(), 
    "Desktop", 
    "iterm2-background.jpg"
)

async def main(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    profile = await session.async_get_profile()
    await profile.async_set_background_image_location(
        image_path
    )

iterm2.run_until_complete(main, True)
