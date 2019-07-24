# Steal money from houses to get maximum value without stealing from adjascent houses

def house_thief(house_networth: list, current_index: int):
    if current_index > len(house_networth):
        return 0
    steal_current_house = house_networth[current_index] + house_thief(house_networth, current_index + 2)
    skip_current_house = house_thief(current_index + 1)
    
    return max(steal_current_house, skip_current_house)


def house_thief_top_down(house_networth: list, current_index: int):
    mem = {}
    if current_index not in mem:
        mem[i] = max(house_thief(house_networth, current_index + 1), (house_networth[i] + house_thief(house_networth, current_index + 2)))
    return mem[current_index]

def house_thief_bottom_up(house_networth: list, current_index: int):
    mem = {}
    if current_index > len(house_networth):
        return 0
    mem[n+1] = 