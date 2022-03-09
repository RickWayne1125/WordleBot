from time import perf_counter


def title_bar(title):
    print()
    print('=' * 60)
    print('{:^60}'.format(title))
    print('-' * 60)


def progress_bar(index, length, start):
    ratio = 50.0 / length
    progress = (index / length) * 100
    finished = '*' * (int(index * ratio) + 1)
    remained = '.' * (49 - int(index * ratio))
    dur = perf_counter() - start
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(progress, finished, remained, dur), end='')
