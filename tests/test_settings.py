from config.settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH

def test_settings_values():
    assert FPS == 60

    assert isinstance(SCREEN_WIDTH, int)

    assert SCREEN_HEIGHT > 0

   