
PHASES = [
    {'phase_name': 'Phase 1', 'time': 10},
    {'phase_name': 'Phase 2', 'time': 10},
]


my_iter = iter(PHASES)




def func (phase_name, time):
    print(phase_name)
    print(time)


func(**next(my_iter))

func(**next(my_iter))

