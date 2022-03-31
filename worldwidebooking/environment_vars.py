import os
import logging


def read_env_file_override(proj_root):
    """
    Overwrite USE_ENV_FILE if there is a local file on the project root.
    It is expected that USE_ENV_FILE content is a single line with the full filename to a custom .env file

    :param proj_root: the project root or where the USE_ENV_FILE file is located
    :return: None
    """
    # noinspection PyBroadException
    try:
        with open(os.path.join(proj_root, 'USE_ENV_FILE'), 'rt') as f:
            line = f.readline().strip()
        if line:
            logging.error(f'Using USE_ENV_FILE="{line}" from file')
            os.environ['USE_ENV_FILE'] = line

    except Exception:
        pass


def import_env():
    use_env_file = os.environ.get('USE_ENV_FILE')

    parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    is_production = parent_dir.endswith('-prod')
    is_qa = parent_dir.endswith('-qa')

    if is_production:
        default_env_filepath = '/etc/regional_api/api-prod.env'
    elif is_qa:
        default_env_filepath = '/etc/regional_api/api-qa.env'
    else:
        default_env_filepath = '/etc/regional_api/api.env'

    try:
        env_filename = use_env_file or default_env_filepath
        with open(env_filename, 'rt') as f:
            for line in f:
                line = line.strip()
                if len(line) == 0 or line.startswith('#'):
                    continue

                parts = line.split('=', 1)
                if len(parts) > 0:
                    var_name = parts[0].strip()
                    var_value = parts[1].strip() if len(parts) >= 2 else ''
                    os.environ[var_name] = var_value

    except Exception as e:
        logging.error(f'Could not parse the environment variables. The exception is: {e}')
