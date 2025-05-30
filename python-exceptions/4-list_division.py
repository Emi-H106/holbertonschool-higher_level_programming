#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            elem1 = my_list_1[i] if i < len(my_list_1) else None
            elem2 = my_list_2[i] if i < len(my_list_2) else None

            if elem1 is None or elem2 is None:
                raise IndexError("out of range")

            if (not isinstance(elem1, (int, float)) or
                    not isinstance(elem2, (int, float))):
                raise TypeError("wrong type")

            if elem2 == 0:
                raise ZeroDivisionError("division by 0")

            result.append(elem1 / elem2)

        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result
