

def test_random_rollout_custom_instance(env):
    env.reset()
    makespan = env.random_rollout()

    assert env.is_terminal_state()
    # 40 is the optimal makespan for the custom instance
    assert makespan >= 40