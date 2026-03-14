# 라이브러리 설치가 필요해요: pip install yfinance prophet
import yfinance as yf
from prophet import Prophet

# 1. 데이터 가져오기 (예: 메타 플랫폼)
df = yf.download("META", start="2020-01-01", end="2026-03-14")
df.reset_index(inplace=True)
df = df.rename(columns={"Date": "ds", "Close": "y"})

# 2. 모델 학습
model = Prophet()
model.fit(df[['ds', 'y']])

# 3. 예측 (향후 365일)
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

# 4. 시각화
model.plot(forecast)
