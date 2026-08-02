import joblib, pandas as pd
class PerformancePredictor:
    def __init__(self, m): self.model = joblib.load(m)
    def predict_load_time(self, metrics):
        cols = ['html_kb', 'css_kb', 'js_kb', 'image_count', 'font_count', 'http_requests']
        t = float(self.model.predict(pd.DataFrame([metrics])[cols])[0])
        return {'estimated_load_time_sec': round(t, 2)}
