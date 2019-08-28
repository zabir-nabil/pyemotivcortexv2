import asyncio
from lib.cortex import Cortex


async def do_stuff(cortex):
    # await cortex.inspectApi()
    #print("** USER LOGIN **")
    await cortex.get_user_login()
    #print("** GET CORTEX INFO **")
    await cortex.get_cortex_info()
    #print("** HAS ACCESS RIGHT **")
    await cortex.has_access_right()
    #print("** REQUEST ACCESS **")
    await cortex.request_access()
    #print("** AUTHORIZE **")
    await cortex.authorize()
    #print("** GET LICENSE INFO **")
    await cortex.get_license_info()
    #print("** QUERY HEADSETS **")
    await cortex.query_headsets()
    
    if len(cortex.headsets) > 0:
        #print("** CREATE SESSION **")
        await cortex.create_session(activate=True,
                                    headset_id=cortex.headsets[0])
        #print("** CREATE RECORD **")
        await cortex.create_record(title="test record 1")
        #print("** SUBSCRIBE POW & MET **")
        await cortex.subscribe(['fac', 'com'])
        while cortex.packet_count < 10:
            await cortex.get_data()
        await cortex.inject_marker(label='halfway', value=1,
                                   time=cortex.to_epoch())
        while cortex.packet_count < 20:
            await cortex.get_data()
        await cortex.close_session()

import time
def test():
    for i in range(10): # how many times I want to get data
        t1 = time.time()

        cortex = Cortex('./cortex_creds')
        asyncio.run(do_stuff(cortex))
        cortex.close()

        t2 = time.time()

        print(t2-t1)


if __name__ == '__main__':
    test()
