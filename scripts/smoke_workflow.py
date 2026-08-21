import json,os,re,time
from genlayer_py import create_client,create_account
from genlayer_py.chains import testnet_bradbury
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));W=os.path.abspath(os.path.join(R,'..','..','..','..'))
def v(n):return re.search(rf'^\s*{n}\s*=\s*"?([^"\r\n]+)',open(os.path.join(W,'accounts.env'),encoding='utf-8').read(),re.M).group(1).strip()
def s(fn):
 for p in (0,3,7,12):
  if p:time.sleep(p)
  try:return fn()
  except Exception as e:last=e
 raise last
 a=create_account(account_private_key=v('ACCOUNT_4_GENLAYER_PRIVATE_KEY'));cl=create_client(chain=testnet_bradbury,account=a);addr=json.load(open(os.path.join(R,'treaty-vector.json')))['vector']['contract'];i='ST-'+str(int(time.time()));h=s(lambda:cl.write_contract(address=addr,function_name='propose',args=[i,'1200x800 collaborative poster',['logo exclusion radius 80','headline baseline 220'],['caption may orbit','accent may rotate'],'https://www.w3.org/TR/SVG2/']));print('proposeTx',h,flush=True);cl.wait_for_transaction_receipt(transaction_hash=h,status='ACCEPTED',retries=80,interval=20000);g=s(lambda:cl.write_contract(address=addr,function_name='ratify',args=[i,['caption orbit overlaps safe zone']]));print('ratifyTx',g,flush=True);cl.wait_for_transaction_receipt(transaction_hash=g,status='ACCEPTED',retries=80,interval=20000);assert all(cl.get_transaction(transaction_hash=x).get('tx_execution_result_name')=='FINISHED_WITH_RETURN' for x in (h,g))
