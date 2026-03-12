import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import psycopg2
import streamlit as st

#Veritabanı Bağlantı Komutları

st.cache_data
def data_ready():
    conn = None

    try: 
        database_name = "steam_dataset"
        user_name = "postgres"
        password = "Bawer2265"
        host_ip ="127.0.0.1" #localhost
        host_port = "5432"

        conn = psycopg2.connect(database =database_name,
                    user = user_name,
                    password = password,
                    host = host_ip,
                    port = host_port)
    
        cur = conn.cursor() #cursor bağlantısı
    
        cur.execute("SELECT * FROM application;")
        app_data = cur.fetchall()
        app_column = [desc[0] for desc in cur.description]

        cur.execute("SELECT * FROM reviews;")
        rev_data = cur.fetchall()
        rev_column = [desc[0] for desc in cur.description]

        cur.execute("SELECT * FROM genres;")
        gen_data = cur.fetchall()
        gen_column = [desc[0] for desc in cur.description]

        cur.execute("SELECT * FROM appgenres;")
        app_gen = cur.fetchall()
        appgen_column = [desc[0] for desc in cur.description]    
    
    
        print("Veritabanına başaralı bir şekilde bağlandı")
    
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")

    finally:
        if conn:
            conn.close()
            print("Veritabanına başaralı bir şekilde kapatıldı.")

    pd.set_option('display.max_columns', None) #sütunları net görmek için


#DataFrame Dosyaları
    df_app = pd.DataFrame(app_data, columns=app_column)
    df_rev = pd.DataFrame(rev_data, columns=rev_column)
    df_gen = pd.DataFrame(gen_data, columns=gen_column)
    df_appgen = pd.DataFrame(app_gen, columns=appgen_column)

#application tablosundaki hatalı veri tipleri düzenlendi
    df_app['release_date'] = pd.to_datetime(df_app['release_date'], errors='coerce')
    df_app['updated_at'] = pd.to_datetime(df_app['updated_at'], errors='coerce')
    df_app['created_at'] = pd.to_datetime(df_app['created_at'], errors='coerce')
    df_app['required_age'] = pd.to_numeric(df_app['required_age'], errors='coerce')
    df_app['metacritic_score'] = pd.to_numeric(df_app['metacritic_score'], errors='coerce')
    df_app['recommendations_total'] = pd.to_numeric(df_app['recommendations_total'], errors='coerce')
    df_app['mat_initial_price'] = pd.to_numeric(df_app['mat_initial_price'], errors='coerce')
    df_app['mat_final_price'] = pd.to_numeric(df_app['mat_final_price'], errors='coerce')
    df_app['mat_discount_percent'] = pd.to_numeric(df_app['mat_discount_percent'], errors='coerce')
    df_app['mat_achievement_count'] = pd.to_numeric(df_app['mat_achievement_count'], errors='coerce')

#reviews tablosundaki hatalı veri tipleri düzenlendi
    df_rev['updated_at'] = pd.to_datetime(df_rev['updated_at'], errors='coerce')
    df_rev['created_at'] = pd.to_datetime(df_rev['created_at'], errors='coerce')
    df_rev['author_playtime_forever'] = pd.to_numeric(df_rev['author_playtime_forever'], errors='coerce')
    df_rev['author_playtime_last_two_weeks'] = pd.to_numeric(df_rev['author_playtime_last_two_weeks'], errors='coerce')
    df_rev['author_playtime_at_review'] = pd.to_numeric(df_rev['author_playtime_at_review'], errors='coerce')
    df_rev['author_last_played'] = pd.to_numeric(df_rev['author_last_played'], errors='coerce')
    df_rev['weighted_vote_score'] = pd.to_numeric(df_rev['weighted_vote_score'], errors='coerce')
    df_rev['timestamp_created'] = pd.to_datetime(df_rev['timestamp_created'], unit='s', errors='coerce')
    df_rev['timestamp_updated'] = pd.to_datetime(df_rev['timestamp_updated'], unit='s', errors='coerce')

    return df_app,df_rev,df_gen,df_appgen