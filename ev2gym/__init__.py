from dotenv import load_dotenv
from gymnasium.envs.registration import register

load_dotenv()

register(
    id='EV2Gym-v1',
    entry_point='ev2gym.models.ev2gym_env:EV2Gym',
    kwargs={'config_file': 'ev2gym/example_config_files/V2GProfitMax.yaml'}
)