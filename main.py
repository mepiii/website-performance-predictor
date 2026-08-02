import os, pandas as pd, joblib
from sklearn.ensemble import RandomForestRegressor
from predictor.predict import PerformancePredictor
def train_model(d, m):
    df = pd.read_csv(d)
    reg = RandomForestRegressor(n_estimators=100, random_state=42)
    reg.fit(df[['html_kb', 'css_kb', 'js_kb', 'image_count', 'font_count', 'http_requests']], df['load_time_sec'])
    os.makedirs(os.path.dirname(m), exist_ok=True)
    joblib.dump(reg, m)

def main():
    b = os.path.dirname(os.path.abspath(__file__))
    d, m = os.path.join(b, 'dataset', 'website_performance.csv'), os.path.join(b, 'models', 'perf_regressor.joblib')
    if not os.path.exists(m): train_model(d, m)
    p = PerformancePredictor(m)
    print('Website Performance Predictor Demo:')
    res = p.predict_load_time({'html_kb': 120, 'css_kb': 250, 'js_kb': 850, 'image_count': 28, 'font_count': 5, 'http_requests': 45})
    print('  Estimated Load Time:', res['estimated_load_time_sec'], 'sec')

if __name__ == '__main__': main()
