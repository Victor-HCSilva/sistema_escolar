def p():
    print("Ola mundo")


class T:
    def r():
        p()
        return


s = T

s.r()
