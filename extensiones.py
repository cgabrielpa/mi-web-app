from supabase import create_client

def inicializar_db():

    cliente = create_client('https://vzeunudtaurpdhzdwfvf.supabase.co', supabase_key= 'sb_publishable_H54TF_3rMX0dkmzm3e5NBw_Bb_peoYP')

    return cliente