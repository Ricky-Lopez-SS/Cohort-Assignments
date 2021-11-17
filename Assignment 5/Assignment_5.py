import numpy as np


if __name__ == '__main__' :

    

    print("2. {}\n".format(np.zeros(10)) )

    print("3. {}\n".format(np.ones(10)) )

    arr = np.arange(0,10)

    arr[:] = 5

    print("4. {}\n".format( arr ) ) 

    print("5. {}\n".format(np.arange(10, 51)))

    print("6. {}\n".format(np.arange(10,51,2)))

    print("7. {}\n".format(np.arange(0,9).reshape(3,3)))

    print("8. {}\n".format(np.eye(3,3)))

    print("9. {}\n".format(np.random.rand(1)))


