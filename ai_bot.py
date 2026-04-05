import random

print("AI Market Analyzer")
print("------------------")

trend = random.choice(["UPTREND","DOWNTREND"])

rsi = random.randint(20,80)

if rsi > 70:
    condition = "OVERBOUGHT"
elif rsi < 30:
    condition = "OVERSOLD"
else:
    condition = "NEUTRAL"

print("Trend:",trend)
print("RSI:",rsi)
print("Market condition:",condition)
