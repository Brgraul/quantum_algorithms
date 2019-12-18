import numpy as np, numpy.random

def random_density_operator(n_qubits:int):
    """ Creates a random density operator for testing purposes. Fulfills the properties:
    1. Operator has trace equal to one
    2. Operator is positive
    :param n_qubits: Number of qubits of the system represented
    :return: np.array of dimension 2^n_qubits x 2^n_qubits containing a qualified
    density operator
    """
    # TODO
    return 0

def partial_trace(rho:np.array, dimA:int, dimB:int):
    """ Calculates the partial trace of a given density operator rho.

    :param rho:
    :param dimA:
    :param dimB:
    :return:
    """

    return

if __name__ == "__main__":
    p = np.random.dirichlet(np.ones(4),size=1)
    ensemble = [(p[0][0], "00"), (p[0][1], "01"), (p[0][2], "10"), (p[0][3], "11")]
    partial_trace(ex, ex1, ex2)
