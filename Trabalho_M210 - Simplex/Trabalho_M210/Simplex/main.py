import PySimpleGUI as sg

def get_variable_names(variable_count):
    layout = [[sg.Text(f"Nome da Variável {i+1}: "), sg.InputText(key=f'var_{i+1}',size=(5,0))] for i in range(variable_count)]
    layout.append([sg.Button('Ok')])
    window = sg.Window('Nomes das Variáveis', layout)
    values = None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Ok'):
            break

    window.close()
    return [values[f'var_{i+1}'] for i in range(variable_count)]

def get_obj_coefficients(variable_names):
    layout = [[sg.Text(f"Coeficiente da {var}: "), sg.InputText(key=f'obj_coeff_{var}',size=(5,0))] for var in variable_names]
    layout.append([sg.Button('Ok')])
    window = sg.Window('Coeficientes da Função Objetivo', layout)
    values = None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Ok'):
            break

    window.close()
    return [values[f'obj_coeff_{var}'] for var in variable_names]

def get_constraint_coefficients(variable_names, constraint_count):
    layout = []
    for i in range(constraint_count):
        row_layout = [sg.Text(f"Coeficientes da Restrição {i+1}: ")]
        row_layout.extend([sg.InputText(key=f'constraint_{i+1}_{var}',size=(5,0)) for var in variable_names])
        row_layout.extend([sg.Text('<=') , sg.InputText(key=f'constraint_const_{i+1}',size=(5,0))])
        layout.append(row_layout)

    layout.append([sg.Button('Ok')])
    window = sg.Window(f'Coeficientes das Restrições', layout)
    values = None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Ok'):
            break

    window.close()
    return values  # Retorna todos os valores das restrições

def display_results(variable_names, obj_coefficients, constraint_coefficients):
    print("Nomes das Variáveis:")
    print(variable_names)
    print("Coeficientes da Função Objetivo:")
    print(obj_coefficients)
    print("Coeficientes das Restrições:")
    print(constraint_coefficients)

def main():
    sg.theme('LightGrey1')

    # Tela 1 - Entrada de Variáveis e Restrições
    layout1 = [
        [sg.Text('Quantidade de Variáveis de Decisão: ', size=(20,0)), sg.InputText(key='var_count',size=(5,0))],
        [sg.Text('Quantidade de Restrições: ', size=(20,0)), sg.InputText(key='constraint_count',size=(5,0))],
        [sg.Button('Próximo')]
    ]
    window1 = sg.Window('Entrada de Dados', layout1)

    while True:
        event1, values1 = window1.read()
        if event1 == sg.WIN_CLOSED:
            break
        if event1 == 'Próximo':
            var_count = int(values1['var_count'])
            constraint_count = int(values1['constraint_count'])
            break

    window1.close()

    # Tela 2 - Nomes das Variáveis e Coeficientes da Função Objetivo
    variable_names = get_variable_names(var_count)
    obj_coefficients = get_obj_coefficients(variable_names)

    # Tela 3 - Coeficientes das Restrições
    constraint_coefficients = get_constraint_coefficients(variable_names, constraint_count)

    # Exibir os dados coletados
    display_results(variable_names, obj_coefficients, constraint_coefficients)

    # Aqui você pode chamar seu código para resolver o problema de programação linear
    # Utilize as variáveis 'variable_names', 'obj_coefficients' e 'constraint_coefficients'
    # para realizar os cálculos ou chame uma função que faça isso.

if __name__ == '__main__':
    main()
