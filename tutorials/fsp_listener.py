import sys
sys.path.insert(1, '../')

import time
import mdml_client as mdml

exp = mdml.experiment("FSP", "Flame", "123FlameOn!!", "merfpoc.egs.anl.gov")
time.sleep(3)
try:
    def callback_func(client, userdata, message): # Only message is used here
        print(f'TOPIC: {message.topic}\nPAYLOAD: {message.payload.decode("utf-8")}')
    exp.listener(analysis_names = ["BAYES_OPTIM"], callback = callback_func)
except KeyboardInterrupt:
    print("Quitting...")
finally:
    exp.disconnect()
