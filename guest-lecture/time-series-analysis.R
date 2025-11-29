data(AirPassengers)
plot(AirPassengers)

# Creating a time series object
# myseries <- ts(data, start=, end=, frequency = )
# ts_data <- ts(AirPassengers, frequency = 12, start = c(1949, 1))

profit <- ts(c(45, 78, 90, 110, 120, 135), start = 2018)
profit
plot(profit)

# create sales monthly time series data from jan 2003 with frequency 12
sales <-c(250, 270, 300, 280, 320, 330, 350, 370, 390, 400, 420, 450,
          260, 280, 310, 290, 330, 340, 360, 380, 400, 410, 430, 460)
tsales <- ts(sales, start = c(2003, 1), frequency = 12)

print(sales)
print(tsales)
plot(tsales)

start(tsales)
end(tsales)
frequency(tsales)
cycle(tsales)

# subset time series from may 2003 to june 2004
tsales.subset<-window(tsales, start=c(2003,5), end=c(2004,6))
tsales.subset

plot(tsales.subset)
frequency(tsales.subset)
cycle(tsales.subset)


# Frequency of time series data
# annual data = 1
# quarterly data = 4
# monthly data = 12
# weekly data = 52

# Decomposing time series data
decomposed.ts <- decompose(tsales)
plot(decomposed.ts)
seasonal.ts <- decomposed.ts$seasonal
trend.ts <- decomposed.ts$trend
random.ts <- decomposed.ts$random
seasonal.ts
trend.ts

# Random walk time series
set.seed(123)
n <- 100
random_walk <- cumsum(rnorm(n))
plot(random_walk, type = "l", main = "Random Walk Time Series", ylab = "Value", xlab = "Time")

# Lag function
# lag(ts, k)
# where k = number of lags
# lag 1 = 1 years(period) previous value

# usmacro.dta data

# Seasonality
# install.packages("forecast")
library(forecast)

# Seasonal decomposition
data("AirPassengers")
plot(AirPassengers)
LAirPassengers <- log(AirPassengers)
plot(LAirPassengers, ylab="log(AirPassengers)")
# Decompose the time series with stl function
fit<-stl(LAirPassengers, s.window="period")
plot(fit)
fit$time.series


# ARIMA
data("JohnsonJohnson")
fit<- ets(JohnsonJohnson)
fit
plot(
  forecast(fit), 
  main="Forecast for Johnson & Johnson Quarterly Earnings",
  ylab="Earnings per Share",
  xlab="Year",
  flty=2
)

# Moving Average
# Plotting using nile dataset
data("Nile")
# see data structure
str(Nile)
ylim <- c(min(Nile), max(Nile))
plot(Nile, ylim=ylim, main="Nile River Flow", ylab="Flow", xlab="Year")
plot(ma(Nile, 3), main="Simple moving average (k=3)", ylim=ylim)
plot(ma(Nile, 7), main="Simple moving average (k=7)", ylim=ylim)
plot(ma(Nile, 15), main="Simple moving average (k=15)", ylim=ylim)

# ARIMA - Checking for statinarity
library(tseries)
plot(Nile)
ndiffs(Nile)
dNile<-diff(Nile)
plot(dNile)
adf.test(Nile)
adf.test(dNile)
Acf(dNile)
Pacf(dNile)

# For adf test:
# Null hypothesis (H0): The time series has a unit root (is non-stationary).
# Alternative hypothesis (H1): The time series does not have a unit root (is stationary).
# If the p-value is less than a chosen significance level (e.g., 0.05), we reject the null hypothesis and conclude that the time series is stationary.
# If the p-value is greater than the significance level, we fail to reject the null hypothesis, indicating that the time series is non-stationary.s

# Auto ARIMA
fit<-auto.arima(Nile)
fit
qqnorm(fit$residuals)
qqline(fit$residuals)
Box.test(fit$residuals, type="Ljung-Box")
forecast(fit, 3)
plot(
  forecast(fit, 3),
  xlab="Year",
  ylab="Nile River Flow",
)

# install.packages("wooldridge")
library(wooldridge)
