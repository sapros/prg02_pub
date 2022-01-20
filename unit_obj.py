war_unit = ['unit_type', 'unit_health', 'unit_streight', 'unit_dexterity', 'unit_speed', 'unit_defence',
            'unit_wearpon_type']
war_unit.append('new_option')
print(war_unit)

droped_property = war_unit.pop()
print(war_unit)
print(droped_property)

a = len(war_unit)
a = a - 1
war_unit_rebuild = []
print(f"list contain is {a} indeces")
while a >= 0:
    print(f" {war_unit[a]} ")
    current_idex_content = ''
    current_idex_content = war_unit.pop(a)
    current_idex_content = current_idex_content.lower()
    war_unit_rebuild.append(current_idex_content)
    a = a - 1
    print(war_unit)


# war_unit_rebuild.sort(reverse=True)  #постоянное изменение сортировки
print(f"rebuilded list sorted appearance:\n{sorted(war_unit_rebuild)}")
print(f"rebuilded list sorted appearance (reversed):\n {sorted(war_unit_rebuild, reverse=True)}")
print(f"real list appearance \n{war_unit_rebuild}")
print(f"rebuid list contain is {len(war_unit_rebuild) - 1} indeces")

for val in war_unit_rebuild:
    print(val)
