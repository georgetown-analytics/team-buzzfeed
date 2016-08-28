
import datetime
import os
import glob
import psycopg2

from pprint import pprint
from loadbuzz import CleanRec




def main():
    conn = psycopg2.connect("dbname=buzzdb user=postgres")
    cur = conn.cursor()
    clean_cur = conn.cursor()
    cur.execute("SELECT * FROM buzzrow;") # ACCESS ALL BUZZ RECORDS
    count = 0
    k = CleanRec()

    # SAVE UNIQUE RECORDS (IN CLEANBUZZ) BY ID AND COUNTRY--ELIMINATE DUPLICATIONS, COUNT FREQUENCY & CLEAN IMPRESSIONS
    for buzzrow in cur:
        k.clean_buzz(buzzrow)
        # FIND MATCHING RECORD IN CLEANBUZZ
        clean_cur.execute("SELECT * FROM cleanbuzz WHERE id=%s AND pull_cc=%s", (k.get_id(), k.get_country()))
        clean_rec = clean_cur.fetchone()
        if clean_rec is None:
            # NEW BUZZ: INITIALIZE IMPRESSIONS
            k.init_impressions_clean()
            k.cure_impressions_clean()
            rec_list=k.get_in_list()        # Prepare record to add to DATABASE
            # ORDER: id, pull_cc, freq, pull_ts, cc, impressions, min_impres, max_impres, descr, cat, cat_id, title, metav, tags
            clean_cur.execute("INSERT INTO cleanbuzz (id, pull_cc, freq, pull_ts, cc, impressions, min_impres, max_impres, descr, cat, cat_id, title, metav, trending, primary_kw, tags) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", rec_list)
            conn.commit()
        else:
            # BUZZ EXISTS IN CLEANBUZZ: UPDATE FREQ, IMPRESSIONS & KEEP OLDEST TIMESTAMP
            # ORDER: id, pull_cc, freq, pull_ts, cc, impressions, descr, cat, cat_id, title, metav, tags
            new_freq = clean_rec[2] + 1     # Increment frequency
            min_impres = min(clean_rec[6], k.get_impressions())    # Reset Minimum impression in cleanbuzz
            max_impres = max(clean_rec[7], k.get_impressions())    # Reset Minimum impression in cleanbuzz
            new_impressions = max_impres - min_impres + 1          # Get latest impression count
            curr_ts = k.get_pull_ts()
            if curr_ts>str(clean_rec[3]): curr_ts=str(clean_rec[3]) # Keep the oldest date
            clean_cur.execute("UPDATE cleanbuzz SET freq=%s, impressions=%s, min_impres=%s, max_impres=%s, pull_ts=%s WHERE id=%s AND pull_cc=%s", \
                (new_freq, new_impressions, min_impres, max_impres, curr_ts, k.get_id(), k.get_country()))
            conn.commit()
        #if count == 100:  exit()
        #else:  count += 1

if __name__ == "__main__":
    main()
