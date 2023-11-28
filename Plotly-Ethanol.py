from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

while True:
    data = pd.read_csv("All Data.csv", usecols=['No.','WL(nm)','Abs','Batch'])

    data = data[data['Batch'] != 'Batch 8 (Part 2)']

    data = data.replace({'Batch': {'Batch 8 (Part 1)': 'Batch 8'}})

    batch_id = data['Batch'].unique()



    app = Dash()

    batch = dcc.Dropdown(
        options = [batch_id],
        #value = 'PM2.5'
    )


    measure_x = dcc.Dropdown(
        options = ['WL(nm)','Abs'],
        value = 'WL(nm)'
    )

    measure_y = dcc.Dropdown(
        options = ['WL(nm)','Abs'],
        value = 'Abs'    
    )

  
    app.layout = html.Div(children=[
        html.H1(children='Ethanol Stuff'),
        measure_x,
        measure_y,
        dcc.Slider(min=0, max=800, step=5, value=280, marks=None, id='my-slider'),
        dcc.Graph(id='ethanol-graph'),
    ])


    @app.callback(
        Output(component_id='ethanol-graph', component_property='figure'),
        #Input(component_id=towers, component_property='value'),
        Input(component_id=measure_x, component_property='value'),
        Input(component_id=measure_y, component_property='value'),
        Input('my-slider', 'value'),
        
    )
    def update_graph(measure_x, measure_y, value):
        
        #user = 'ramoncarlos1114'
        #api = 'Gl8JjwU6YCm3k4vm8Na8'
        #chart_studio.tools.set_credentials_file(username=user, api_key=api)
        filter = data[data['WL(nm)'] <= value]
        #tfh = data[(data['Date/Time'] >= start) & (data['Date/Time'] <= dayz)]
        line_fig = px.scatter(filter,
                            x=measure_x, y= measure_y,
                            color='Batch',
                            title=f'Analysis of Ethanol Batches')
        
        #fig = py.plot(line_fig, filename = 'test graph', auto_open=False)
        #return fig
        return line_fig

    if __name__ == '__main__':
            app.run(debug=True)
