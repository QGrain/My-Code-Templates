import argparse


def main():
    parser = argparse.ArgumentParser(description='Description here')
    parser.add_argument('-s', '--string', type=str, dest='str_val', default='default string', help='explanation')
    parser.add_argument('-i', '--int', type=int, dest='int_val', default='2333', help='explanation')
    # nargs='*', at least specify 0 value
    parser.add_argument('-x', '--xin', type=str, dest='xin_list', nargs='*', help='explanation')
    # nargs='+', at least specify 1 value
    parser.add_argument('-j', '--jia', type=str, dest='jia_list', nargs='+', help='explanation')
    parser.add_argument('-f', '--float', type=float, dest='float_val', default='2.333', help='explanation')
    parser.add_argument('-D', '--DEBUG', action='store_true', help='DEBUG mode')
    parser.add_argument('-v', '--verbose', action='store_true', help='show verbose output')
    args = parser.parse_args()

    print('args.str_val=%s'%args.str_val)
    print('args.int_val=%d'%args.int_val)
    print('args.float_val=%.4f'%args.float_val)
    print('args.DEBUG', args.DEBUG)
    print('args.verbose', args.verbose)

    if args.xin_list:
        print('args.xin_list:')
        for x in args.xin_list:
            print(x)
    if args.jia_list:
        print('args.jia_list')
        for j in args.jia_list:
            print(j)

if __name__ == '__main__':
    main()