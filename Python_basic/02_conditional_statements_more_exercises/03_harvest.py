from math import floor, ceil

vineyard_sqr_metres = int(input())
grapes_per_sqr_metre = float(input())
req_wine_litres = int(input())
worker_count = int(input())

wine_production_raw = (vineyard_sqr_metres * grapes_per_sqr_metre) * 0.40
produced_wine = wine_production_raw / 2.5
extra_wine = produced_wine - req_wine_litres

if produced_wine < req_wine_litres:
    print(f'It will be a tough winter! More {floor(req_wine_litres - produced_wine)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(produced_wine)} liters.')
    print(f'{ceil(extra_wine)} liters left -> {ceil(extra_wine / worker_count)} liters per person.')
