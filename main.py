import plotly
import pandas as pd
import openpyxl


import plotly.express as px



data = pd.read_excel('Ergebnis.xlsx',sheet_name='Sheet3')

fig = px.line(data,
              x="Date",
              y="Duration",
              title='Durschnitt von Duration nach Date und Timer Name',
              color='Timer Name',
              labels={"Duration":"Duration(second)"})


fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.show()
plotly.offline.plot(fig, filename="test.html")



