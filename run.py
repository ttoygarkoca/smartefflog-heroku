import dash
import datetime
import dash_core_components as dcc
import dash_html_components as html
import json
import random
import requests




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
response = requests.get("https://smarteff.herokuapp.com/ListPersons")

response = response.text
loaded = json.loads(response)

allUsers = []
idSize = []
idLer=[]
for p in loaded['people']:
    allUsers.append(p['name'])
    idLer.append(p['id'])


hash = dict(zip(allUsers,idLer))


print(allUsers[0]+' '+allUsers[1])

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
valuee = 'Inside'
events = []
datetimes = []

user = []
time = []
date = []
action = []
randomId=4000
randomAct=["enter","exit"]
randomTimeHour=["08","09","10","11","12","13","14","15","16","17","18"]
randomTimeMin= ["10","20","30","40","50","00"]
randomChoiceforId=[2,3,4,5,6,7,8,9,10,11,12,13,14]
randomAction=""


nameAndId = { i : allUsers[i] for i in range(0, len(allUsers) ) }





inside = []
outside = []
inUsers = ""
outUsers = ""

temp = ""
dyear = datetime.datetime.now().strftime('%d-%m-%Y')
dtime = datetime.datetime.now().strftime('%H:%M:%S')
data = {}
dataName = {}
dataDate = {}
dataTime = {}
dataAct = {}
randomDay=dyear[0:2]

app.layout = html.Div(children=[
    html.H1(children='\tEnter/Exit Simulation', style={'marginLeft': 400}),

    html.Div(children='''
        Current Time:
    ''', style={'color': 'black', 'fontSize': 30, 'marginTop': 50}),
    html.H1(dcc.Input(id='input-box-date', type='text', value=datetime.datetime.now().strftime('%d-%m-%Y')),
            style={'opacity': '1', 'color': 'black', 'fontSize': 15, 'display': 'inline-block'}),
    html.H1(dcc.Input(id='input-box-time', type='text', value=datetime.datetime.now().strftime('%H:%M:%S')),
            style={'opacity': '1', 'color': 'black', 'fontSize': 15}),
    html.Div(children='''
                Options
            ''', style={'color': 'black', 'fontSize': 20, 'marginLeft': 600}),
    dcc.Dropdown(id='ozellikler',
                 options=[
                     {'label': 'Show Users Inside', 'value': 1},
                     {'label': 'Show Users Outside', 'value': 2},
                     {'label': 'Show Devices in Use', 'value': 3},
                     {'label': 'Show Devices Used By a User', 'value': 4},
                     {'label': 'Turn All Devices On', 'value': 5}
                 ],
                 value='1',
                 style={'width': '50%', 'marginLeft': 300}
                 ),
    html.Button('View The Event Log', id='button1', style={'marginLeft': 550}),
    html.Button('Export the Event Log', id='button2', style={'marginLeft': 10}),
    html.H1(dcc.Input(id='logFileId', type='text', value='Enter here name of Log File'),
            style={'opacity': '1', 'color': 'black', 'fontSize': 15, 'display': 'inline-block'}),
    html.Div(id='output-container-button2', style={'color': 'Black', 'fontSize': 18}),

    html.Div(children='''
        SELECT USER
    ''', style={'color': 'black', 'fontSize': 20}),

    dcc.Dropdown(id='input-box1',
                 options=[
                     {'label': 'John', 'value': 'John'},
                     {'label': 'Jane', 'value': 'Jane'},
                     {'label': 'Ali', 'value': 'Ali'},
                     {'label': 'Veli', 'value': 'Veli'},
                     {'label': 'Ayşe', 'value': 'Ayşe'},
                     {'label': 'Fatma', 'value': 'Fatma'}
                 ],
                 value='x',
                 style={'width': '50%'}
                 ),
    html.Div(children='''
      
    ''', style={'color': 'black', 'fontSize': 30, 'marginLeft': 600}),
    html.Div(id='display-options', style={'color': 'red', 'width': '50%','fontSize': 18, 'marginLeft': 550}),

    html.Div(children='''
        Inside/Outside
    ''', style={'color': 'black', 'fontSize': 30, 'marginTop': 50}),
    html.Div(id='display-selected-values', style={'color': 'red', 'fontSize': 18, 'marginTop': 10}),

    html.Div(children='''
        Action
    ''', style={'color': 'black', 'fontSize': 30, 'marginTop': 50}),
    html.Button('Enter', id='button'),
    html.Button('Exit', id='buttonE', style={'color':'Red','marginLeft': 10}),
    html.Div(id='output-container-button4', style={'color': 'Black', 'fontSize': 18}),
    html.Button('SIMULATE', id='buttonSim', style={'backgroundColor':'Black','color':'Red','marginLeft': 20,'marginTop': 15,'fontSize': 20}),
    html.Div(id='output-container-button', style={'color': 'Black', 'fontSize': 18}),
    html.Div(id='output-container-button3', style={'color': 'Black', 'fontSize': 18})

]
    , style={'marginBottom': 50, 'marginTop': 25, 'marginLeft': 100})


