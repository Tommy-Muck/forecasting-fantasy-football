from app.app import get_points_data, get_playing_data, get_forecast_data


class TestApp:
    def test_get_points_data(self):
        df = get_points_data()
        assert not df.empty

    def test_get_playing_data(self):
        df = get_playing_data()
        assert not df.empty

    def test_get_forecast_data(self):
        df = get_forecast_data()
        assert not df.empty
