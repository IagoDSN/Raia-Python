import logging
import logging.config
import queue
import threading
import concurrent.futures

USE_CAMERA = False  # Mude para True se quiser ativar o uso real da câmera (com OpenCV)

if USE_CAMERA:
    from services.camera_services import (FaceDB, PresenceDetector, RecordFace, Wakeface)
else:
    # Mock das classes da câmera
    class FaceDB:
        @staticmethod
        def load():
            print("Mock: FaceDB loaded")

    class Wakeface:
        def __init__(self, handler): pass
        def start(self): print("Mock: Wakeface start")
        def stop(self): print("Mock: Wakeface stop")

    class RecordFace:
        def __init__(self, handler): pass
        def start(self, username): print(f"Mock: RecordFace start ({username})")
        def stop(self): print("Mock: RecordFace stop")

    class PresenceDetector:
        def __init__(self, handler): pass
        def start(self): print("Mock: PresenceDetector start")
        def stop(self): print("Mock: PresenceDetector stop")

from services.cloud import server
from services.eyes.service import Eyes
from services.leds import ArrayLed, LedState
from services.mic import Recorder
from services.proactive_service import ProactiveService
from services.speaker import Speaker
from services.touchscreen import TouchScreen

logging.config.fileConfig('files/logging.conf')
logger = logging.getLogger('Main')
logger.setLevel(logging.DEBUG)

robot_context = {
    'state': 'idle',
    'username': None,
    'continue_conversation': False,
    'proactive_question': '',
    'unknown_user_interactions': 0
}

notifications = queue.Queue()
listen_timer = None
DELAY_TIMEOUT = 5
global_executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
SERVER_QUERY_TIMEOUT = 15

with open('files/connection_error.wav', 'rb') as f:
    connection_error_audio = f.read()

# [AQUI CONTINUA SEU CÓDIGO COMPLETO SEM MODIFICAÇÃO]
# As funções: wf_event_handler, rf_event_handler, etc...
# Toda a lógica permanece igual até o bloco principal abaixo

if __name__ == '__main__':
    leds = ArrayLed()
    eyes = Eyes(sc_width=600, sc_height=1024)
    FaceDB.load()  # carregar embeddings de rostos (ou mock)

    wf = Wakeface(wf_event_handler)
    rf = RecordFace(rf_event_handler)
    pd = PresenceDetector(pd_event_handler)

    proactive = ProactiveService(proactive_service_event_handler)

    speaker = Speaker(speaker_event_handler)
    mic = Recorder(mic_event_handler)
    touch = TouchScreen(touchscreen_event_handler)

    touch.start()
    if pd:
        pd.start()

    logger.info('Ready')
    try:
        while True:
            notification = notifications.get()

            if notification.get('transition') == 'shutdown':
                break

            process_transition(**notification)

    except KeyboardInterrupt:
        pass

    finally:
        logger.info("Interruption detected. Stopping and shutting down the robot...")

        with open('files/powerdown_sound.wav', 'rb') as f:
            powerdown_audio = f.read()

        speaker.start(powerdown_audio)

        touch.stop()

        server.dump_conversation_db(robot_context['username'])

        eyes.set('neutral_closed')

        global_executor.shutdown(wait=False)

        if wf:
            wf.stop()
        if rf:
            rf.stop()
        if pd:
            pd.stop()
        mic.destroy()
        speaker.destroy()
        leds.stop()
        eyes.stop()

        logger.info('Stopped')
