import PySimpleGUI as sg
from tabs import tab_grp
from match_file import sort_choice
from string_sort_functions import single_string_sort, multi_string_sort
from glossary import gloss_text
from average import total_list


window = sg.Window("Sort Program", tab_grp)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
       
    if event == 'int_sort':
        try:
            arr_size = int(values['int_size'])
            sort_type = values['Sort'][0]
            iterations = int(values["iterator"])
            for i in range(iterations):
                total_time = sort_choice(arr_size, sort_type)
                window["int_output"].print(f"{sort_type} took {total_time * 1000:0.0f} milliseconds ({total_time*1:0.3f} seconds) to sort {arr_size:,d} integers")
                window["history_output"].print(f"{sort_type} took {total_time * 1000:0.0f} milliseconds ({total_time*1:0.3f} seconds) to sort {arr_size:,d} integers")
                window.refresh()
                total_list.append([sort_type, arr_size, total_time])
        except IndexError:
            window["int_output"].print("Please select a sort type.")
        except ValueError:
            window["int_output"].print("Please enter a numerical value")

    if event == 'comp_sort':
        try:
            arr_size = int(values['Calc_comp'])
            sort_type_1 = values['Sort_1'][0]
            sort_type_2 = values['Sort_2'][0]
            time_1 = sort_choice(arr_size, sort_type_1)
            time_2 = sort_choice(arr_size, sort_type_2)
            window["comp_output"].print(f"{sort_type_1} took {time_1 * 1000:0.0f} milliseconds "
                                        f"and {sort_type_2} took {time_2 * 1000:0.0f} milliseconds to sort {arr_size} integers")
            total_list.append([sort_type_1, arr_size, time_1])
            total_list.append([sort_type_2, arr_size, time_2])

        except IndexError:
            window["comp_output"].print("Please select the sort types you want to compare. ")
        except ValueError:
            window["comp_output"].print("Please enter a numerical value")

    if event == "str_sort":
        try:
            arr_size = int(values['str_comp'])
            str_size = int(values['str_size'])
            if str_size > 1:
                window["str_output"].print(f"Sorted {arr_size} strings with a length of {str_size} characters in {multi_string_sort(arr_size, str_size) * 1000:0.0f} milliseconds")
            else:
                x = single_string_sort(arr_size)
                window["str_output"].print(f"Sorted {arr_size} strings with a length of {str_size} character in {x*1000:0.0f} milliseconds")
        except ValueError:
            window["str_output"].print("Wrong value indicated")

    if event == "glossary":
        gloss_id = values["glossary"][0]
        window["glossary_output"].print(gloss_text(gloss_id))

    if event == "average":
        avg_value = values["average"]
        count = 0
        total_arr = 0
        time_total = 0
        for lst in total_list:
            if lst[0] == avg_value:
                count += 1
                total_arr += lst[1]
                time_total += lst[2]
        if time_total > 0:
            window["avg_output"].print(f"{avg_value} was run {count} times. The average number of integers was {int(total_arr / count)} and the average run-time was {(time_total / count) * 1000:0.0f} milliseconds")
        else:
            window["avg_output"].print("I need some more data first")


window.close()
