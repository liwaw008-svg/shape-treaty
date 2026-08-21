import ast,pathlib
P=pathlib.Path(__file__).parents[1]/'contracts'/'contract.py';S=P.read_text(encoding='utf-8')
def gate():
 n=next(x for x in ast.parse(S).body if isinstance(x,ast.FunctionDef) and x.name=='treaty_gate');z={};exec(compile(ast.Module([n],[]),str(P),'exec'),z);return z['treaty_gate']
def test_surface():ast.parse(S);assert all(x in S for x in ('propose','ratify','get_treaty','run_nondet_unsafe'))
def test_fixed_conflict_is_never_waived():assert gate()(['minimum contrast'],[],True,True)=='IMPOSSIBLE'
def test_flexible_conflict_is_elastic():assert gate()([],['preferred spacing'],True,True)=='ELASTIC'
def test_clean_authenticated_candidate_ratifies():assert gate()([],[],True,True)=='RATIFIED'
def test_unavailable_artifact_fails_closed():assert gate()([],[],True,False)=='IMPOSSIBLE'
