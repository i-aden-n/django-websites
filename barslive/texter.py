ready_text = ''

with open('to_conv.txt', 'r', encoding = 'utf-8') as file:
    # print(file.read().splitlines())
    for l in file.read().splitlines():
        if l != '':
            if l[0] == 'h':
                ready_text += f'<h2 class="item__headline">{l}</h2>'
                print(f'<h2 class="item__headline">{l}</h2>')
            else: 
                ready_text += f'<p class="item__paragraph">{l}</p>'
                print(f'<p class="item__paragraph">{l}</p>')