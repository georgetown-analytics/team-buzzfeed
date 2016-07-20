class BuzzRec(object):
    
    def __init__(self):
        # MAKE THESE TIMESTAMP
        self.pull_ts = ""
        self.pub_ts = ""

        self.id = 0
        self.impressions = 0
        self.cat_id = 0
        self.u_id = 0

        self.pull_cc = ""
        self.last_upd = ""
        self.pub = ""
        self.cc = ""
        self.lang = ""
        self.descr = ""
        self.cat = ""
        self.u_name = ""
        self.title = ""
        self.status = ""
        self.metav = ""
        self.tags = ""
        self.comment_stat = ""



    # REMOVE ALL NON ASCII
    def remove_non_ascii(self, text):
        return ''.join([i if ord(i) < 128 else ' ' for i in text])

    # REPLACE ALL NON ASCII WITH SPACE
    def replace_non_ascii_with_space(self,text):
        return re.sub(r'[^\x00-\x7F]+',' ', text)

    def add_pull_cc(self, cc):
        self.pull_cc = cc

    def add_pull_ts(self, ts):
        self.pull_ts = ts

    def add_buzz(self, dl):
        for key, value in dl.iteritems():
            if key == 'username':
                self.u_name = str(value)
            elif key == 'last_updated':
                self.last_upd = str(value)
            elif key == 'published':
                self.pub = str(value)
            elif key == 'published_date':
                self.pub_ts = str(value)
            elif key == 'country_code':
                self.cc = str(value)
            elif key == 'impressions':
                if value is None:
                    True
                else:
                    self.impressions = int(value)
            elif key == 'language':
                self.lang = str(value)
            elif key == 'id':
                self.id = int(value)
            elif key == 'description':
                self.descr = ''.join([i if ord(i) < 128 else ' ' for i in value])
            elif key == 'category':
                self.cat = str(value)
            elif key == 'category_id':
                self.cat_id = int(value)
            elif key == 'user_id':
                self.u_id = int(value)
            elif key == 'title':
                self.title = ''.join([i if ord(i) < 128 else ' ' for i in value])
            elif key == 'status':
                self.status = str(value)
            elif key == 'metavertical':
                self.metav = str(value)
            elif key == 'tags':
                self.tags = "*".join(value)
                self.tags = ''.join([i if ord(i) < 128 else ' ' for i in self.tags])
            elif key == 'comment_stats':
                self.comment_stat = str(value)
            else:
                True

    def load_buzz(self):
        print ">>>>>>>>>>>>>>>>>>>>> writing to database <<<<<<<<<<<<<<<<<<"

    def display_buzz(self):
        # ADD RECORD TO DATABASE
        buzzrec = ""
        buzzrec += self.pull_cc
        buzzrec += "|"
        buzzrec += self.pull_ts
        buzzrec += "|"
        buzzrec += self.u_name
        buzzrec += "|"
        buzzrec += self.last_upd
        buzzrec += "|"
        buzzrec += self.pub
        buzzrec += "|"
        buzzrec += self.pub_ts
        buzzrec += "|"
        buzzrec += self.cc
        buzzrec += "|"
        buzzrec += str(self.impressions)
        buzzrec += "|"
        buzzrec += self.lang
        buzzrec += "|"
        buzzrec += str(self.id)
        buzzrec += "|"
        buzzrec += self.descr
        buzzrec += "|"
        buzzrec += self.cat
        buzzrec += "|"
        buzzrec += str(self.cat_id)
        buzzrec += "|"
        buzzrec += str(self.u_id)
        buzzrec += "|"
        buzzrec += self.title
        buzzrec += "|"
        buzzrec += self.status
        buzzrec += "|"
        buzzrec += self.metav
        buzzrec += "|"
        buzzrec += self.tags
        buzzrec += "|"
        buzzrec += self.comment_stat
        print buzzrec

    def __del__(self):
        del self

if __name__ == '__main__':
    keylist = BuzzRec()