@app.callback(
    dash.dependencies.Output('output-container-button4', 'children'),
    [dash.dependencies.Input('buttonSim', 'n_clicks')],[dash.dependencies.State('input-box1', 'value')])

def simulate_event(n_clicks, value):
    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )
    global randomId
    global randomDay
    tutDay=""
    dayInt=int(randomDay)
    if n_clicks == 1:
        for o in range(5):
            for z in range(30):
                isim=random.choice(allUsers)
                randomAction=random.choice(randomAct)
                if randomAction == 'enter':
                    if isim in inside:
                        a = 2
                    else:
                        if isim in outside:
                            outside.remove(isim)
                        inside.append(isim)
                        user.append(isim)
                        idSize.append(hash[isim])
                        tutDay=randomDay+dyear[2:]
                        if tutDay[1] == '-':
                            tutDay = "0" + tutDay
                        date.append(tutDay)
                        tutSaat = random.choice(randomTimeHour)
                        tutDakika = random.choice(randomTimeMin)
                        dtime2 = tutSaat + ":" + tutDakika + ":" + dtime[6:]
                        time.append(dtime2)
                        action.append(randomAction)

                if randomAction == 'exit':
                    if isim in outside:
                        a = 2
                    else:
                        if isim in inside:
                            inside.remove(isim)
                        outside.append(isim)
                        user.append(isim)
                        idSize.append(hash[isim])
                        tutDay = randomDay + dyear[2:]
                        if tutDay[1] == '-':
                            tutDay = "0" + tutDay
                        date.append(tutDay)
                        tutSaat = random.choice(randomTimeHour)
                        tutDakika = random.choice(randomTimeMin)
                        dtime2=tutSaat+":"+tutDakika+":"+dtime[6:]
                        time.append(dtime2)
                        action.append(randomAction)
            dayInt=dayInt+1
            randomDay = str(dayInt)






@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box1', 'value'),
     dash.dependencies.State('input-box-time', 'value'),
     dash.dependencies.State('input-box-date', 'value')])
def enter_event(n_clicks, value, value3, value2):

    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )
    acti = "enter"
    if (value != 'x'):
        if (value in inside):
            a = 2
        else:
            if (value in outside):
                outside.remove(value)
            inside.append(value)

            # events.append(value+","+dyear+","+dtime+","+acti)
            dyear = value2
            dtime = value3
            user.append(value)
            idSize.append(hash[value])

            date.append(dyear)
            time.append(dtime)
            action.append(acti)


@app.callback(
    dash.dependencies.Output('output-container-button3', 'children'),
    [dash.dependencies.Input('buttonE', 'n_clicks')],
    [dash.dependencies.State('input-box1', 'value'),
     dash.dependencies.State('input-box-time', 'value'),
     dash.dependencies.State('input-box-date', 'value')])
def exit_event(n_clicks, value, value3, value2):
    global randomId
    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )

    act = "exit"
    if (value != 'x'):
        if (value in outside):
            a = 2
        else:
            if (value in inside):
                inside.remove(value)
            outside.append(value)
            # events.append(value + "," + dyear + "," + dtime + "," + act)
            dyear = value2
            dtime = value3
            user.append(value)
            idSize.append(hash[value])
            date.append(dyear)
            time.append(dtime)
            action.append(act)


@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('input-box1', 'value'), dash.dependencies.Input('buttonE', 'n_clicks')])
def update_input(value, n_clicks):
    if value in outside:
        return "outside"
    if value in inside:
        return "inside"
    else:
        return "-"


@app.callback(
    dash.dependencies.Output('display-options', 'children'),
    [dash.dependencies.Input('button1', 'n_clicks')],
    [dash.dependencies.State('ozellikler', 'value')])
def update_input2(value, n_clicks):
    global inUsers
    global outUsers
    for x in inside:
        inUsers = inUsers + "," + x

    for y in outside:
        outUsers = outUsers + "," + y

    if value == 1:
        return "Users Inside:\n" + inUsers
    if value == 2:
        return "Users Outside:\n" + outUsers
    if value == 3:
        return ""
    if value == 4:
        return ""
    if value == 5:
        return ""
    else:
        return ""


@app.callback(
    dash.dependencies.Output('output-container-button2', 'children'),
    [dash.dependencies.Input('button2', 'n_clicks')],
    [dash.dependencies.State('logFileId', 'value'),
    dash.dependencies.State('input-box1', 'value')])
def update_backlog(n_clicks, value2,value):
    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )
    if n_clicks == 1:
        events.append(user)
        events.append(idSize)
        events.append(date)
        events.append(time)
        events.append(action)


        index=0
        logFileName=value2
        data['events']=[]
        for i in user:
            data['events'].append({
                'name': user[index],
                'id': idSize[index],
                'date': date[index],
                'time': time[index],
                'action': action[index]
            })
            index=index+1


        with open("data.json", 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, sort_keys=False, indent=4, ensure_ascii=False)


        URL = "https://smarteff.herokuapp.com/SaveEvent/"
        URL=URL+logFileName

        headers={'Content-type': 'application/json', 'Accept':'text/plain'}
        r = requests.post(url=URL, data=json.dumps(data),headers=headers)


if __name__ == '__main__':
    app.run_server(debug=True)
