import requests as re
import json

# # mainnet
# EL_RPC = "https://ethereum-rpc.publicnode.com"
# CL_API = "https://ethereum-beacon-api.publicnode.com"


# # testnet
EL_RPC = "https://ethereum-sepolia-rpc.publicnode.com"
CL_API = "https://ethereum-sepolia-beacon-api.publicnode.com"


def get_blobsidecar(block_id):
    data = re.get(f"{CL_API}/eth/v1/beacon/blob_sidecars/{block_id}").json()
    with open(f'./blob_sidecars_{block_id}.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


# data = re.get(f"{CL_API}//eth/v1/beacon/headers").json()
# with open(f'./temp.json', 'w') as json_file:
#     json.dump(data, json_file, indent=2)


get_blobsidecar(4545038)
