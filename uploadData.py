# local emulator can be installed here
# https://learn.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21
# code originally from
# from: https://github.com/Azure-Samples/azure-cosmos-db-python-getting-started
import pandas as pd
from azure.cosmos.aio import CosmosClient as cosmos_client
from azure.cosmos import PartitionKey, exceptions
import asyncio
import env

# <create_database_if_not_exists>
async def get_or_create_db(client, database_name):
    try:
        database_obj  = client.get_database_client(database_name)
        await database_obj.read()
        return database_obj
    except exceptions.CosmosResourceNotFoundError:
        print("Creating database")
        return await client.create_database(database_name)
# </create_database_if_not_exists>
    
# Create a container
# Using a good partition key improves the performance of database operations.
# <create_container_if_not_exists>
async def get_or_create_container(database_obj, container_name):
    try:        
        todo_items_container = database_obj.get_container_client(container_name)
        await todo_items_container.read()   
        return todo_items_container
    except exceptions.CosmosResourceNotFoundError:
        print("Creating container with id as partition key")
        return await database_obj.create_container(
            id=container_name,
            partition_key=PartitionKey(path="/id"))
    except exceptions.CosmosHttpResponseError:
        raise
# </create_container_if_not_exists>
    
# <method_populate_container_items>
async def populate_container_items(container_obj, items_to_create):
    # <create_item>
    for item in items_to_create:
        await container_obj.create_item(body=item)
    # </create_item>
# </method_populate_container_items>

# <run_sample>
async def run_sample(database_name, container_name, getDataFunction, saveLocal = True):
    if saveLocal:
        endpoint = env.vars['localEndpoint']
        key = env.vars['localKey']
    else:
        endpoint = env.vars['productionEndpoint']
        key =  env.vars['productionKey']

    # <create_cosmos_client>
    async with cosmos_client(endpoint, credential = key) as client:
    # </create_cosmos_client>
        try:
            # create a database
            database_obj = await get_or_create_db(client, database_name)
            # create a container
            container_obj = await get_or_create_container(database_obj, container_name)

            data = getDataFunction()
            # populate the family items in container
            await populate_container_items(container_obj, data)    

        except exceptions.CosmosHttpResponseError as e:
            print('\nrun_sample has caught an error. {0}'.format(e.message))
        finally:
            print("\nQuickstart complete")
# </run_sample>

def getEarthquakeData():
    df = pd.read_csv('data/earthquakes.csv')
    data = []
    # for data formatting checkout 
    # https://en.wikipedia.org/wiki/GeoJSON
    for i in range(df.shape[0]):
        item = {
            "id": str(i), 
            "type": 'Feature', 
            "geometry": { 
                            "type" : "Point", 
                            "coordinates": [ str(df.loc[i,"Longitude"]), str(df.loc[i,"Latitude"])]
                        },
            "properties": {
                            "date" : str(df.loc[i,"Date"]), 
                            "time" : str(df.loc[i,"Time"]), 
                            "type" : str(df.loc[i,"Type"]),
                            "depth" : str(df.loc[i,"Depth"]),
                            "magnitude" : str(df.loc[i,"Magnitude"])
                        }
            }
        data.append(item)
    return data


def getLocations():
    df = pd.read_csv('data/locations.csv')
    data = []
    for i in range(df.shape[0]):
        item = {
            "id": str(i),
            "name": str(df.loc[i,"Name"]),
            "type": "country",
            "coordinates": [ str(df.loc[i,"Longitude"]), str(df.loc[i,"Latitude"])]
        }
        data.append(item)
    return data

# <python_main>
if __name__=="__main__":
    loop = asyncio.get_event_loop()
    #loop.run_until_complete(run_sample('mapContent', 'earthquakes', getEarthquakeData, False))
    #loop.run_until_complete(run_sample('mapContent', 'locations', getLocations, False))
    print()

