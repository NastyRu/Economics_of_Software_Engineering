import matplotlib.pyplot as plot
from plotly.tools import mpl_to_plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    dbc.Row(
        [
            dbc.Col(children=html.H4("RELY:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 0.75},
                    {'label': 'Низкий', 'value': 0.86},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 1.15},
                    {'label': 'Очень высокий', 'value': 1.4}],
                value=1,
                clearable=False,
                id='rely_mode'
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1.0}],
                id='rely_change'
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("DATA:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Низкий', 'value': 0.94},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 1.08},
                    {'label': 'Очень высокий', 'value': 1.16}],
                value=1,
                clearable=False,
                id='data_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='data_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("CPLX:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 0.7},
                    {'label': 'Низкий', 'value': 0.85},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 1.15},
                    {'label': 'Очень высокий', 'value': 1.3}],
                value=1,
                clearable=False,
                id='cplx_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='cplx_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("TIME:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 1.11},
                    {'label': 'Очень высокий', 'value': 1.5}],
                value=1,
                clearable=False,
                id='time_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='time_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("STOR:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 1.06},
                    {'label': 'Очень высокий', 'value': 1.21}],
                value=1,
                clearable=False,
                id='stor_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='stor_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("VIRT:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Низкий', 'value': 0.87},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 1.15},
                    {'label': 'Очень высокий', 'value': 1.3}],
                value=1,
                clearable=False,
                id='virt_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='virt_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("TURN:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Низкий', 'value': 0.87},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 1.07},
                    {'label': 'Очень высокий', 'value': 1.15}],
                value=1,
                clearable=False,
                id='turn_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='turn_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("ACAP:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 1.46},
                    {'label': 'Низкий', 'value': 1.19},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 0.86},
                    {'label': 'Очень высокий', 'value': 0.71}],
                value=1,
                clearable=False,
                id='acap_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='acap_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("AEXP:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 1.29},
                    {'label': 'Низкий', 'value': 1.15},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 0.91},
                    {'label': 'Очень высокий', 'value': 0.82}],
                value=1,
                clearable=False,
                id='aexp_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='aexp_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("PCAP:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 1.42},
                    {'label': 'Низкий', 'value': 1.17},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 0.86},
                    {'label': 'Очень высокий', 'value': 0.7}],
                value=1,
                clearable=False,
                id='pcap_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='pcap_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("VEXP:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 1.21},
                    {'label': 'Низкий', 'value': 1.1},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 0.9}],
                value=1,
                clearable=False,
                id='vexp_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='vexp_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("LEXP:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 1.14},
                    {'label': 'Низкий', 'value': 1.07},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 0.95}],
                value=1,
                clearable=False,
                id='lexp_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='lexp_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("MODP:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 1.24},
                    {'label': 'Низкий', 'value': 1.1},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 0.91},
                    {'label': 'Очень высокий', 'value': 0.82}],
                value=1,
                clearable=False,
                id='modp_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='modp_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("TOOL:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 1.24},
                    {'label': 'Низкий', 'value': 1.1},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 0.91},
                    {'label': 'Очень высокий', 'value': 0.82}],
                value=1,
                clearable=False,
                id='tool_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='tool_change',
            ))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H4("SCED:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Очень низкий', 'value': 1.23},
                    {'label': 'Низкий', 'value': 1.08},
                    {'label': 'Номинальный', 'value': 1.0},
                    {'label': 'Высокий', 'value': 1.04},
                    {'label': 'Очень высокий', 'value': 1.1}],
                value=1,
                clearable=False,
                id='sced_mode',
            )),
            dbc.Col(
                children=dcc.Checklist(options=[
                    {'label': 'Переменный', 'value': 1}],
                id='sced_change',
            ))
        ], style={"padding": "3px"}
    ),

    dbc.Row(
        [
            dbc.Col(children=html.H4("Количество строк кода (LOC):"), width="auto"),
            dbc.Col(children=dcc.Input(id="loc", type="number", placeholder="", value=430000)),
        ], style={"padding": "3px"}
    ),

    dbc.Row(
        [
            dbc.Col(children=html.H4("Средняя заработная плата:"), width="auto"),
            dbc.Col(children=dcc.Input(id="salary", type="number", placeholder="", value=100000)),
        ], style={"padding": "3px"}
    ),

    dbc.Row(
        [
            dbc.Col(children=html.H4("Тип проекта:"), width="auto"),
            dbc.Col(
                children=dcc.Dropdown(options=[
                    {'label': 'Обычный', 'value': 1},
                    {'label': 'Промежуточный', 'value': 2},
                    {'label': 'Встроенный', 'value': 3}],
                value=1,
                clearable=False,
                id='type_mode',
            ))
        ], style={"padding": "3px"}
    ),

    html.Div([
        dcc.Graph(
            id='norm_work_graph',
            figure=go.Figure(data=[go.Scatter(x=[], y=[])])
        ),
        dcc.Graph(
            id='norm_time_graph',
            figure=go.Figure(data=[go.Scatter(x=[], y=[])])
        )
    ], style={'columnCount': 2}),

    html.Div([
        dcc.Graph(
            id='inter_work_graph',
            figure=go.Figure(data=[go.Scatter(x=[], y=[])])
        ),
        dcc.Graph(
            id='inter_time_graph',
            figure=go.Figure(data=[go.Scatter(x=[], y=[])])
        )
    ], style={'columnCount': 2}),

    html.Div([
        dcc.Graph(
            id='bltin_work_graph',
            figure=go.Figure(data=[go.Scatter(x=[], y=[])])
        ),
        dcc.Graph(
            id='bltin_time_graph',
            figure=go.Figure(data=[go.Scatter(x=[], y=[])])
        )
    ], style={'columnCount': 2}),

    dbc.Row(
        [
            dbc.Col(children=html.H4("Трудозатраты:"), width="auto"),
            dbc.Col(children=html.Div(id='labor')),
            dbc.Col(children=html.H4("Время:"), width="auto"),
            dbc.Col(children=html.Div(id='time')),
        ], style={"padding": "3px"}
    ),

    dbc.Row(
        [
            dbc.Col(children=html.H4("Трудозатраты с планированием:"), width="auto"),
            dbc.Col(children=html.Div(id='labor_plan')),
            dbc.Col(children=html.H4("Время с планированием:"), width="auto"),
            dbc.Col(children=html.Div(id='time_plan')),
        ], style={"padding": "3px"}
    ),

    html.H4("Распределение работ и времени по стадиям жизненного цикла при традиционном подходе"),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Планирование и определение требований:"), width="auto"),
            dbc.Col(children=html.Div(id='trad_1'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Проектирование продукта:"), width="auto"),
            dbc.Col(children=html.Div(id='trad_2'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Детальное проектирование:"), width="auto"),
            dbc.Col(children=html.Div(id='trad_3'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Кодирование и тестирование отдельных модулей:"), width="auto"),
            dbc.Col(children=html.Div(id='trad_4'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Интеграция и тестирование:"), width="auto"),
            dbc.Col(children=html.Div(id='trad_5'))
        ], style={"padding": "3px"}
    ),

    html.H4("Стандартное распределение работ по видам деятельности WBS в модели COCOMO"),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Анализ требований:"), width="auto"),
            dbc.Col(children=html.Div(id='wbs_1'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Проектирование продукта:"), width="auto"),
            dbc.Col(children=html.Div(id='wbs_2'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Программирование:"), width="auto"),
            dbc.Col(children=html.Div(id='wbs_3'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Планирование тестирования:"), width="auto"),
            dbc.Col(children=html.Div(id='wbs_4'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Верификация и аттестация:"), width="auto"),
            dbc.Col(children=html.Div(id='wbs_5'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Канцелярия проекта:"), width="auto"),
            dbc.Col(children=html.Div(id='wbs_6'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Управление конфигурацией и беспечение качества:"), width="auto"),
            dbc.Col(children=html.Div(id='wbs_7'))
        ], style={"padding": "3px"}
    ),
    dbc.Row(
        [
            dbc.Col(children=html.H6("Создание руководств:"), width="auto"),
            dbc.Col(children=html.Div(id='wbs_8'))
        ], style={"padding": "3px"}
    ),

    dbc.Row(
        [
            dbc.Col(children=html.H6("Бюджет:"), width="auto"),
            dbc.Col(children=html.Div(id='wbs_9'))
        ], style={"padding": "3px"}
    ),

    html.H4("Количество работников на протяжении всего цикла создания продукта"),

    dcc.Graph(
        id="graph",
        figure={
            "data": [go.Bar(
                        x=[],
                        y=[])
                    ]
            }
    ),
])

@app.callback(
    [Output("norm_work_graph", "figure"),
     Output("norm_time_graph", "figure"),
     Output("inter_work_graph", "figure"),
     Output("inter_time_graph", "figure"),
     Output("bltin_work_graph", "figure"),
     Output("bltin_time_graph", "figure"),
    ],
    [
        Input("rely_mode", "value"),
        Input("rely_change", "value"),
        Input("data_mode", "value"),
        Input("data_change", "value"),
        Input("cplx_mode", "value"),
        Input("cplx_change", "value"),
        Input("time_mode", "value"),
        Input("time_change", "value"),
        Input("stor_mode", "value"),
        Input("stor_change", "value"),
        Input("virt_mode", "value"),
        Input("virt_change", "value"),
        Input("turn_mode", "value"),
        Input("turn_change", "value"),
        Input("acap_mode", "value"),
        Input("acap_change", "value"),
        Input("aexp_mode", "value"),
        Input("aexp_change", "value"),
        Input("pcap_mode", "value"),
        Input("pcap_change", "value"),
        Input("vexp_mode", "value"),
        Input("vexp_change", "value"),
        Input("lexp_mode", "value"),
        Input("lexp_change", "value"),
        Input("modp_mode", "value"),
        Input("modp_change", "value"),
        Input("tool_mode", "value"),
        Input("tool_change", "value"),
        Input("sced_mode", "value"),
        Input("sced_change", "value"),
    ],
)
def update_graphics(rely_m, rely_c, data_m, data_c, cplx_m, cplx_c,
                    time_m, time_c, stor_m, stor_c, virt_m, virt_c,
                    turn_m, turn_c, acap_m, acap_c, aexp_m, aexp_c,
                    pcap_m, pcap_c, vexp_m, vexp_c, lexp_m, lexp_c,
                    modp_m, modp_c, tool_m, tool_c, sced_m, sced_c):
    attributes = [rely_m, data_m, cplx_m, time_m, stor_m, virt_m,
                  turn_m, acap_m, aexp_m, pcap_m, vexp_m, lexp_m,
                  modp_m, tool_m, sced_m]

    fig_work_norma = go.Figure()
    fig_work_norma.update_layout(title='Оценка трудозатрат при обычном режиме работы',
                   xaxis_title='Значение параметра',
                   yaxis_title='Трудозатраты')

    fig_work_inter = go.Figure()
    fig_work_inter.update_layout(title='Оценка трудозатрат при промежуточном режиме работы',
                   xaxis_title='Значение параметра',
                   yaxis_title='Трудозатраты')

    fig_work_bltin = go.Figure()
    fig_work_bltin.update_layout(title='Оценка трудозатрат при встроенном режиме работы',
                   xaxis_title='Значение параметра',
                   yaxis_title='Трудозатраты')

    fig_time_norma = go.Figure()
    fig_time_norma.update_layout(title='Оценка времени при обычном режиме работы',
                   xaxis_title='Значение параметра',
                   yaxis_title='Время')

    fig_time_inter = go.Figure()
    fig_time_inter.update_layout(title='Оценка времени при промежуточном режиме работы',
                   xaxis_title='Значение параметра',
                   yaxis_title='Время')

    fig_time_bltin = go.Figure()
    fig_time_bltin.update_layout(title='Оценка времени при встроенном режиме работы',
                   xaxis_title='Значение параметра',
                   yaxis_title='Время')

    if rely_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[1:], SIZE, RELY)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_inter,
            name="RELY",
            line=dict(color='rgb(0, 77, 0)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_norma,
            name="RELY",
            line=dict(color='rgb(0, 77, 0)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_bltin,
            name="RELY",
            line=dict(color='rgb(0, 77, 0)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_inter,
            name="RELY",
            line=dict(color='rgb(0, 77, 0)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_norma,
            name="RELY",
            line=dict(color='rgb(0, 77, 0)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_bltin,
            name="RELY",
            line=dict(color='rgb(0, 77, 0)')
        ))
    if data_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:1]+attributes[2:], SIZE, DATA)

        fig_work_inter.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=work_inter,
            name="DATA",
            line=dict(color='rgb(255, 153, 255)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=work_norma,
            name="DATA",
            line=dict(color='rgb(255, 153, 255)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=work_bltin,
            name="DATA",
            line=dict(color='rgb(255, 153, 255)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=time_inter,
            name="DATA",
            line=dict(color='rgb(255, 153, 255)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=time_norma,
            name="DATA",
            line=dict(color='rgb(255, 153, 255)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=time_bltin,
            name="DATA",
            line=dict(color='rgb(255, 153, 255)')
        ))
    if cplx_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:2]+attributes[3:], SIZE, CPLX)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_inter,
            name="CPLX",
            line=dict(color='rgb(153, 153, 255)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_norma,
            name="CPLX",
            line=dict(color='rgb(153, 153, 255)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_bltin,
            name="CPLX",
            line=dict(color='rgb(153, 153, 255)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_inter,
            name="CPLX",
            line=dict(color='rgb(153, 153, 255)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_norma,
            name="CPLX",
            line=dict(color='rgb(153, 153, 255)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_bltin,
            name="CPLX",
            line=dict(color='rgb(153, 153, 255)')
        ))
    if time_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:3]+attributes[4:], SIZE, TIME)

        fig_work_inter.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=work_inter,
            name="TIME",
            line=dict(color='rgb(230, 230, 0)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=work_norma,
            name="TIME",
            line=dict(color='rgb(230, 230, 0)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=work_bltin,
            name="TIME",
            line=dict(color='rgb(230, 230, 0)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=time_inter,
            name="TIME",
            line=dict(color='rgb(230, 230, 0)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=time_norma,
            name="TIME",
            line=dict(color='rgb(230, 230, 0)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=time_bltin,
            name="TIME",
            line=dict(color='rgb(230, 230, 0)')
        ))
    if stor_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:4]+attributes[5:], SIZE, STOR)

        fig_work_inter.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=work_inter,
            name="STOR",
            line=dict(color='rgb(102, 255, 255)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=work_norma,
            name="STOR",
            line=dict(color='rgb(102, 255, 255)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=work_bltin,
            name="STOR",
            line=dict(color='rgb(102, 255, 255)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=time_inter,
            name="STOR",
            line=dict(color='rgb(102, 255, 255)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=time_norma,
            name="STOR",
            line=dict(color='rgb(102, 255, 255)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[2, 3, 4, None],
            y=time_bltin,
            name="STOR",
            line=dict(color='rgb(102, 255, 255)')
        ))
    if virt_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:5]+attributes[6:], SIZE, VIRT)

        fig_work_inter.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=work_inter,
            name="VIRT",
            line=dict(color='rgb(255, 128, 0)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=work_norma,
            name="VIRT",
            line=dict(color='rgb(255, 128, 0)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=work_bltin,
            name="VIRT",
            line=dict(color='rgb(255, 128, 0)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=time_inter,
            name="VIRT",
            line=dict(color='rgb(255, 128, 0)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=time_norma,
            name="VIRT",
            line=dict(color='rgb(255, 128, 0)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=time_bltin,
            name="VIRT",
            line=dict(color='rgb(255, 128, 0)')
        ))
    if turn_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:6]+attributes[7:], SIZE, TURN)

        fig_work_inter.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=work_inter,
            name="TURN",
            line=dict(color='rgb(128, 115, 77)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=work_norma,
            name="TURN",
            line=dict(color='rgb(128, 115, 77)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=work_bltin,
            name="TURN",
            line=dict(color='rgb(128, 115, 77)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=time_inter,
            name="TURN",
            line=dict(color='rgb(128, 115, 77)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=time_norma,
            name="TURN",
            line=dict(color='rgb(128, 115, 77)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[1, 2, 3, 4, None],
            y=time_bltin,
            name="TURN",
            line=dict(color='rgb(128, 115, 77)')
        ))
    if acap_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:7]+attributes[8:], SIZE, ACAP)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_inter,
            name="ACAP",
            line=dict(color='rgb(255, 0, 0)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_norma,
            name="ACAP",
            line=dict(color='rgb(255, 0, 0)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_bltin,
            name="ACAP",
            line=dict(color='rgb(255, 0, 0)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_inter,
            name="ACAP",
            line=dict(color='rgb(255, 0, 0)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_norma,
            name="ACAP",
            line=dict(color='rgb(255, 0, 0)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_bltin,
            name="ACAP",
            line=dict(color='rgb(255, 0, 0)')
        ))
    if aexp_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:8]+attributes[9:], SIZE, AEXP)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_inter,
            name="AEXP",
            line=dict(color='rgb(64, 0, 255)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_norma,
            name="AEXP",
            line=dict(color='rgb(64, 0, 255)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_bltin,
            name="AEXP",
            line=dict(color='rgb(64, 0, 255)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_inter,
            name="AEXP",
            line=dict(color='rgb(64, 0, 255)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_norma,
            name="AEXP",
            line=dict(color='rgb(64, 0, 255)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_bltin,
            name="AEXP",
            line=dict(color='rgb(64, 0, 255)')
        ))
    if pcap_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:9]+attributes[10:], SIZE, PCAP)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_inter,
            name="PCAP",
            line=dict(color='rgb(0, 255, 64)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_norma,
            name="PCAP",
            line=dict(color='rgb(0, 255, 64)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_bltin,
            name="PCAP",
            line=dict(color='rgb(0, 255, 64)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_inter,
            name="PCAP",
            line=dict(color='rgb(0, 255, 64)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_norma,
            name="PCAP",
            line=dict(color='rgb(0, 255, 64)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_bltin,
            name="PCAP",
            line=dict(color='rgb(0, 255, 64)')
        ))
    if vexp_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:10]+attributes[11:], SIZE, VEXP)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=work_inter,
            name="VEXP",
            line=dict(color='rgb(191, 0, 255)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=work_norma,
            name="VEXP",
            line=dict(color='rgb(191, 0, 255)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=work_bltin,
            name="VEXP",
            line=dict(color='rgb(191, 0, 255)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=time_inter,
            name="VEXP",
            line=dict(color='rgb(191, 0, 255)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=time_norma,
            name="VEXP",
            line=dict(color='rgb(191, 0, 255)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=time_bltin,
            name="VEXP",
            line=dict(color='rgb(191, 0, 255)')
        ))
    if lexp_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:11]+attributes[12:], SIZE, LEXP)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=work_inter,
            name="LEXP",
            line=dict(color='rgb(255, 0, 255)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=work_norma,
            name="LEXP",
            line=dict(color='rgb(255, 0, 255)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=work_bltin,
            name="LEXP",
            line=dict(color='rgb(255, 0, 255)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=time_inter,
            name="LEXP",
            line=dict(color='rgb(255, 0, 255)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=time_norma,
            name="LEXP",
            line=dict(color='rgb(255, 0, 255)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, None],
            y=time_bltin,
            name="LEXP",
            line=dict(color='rgb(255, 0, 255)')
        ))
    if modp_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:12]+attributes[13:], SIZE, MODP)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_inter,
            name="MODP",
            line=dict(color='rgb(255, 255, 0)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_norma,
            name="MODP",
            line=dict(color='rgb(255, 255, 0)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_bltin,
            name="MODP",
            line=dict(color='rgb(255, 255, 0)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_inter,
            name="MODP",
            line=dict(color='rgb(255, 255, 0)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_norma,
            name="MODP",
            line=dict(color='rgb(255, 255, 0)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_bltin,
            name="MODP",
            line=dict(color='rgb(255, 255, 0)')
        ))
    if tool_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:13]+attributes[14:], SIZE, TOOL)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_inter,
            name="TOOL",
            line=dict(color='rgb(0, 128, 255)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_norma,
            name="TOOL",
            line=dict(color='rgb(0, 128, 255)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_bltin,
            name="TOOL",
            line=dict(color='rgb(0, 128, 255)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_inter,
            name="TOOL",
            line=dict(color='rgb(0, 128, 255)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_norma,
            name="TOOL",
            line=dict(color='rgb(0, 128, 255)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_bltin,
            name="TOOL",
            line=dict(color='rgb(0, 128, 255)')
        ))
    if sced_c:
        work_norma, work_inter, work_bltin, \
        time_norma, time_inter, time_bltin = change_attribute(attributes[:-1], SIZE, SCED)

        fig_work_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_inter,
            name="SCED",
            line=dict(color='rgb(41, 163, 41)')
        ))
        fig_work_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_norma,
            name="SCED",
            line=dict(color='rgb(41, 163, 41)')
        ))
        fig_work_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=work_bltin,
            name="SCED",
            line=dict(color='rgb(41, 163, 41)')
        ))

        fig_time_inter.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_inter,
            name="SCED",
            line=dict(color='rgb(41, 163, 41)')
        ))
        fig_time_norma.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_norma,
            name="SCED",
            line=dict(color='rgb(41, 163, 41)')
        ))
        fig_time_bltin.add_trace(go.Scatter(
            x=[0, 1, 2, 3, 4, None],
            y=time_bltin,
            name="SCED",
            line=dict(color='rgb(41, 163, 41)')
        ))

    return [fig_work_norma, fig_time_norma,
            fig_work_inter, fig_time_inter,
            fig_work_bltin, fig_time_bltin]

@app.callback(
    [
        Output("labor", "children"),
        Output("time", "children"),
        Output("labor_plan", "children"),
        Output("time_plan", "children"),
        Output("trad_1", "children"),
        Output("trad_2", "children"),
        Output("trad_3", "children"),
        Output("trad_4", "children"),
        Output("trad_5", "children"),
        Output("wbs_1", "children"),
        Output("wbs_2", "children"),
        Output("wbs_3", "children"),
        Output("wbs_4", "children"),
        Output("wbs_5", "children"),
        Output("wbs_6", "children"),
        Output("wbs_7", "children"),
        Output("wbs_8", "children"),
        Output("wbs_9", "children"),
        Output("graph", "figure"),
    ],
    [
        Input("rely_mode", "value"),
        Input("data_mode", "value"),
        Input("cplx_mode", "value"),
        Input("time_mode", "value"),
        Input("stor_mode", "value"),
        Input("virt_mode", "value"),
        Input("turn_mode", "value"),
        Input("acap_mode", "value"),
        Input("aexp_mode", "value"),
        Input("pcap_mode", "value"),
        Input("vexp_mode", "value"),
        Input("lexp_mode", "value"),
        Input("modp_mode", "value"),
        Input("tool_mode", "value"),
        Input("sced_mode", "value"),
        Input("type_mode", "value"),
        Input("loc", "value"),
        Input("salary", "value"),
    ],
)
def update_fields(rely_m, data_m, cplx_m, time_m, stor_m, virt_m, turn_m,
                  acap_m, aexp_m, pcap_m, vexp_m, lexp_m, modp_m, tool_m,
                  sced_m, type, loc, salary):
    attributes = [rely_m, data_m, cplx_m, time_m, stor_m, virt_m,
                  turn_m, acap_m, aexp_m, pcap_m, vexp_m, lexp_m,
                  modp_m, tool_m, sced_m]

    if (type == 1):
        labor = labor_costs(attributes, loc / 1000, NORMA)
        tim  = time(attributes, loc / 1000, NORMA)
    if (type == 2):
        labor = labor_costs(attributes, loc / 1000, INTER)
        tim  = time(attributes, loc / 1000, INTER)
    if (type == 3):
        labor = labor_costs(attributes, loc / 1000, INTER)
        tim  = time(attributes, loc / 1000, INTER)

    labor_new = labor * 1.08
    time_new = int(tim * 1.36)

    x = []
    y = []

    i = 1
    while (i < time_new):
        x.append(i)
        if i < tim * 0.36:
            y.append(round(labor * 0.08 / tim / 0.36))
        elif i < 2 * tim * 0.36:
            y.append(round(labor * 0.18 / tim / 0.36))
        elif i < (2 * tim * 0.36 + tim * 0.18):
            y.append(round(labor * 0.25 / tim / 0.18))
        elif i < (2 * tim * 0.36 + 2 * tim * 0.18):
            y.append(round(labor * 0.26 / tim / 0.18))
        else:
            y.append(round(labor * 0.31 / tim / 0.28))
        i += 1

    figure={"data": [go.Bar(x=x, y=y)]}

    return [round(labor), round(tim), round(labor_new), time_new,
            labor_time(labor * 0.08, tim * 0.36),
            labor_time(labor * 0.18, tim * 0.36),
            labor_time(labor * 0.25, tim * 0.18),
            labor_time(labor * 0.26, tim * 0.18),
            labor_time(labor * 0.31, tim * 0.28),
            round(labor_new * 0.04), round(labor_new * 0.12), round(labor_new * 0.44),
            round(labor_new * 0.06), round(labor_new * 0.14), round(labor_new * 0.07),
            round(labor_new * 0.07), round(labor_new * 0.06), round(salary * labor_new), figure]


def labor_time(labor, time):
    return str(round(labor)) + " человеко-месяцы, " + str(round(time)) + " месяцы"



RELY = {0: 0.75, 1: 0.86, 2: 1.0, 3: 1.15, 4:  1.4}
DATA = {0: None, 1: 0.94, 2: 1.0, 3: 1.08, 4: 1.16}
CPLX = {0:  0.7, 1: 0.85, 2: 1.0, 3: 1.15, 4:  1.3}
TIME = {0: None, 1: None, 2: 1.0, 3: 1.11, 4:  1.5}
STOR = {0: None, 1: None, 2: 1.0, 3: 1.06, 4: 1.21}
VIRT = {0: None, 1: 0.87, 2: 1.0, 3: 1.15, 4:  1.3}
TURN = {0: None, 1: 0.87, 2: 1.0, 3: 1.07, 4: 1.15}
ACAP = {0: 1.46, 1: 1.19, 2: 1.0, 3: 0.86, 4: 0.71}
AEXP = {0: 1.29, 1: 1.15, 2: 1.0, 3: 0.91, 4: 0.82}
PCAP = {0: 1.42, 1: 1.17, 2: 1.0, 3: 0.86, 4:  0.7}
VEXP = {0: 1.21, 1:  1.1, 2: 1.0, 3:  0.9, 4: None}
LEXP = {0: 1.14, 1: 1.07, 2: 1.0, 3: 0.95, 4: None}
MODP = {0: 1.24, 1:  1.1, 2: 1.0, 3: 0.91, 4: 0.82}
TOOL = {0: 1.24, 1:  1.1, 2: 1.0, 3: 0.91, 4: 0.82}
SCED = {0: 1.23, 1: 1.08, 2: 1.0, 3: 1.04, 4:  1.1}

SIZE = 430

NORMA = {'c1': 3.2, 'p1': 1.05, 'c2': 2.5, 'p2': 0.38}
INTER = {'c1': 3.0, 'p1': 1.12, 'c2': 2.5, 'p2': 0.35}
BLTIN = {'c1': 2.8, 'p1':  1.2, 'c2': 2.5, 'p2': 0.32}

def eaf(attributes):
    res = 1
    for atr in attributes:
        res *= atr
    return res

def labor_costs(eaf_atrs, size, mode):
    return mode['c1'] * eaf(eaf_atrs) * size ** mode['p1']

def time(eaf_atrs, size, mode):
    return mode['c2'] * labor_costs(eaf_atrs, size, mode) ** mode['p2']

def change_attribute(attributes, size, attr):
    work_norma = []
    work_inter = []
    work_bltin = []

    time_norma = []
    time_inter = []
    time_bltin = []

    for mode in attr.keys():
        if (attr[mode] != None):
            work_norma.append(labor_costs(attributes + [attr[mode]], size, NORMA))
            work_inter.append(labor_costs(attributes + [attr[mode]], size, INTER))
            work_bltin.append(labor_costs(attributes + [attr[mode]], size, BLTIN))
            time_norma.append(time(attributes + [attr[mode]], size, NORMA))
            time_inter.append(time(attributes + [attr[mode]], size, INTER))
            time_bltin.append(time(attributes + [attr[mode]], size, BLTIN))

    return work_norma, work_inter, work_bltin, time_norma, time_inter, time_bltin

if __name__ == '__main__':
    app.run_server(debug=True)
