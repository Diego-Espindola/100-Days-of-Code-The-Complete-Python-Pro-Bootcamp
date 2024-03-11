def main():
    try:
        it = input('Write it bro: ')
        if it == 's':
            raise KeyError
    except KeyError:
        main()
    finally:
        print('hey')


if __name__ == '__main__':
    main()
