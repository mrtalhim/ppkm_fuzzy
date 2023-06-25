import PySimpleGUI as sg
import pickle
def inputColumn(tx: list):
    return [
        sg.Text(tx[0], font='Courier 12'),
        sg.InputText(key=tx[1])
    ]

def predict(x):
    with open('FS1.pickle', 'rb') as f:
        FS = pickle.load(f)

    with open('FS2.pickle', 'rb') as f:
        FS2 = pickle.load(f)
    
    input = {'new_cases':float(x['NEW_CASE']),
            'hospitalization_rate':float(x['HOSPITALIZATION_RATE']),
            'mortality':float(x['MORTALITY']),
            'testing':float(x['TESTING']),
            'tracing_ratio':float(x['TRACING_RATIO']),
            'bed_occupancy_rate':float(x['BED_OCCOPANCY_RATE'])
            }

    for label, data in input.items():
        FS.set_variable(label, data)

    result = FS.Mamdani_inference()
    result = result['ppkm']
    FS2.set_variable('ppkm', round(result))
    FS2.set_variable('vaksin_umum', float(x['VAKSIN_UMUM']))
    FS2.set_variable('vaksin_lansia', float(x['VAKSIN_LANSIA']))

    result = FS2.inference()
    return result['output']

def home():
    layout = [
        inputColumn(['Kasus Baru            ', 'NEW_CASE']),
        inputColumn(['Rawat Inap RS         ', 'HOSPITALIZATION_RATE']),
        inputColumn(['Kematian              ', 'MORTALITY']),
        inputColumn(['Testing               ', 'TESTING']),
        inputColumn(['Tracing               ', 'TRACING_RATIO']),
        inputColumn(['Treatment             ', 'BED_OCCOPANCY_RATE']),
        inputColumn(['Vaksin Lengkap Total  ', 'VAKSIN_UMUM']),
        inputColumn(['Vaksin Lengkap Lansia ', 'VAKSIN_LANSIA']),
        [sg.Text('PPKM Level: ', key='OUTPUT', font='Courier 12')],
        [
            sg.Button('Proses', key='PROSES', font='Courier 12'),
            sg.Button('Reset', key='RESET', font='Courier 12')]
    ]
    
    window = sg.Window('FIS PPKM', layout, element_justification='left')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == 'PROSES':
            output = predict(values)
            window['OUTPUT'].update(' '.join(['PPKM Level', str(int(output))]))

    window.close()

if __name__ == "__main__":
    home()