from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import EndpointConfig
from rasa.core.run import serve_application
from rasa.nlu.model import Interpreter


def run_recruitment_bot():
    '''
    Initialize bot for chat.
    :return: agent
    '''

    interpreter = Interpreter.load('models/20200911-131705/nlu') ## this should be an extracted model
    result = interpreter.parse('hello world', only_output_properties=False)
    embeds = result.get("text_sparse_features")
    print('Embeddings :', embeds)


if __name__ == '__main__':
    run_recruitment_bot()