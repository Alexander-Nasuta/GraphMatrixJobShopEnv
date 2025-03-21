from graph_matrix_jsp_env.disjunctive_jsp_env import DisjunctiveGraphJspEnv
import numpy as np

if __name__ == '__main__':
    custom_jsp_instance = np.array([
        [
            [0, 1, 2, 3],  # job 0
            [0, 2, 1, 3]  # job 1
        ],
        [
            [11, 3, 3, 12],  # task durations of job 0
            [5, 16, 7, 4]  # task durations of job 1
        ]

    ], dtype=np.int32)
    env = DisjunctiveGraphJspEnv(
        jsp_instance=custom_jsp_instance,
    )
    obs, info = env.reset()
    env.render(mode='debug') #

    for a in [5, 1, 2, 6, 3, 7, 4, 8]:
        obs, reward, terminated, truncated, info  = env.step(a)
        env.render(mode='debug', wait=None)

    env.render()
