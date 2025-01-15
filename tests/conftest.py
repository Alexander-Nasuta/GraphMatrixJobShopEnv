import pytest


@pytest.fixture(scope="function")
def custom_jsp_instance():
    import numpy as np
    custom_jsp_instance = np.array([
        [
            [0, 1, 2, 3],  # job 0
            [0, 2, 1, 3]  # job 1
        ],
        [
            [11, 3, 3, 12],  # task durations of job 0
            [5, 16, 7, 4]  # task durations of job 1
        ]
    ], dtype=np.int32)  # dtype=np.int32 is necessary for the Rust wrapper
    yield custom_jsp_instance


@pytest.fixture(scope="function")
def ft06():
    import numpy as np
    ft06 = np.array([[[2, 0, 1, 3, 5, 4],
                      [1, 2, 4, 5, 0, 3],
                      [2, 3, 5, 0, 1, 4],
                      [1, 0, 2, 3, 4, 5],
                      [2, 1, 4, 5, 0, 3],
                      [1, 3, 5, 0, 4, 2]],

                     [[1, 3, 6, 7, 3, 6],
                      [8, 5, 10, 10, 10, 4],
                      [5, 4, 8, 9, 1, 7],
                      [5, 5, 5, 3, 8, 9],
                      [9, 3, 5, 4, 3, 1],
                      [3, 3, 9, 10, 4, 1]]
                     ])
    yield ft06


@pytest.fixture(scope="function")
def left_shift_jsp_instance():
    import numpy as np
    jsp_left_shift_instance = np.array([
        [
            [0, 1, 2],  # job 0
            [2, 0, 1],  # job 1
            [0, 2, 1]  # job 3
        ],
        [
            [1, 1, 5],  # task durations of job 0
            [5, 3, 3],  # task durations of job 1
            [3, 6, 3]  # task durations of job 1
        ]
    ])
    yield jsp_left_shift_instance


@pytest.fixture(scope="function")
def env(custom_jsp_instance):
    from graph_matrix_jsp_env.disjunctive_jsp_env import DisjunctiveGraphJspEnv

    env = DisjunctiveGraphJspEnv(
        jsp_instance=custom_jsp_instance,
        c_lb=0,
    )
    yield env


@pytest.fixture(scope="function")
def python_env_ft06(ft06):
    from graph_matrix_jsp_env.disjunctive_jsp_env import DisjunctiveGraphJspEnv

    env = DisjunctiveGraphJspEnv(
        jsp_instance=ft06,
        c_lb=0,
    )
    yield env


