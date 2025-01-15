from jsp_instance_utils.instances import (ft06)

import gymnasium as gym
import sb3_contrib
import stable_baselines3 as sb3

import numpy as np
from sb3_contrib.common.maskable.policies import MaskableActorCriticPolicy
from sb3_contrib.common.wrappers import ActionMasker

from graph_matrix_jsp_env.disjunctive_jsp_env import DisjunctiveGraphJspEnv

if __name__ == '__main__':

    # You can also use other instances ft06, ft20, ta21, ta80
    # just make sure to import them from jsp_instance_utils.instances
    env = DisjunctiveGraphJspEnv(jsp_instance=ft06)
    env = sb3.common.monitor.Monitor(env)


    def mask_fn(env: gym.Env) -> np.ndarray:
        return env.unwrapped.valid_action_mask()


    env = ActionMasker(env, mask_fn)

    model = sb3_contrib.MaskablePPO(
        MaskableActorCriticPolicy,
        env,
        verbose=1,
        device="cpu" # Note: You can also use "cuda" if you have a GPU with CUDA
    )

    # Train the agent
    model.learn(total_timesteps=10_000)