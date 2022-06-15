from mpi4py import MPI


if __name__ == '__main__':
    N = 10
    L = []

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    nb_proc = comm.Get_size()

    for i in range(int(N/nb_proc*rank), int(N/nb_proc*(rank+1))):
        L.append(i)

    data = comm.gather(L, root=0)
    if rank == 0:
        print(data)
