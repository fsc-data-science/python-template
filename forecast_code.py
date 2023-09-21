# import pmdarima as pm 

arima_model=pm.auto_arima(eth_vwap_close,seasonal=False,stepwise=True,supress_warnings=True)


#Forecast the next 5 periods
n_periods=5
forecast,conf_int = arima_model.predict(n_periods=n_periods,return_conf_int=True)


trace1 = go.Scatter(x=list(range(1, len(eth_vwap_close)+1)), y=eth_vwap_close, mode='lines+markers', name='close')

# create a trace for the 'forecast' data with NaN for missing values

trace2=go.Scatter(x=list(range(len(eth_vwap_close)+1, len(eth_vwap_close)+len(forecast)+1)),y=forecast, mode='lines+markers',name='forecast')

fig2=go.Figure(data=[trace1,trace2])

#create the plotly figure
# show the plot
fig2.write_html('forecast_chart.html')
