import numpy as np
from jsp_instance_utils.instances import ft06

from graph_jsp_env.disjunctive_graph_jsp_env import DisjunctiveGraphJspEnv as GraphJspEnv
from graph_matrix_jsp_env.disjunctive_jsp_env import DisjunctiveGraphJspEnv as GraphMatrixEnv

if __name__ == '__main__':
    env_kwargs = {
        "jps_instance": ft06,
        "default_visualisations": ["gantt_console", "graph_console"],
        "reward_function_parameters": {
            "scaling_divisor": 1.0
        }
    }

    graph_env = GraphJspEnv(**env_kwargs)

    graph_matrix_env = GraphMatrixEnv(
        jsp_instance=ft06,
        reward_function="makespan",
        ls_enabled=False
    )


    graph_matrix_env.render()

    state = graph_matrix_env.get_state()

    graph_matrix_env.greedy_rollout()
    graph_matrix_env.render()
    graph_matrix_env.load_state(state)

    graph_matrix_env.random_rollout()
    graph_matrix_env.render()

    print(f"after rollout: terminal={graph_matrix_env.is_terminal_state()}")

    # reload state
    graph_matrix_env.load_state(state)
    graph_matrix_env.render()

    print(f"after reload: terminal={graph_matrix_env.is_terminal_state()}")
