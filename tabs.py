import PySimpleGUI as sg

sg.set_options(font=("Arial", 16))
sg.theme("Black")

sort_list = ['Insertion Sort', 'Bubble Sort', 'Quick Sort', 'Selection Sort', 'Heap Sort', 'Heap Sort 2',
             'Shell Sort', 'Radix Sort', 'Cocktail Sort', 'Gnome Sort', 'Pigeonhole Sort', 'Bead Sort']

tab1 = [[sg.Listbox(values=sort_list, size=(30, 6), key="Sort", bind_return_key=True), sg.Column([[sg.Text(text="Number of Integers")], [sg.InputText("10", key="int_size", size=(17, 10), pad=((5, 5), (2, 0)), justification="center")], [sg.Button("Calculate", key='int_sort', pad=((0, 0), (12, 0)))]], element_justification="center"), sg.Column([[sg.Text(text="Number of Iterations")], [sg.InputText("1", key="iterator", size=(17, 10), pad=((5, 5), (2, 0)), justification="center")]], element_justification="center", pad=((0, 0), (0, 52)))],
        [sg.Multiline(size=(81, 20), key="int_output", font="Arial 16", do_not_clear=False)]]

tab2 = [[sg.Listbox(values=sort_list, size=(30, 6), key="Sort_1"), sg.Column([[sg.Text(text="Number of Integers")], [sg.InputText("10", key="Calc_comp", size=(17, 10), pad=((5, 5), (2, 0)), justification="center")], [sg.Button("Calculate", key='comp_sort', pad=((0, 0), (12, 0)))]], element_justification="center"), sg.Listbox(values=sort_list, size=(30, 6), key="Sort_2")],
        [sg.Multiline(size=(81, 20), key="comp_output", font="Arial 16")]]

tab3 = [[sg.InputText("10", key="str_comp", size=(17, 10), pad=((5, 0), (10, 5))), sg.Text(text="Number of Strings", pad=((5, 0), (10, 0)))],
        [sg.InputText("1", key="str_size", size=(17, 10)), sg.Text(text="Length of Strings")],
        [sg.Button("Calculate", key='str_sort', pad=((5, 0), (15, 10)))],
        [sg.Multiline(size=(81, 20), key="str_output", font="Arial 16", pad=((5, 0), (19, 0)), do_not_clear=False)]]

tab4 = [[sg.Listbox(values=sort_list, size=(30, 6), key="glossary", bind_return_key=True)],
        [sg.Multiline(size=(81, 20), key="glossary_output", font="Arial 16", do_not_clear=False)]]

tab5 = [[sg.Multiline(size=(81, 25), key="history_output", font="Arial 16", pad=((5, 5), (36, 0)))]]

tab6 = [[sg.Drop(values=sort_list, enable_events=True, key="average")],
        [sg.Multiline(size=(81, 25), key="avg_output", font="Arial 16", do_not_clear=False)]]

tab_grp = [[sg.TabGroup([[sg.Tab("Integer Sort  ", tab1),
                          sg.Tab("Comparison Sort  ", tab2),
                          sg.Tab("String Sort  ", tab3),
                          sg.Tab("Glossary  ", tab4),
                          sg.Tab("History  ", tab5),
                          sg.Tab("Averages ", tab6)]])]]
