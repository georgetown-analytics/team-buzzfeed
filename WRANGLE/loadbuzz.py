import datetime

class CleanRec(object):

    def __init__(self):
        # MAKE THESE TIMESTAMP
        self.pull_ts = ""           # Keep the latest

        self.id = 0                 # RECORD IDENTIFIER - PRIMARY
        self.impressions = 0        # Keep the Max
        self.cat_id = 0             # FEATURE
        self.freq = 0               # NEW

        self.min_impres = 10000000000
        self.max_impres = 0

        self.pull_cc = "None"       # RECORD IDENTIFIER - SECONDARY
        self.cc = "None"            # RECORD IDENTIFIER - SECONDARY (COUNTRY OF ORIGIN)
        self.descr = "None"         # FEATURE
        self.cat = "None"           # FEATURE
        self.title = "None"         # FEATURE
        self.metav = "None"         # FEATURE
        self.trending = "None"
        self.primary_kw = "None"
        self.tags = "None"          # FEATURE


    def clean_buzz(self, br):
        self.pull_ts = str(br[1])
        self.id = int(br[9])
        self.impressions = br[7]
        self.cat_id = int(br[12])
        self.freq = 1

        self.pull_cc = br[0]
        self.cc = br[6]
        self.descr = br[10]
        self.cat = br[11]
        self.title = br[14]
        self.metav = br[16]
        self.tags = br[17]

        self.trending = ""
        self.primary_kw = ""
        taglist=self.tags.split("*")        # Parse tags back to a list
        self.tags = ""

        for atag in taglist:                # Pull out trending and primary kw
            if atag.find("--trending") >= 0:
                self.trending = atag
                self.trending = self.trending.replace("--", "")
            elif atag.find("--primarykeyword") >= 0:
                self.primary_kw += atag # APPEND INSTEAD OF REMOVE
                self.primary_kw = self.primary_kw.replace("--primarykeyword-", "")

            else:
                True

        taglist[:] = [x for x in taglist if x.find("--") < 0]  # Remove all special tags
        self.tags = " ".join(taglist)


    def get_id(self):
        return self.id
    def get_country(self):
        return self.pull_cc
    def get_impressions(self):
        return self.impressions
    def get_pull_ts(self):
        return self.pull_ts
    def init_impressions_clean(self):
        self.min_impres = self.impressions
        self.max_impres = self.impressions
    def cure_impressions_clean(self):
        self.impressions = self.max_impres - self.min_impres + 1



    def print_clean(self):
        # ADD RECORD TO DATABASE
        # ORDER: id, pull_cc, freq, pull_ts, cc, impressions, descr, cat, cat_id, title, metav, tags
        buzzrec = ""
        buzzrec += str(self.id)
        buzzrec += "|"
        buzzrec += self.pull_cc
        buzzrec += "|"
        buzzrec += str(self.freq)
        buzzrec += "|"
        buzzrec += self.pull_ts
        buzzrec += "|"
        buzzrec += self.cc
        buzzrec += "|"
        buzzrec += str(self.impressions)
        buzzrec += "|"
        buzzrec += str(self.min_impres)
        buzzrec += "|"
        buzzrec += str(self.max_impres)
        buzzrec += "|"
        buzzrec += self.descr
        buzzrec += "|"
        buzzrec += self.cat
        buzzrec += "|"
        buzzrec += str(self.cat_id)
        buzzrec += "|"
        buzzrec += self.title
        buzzrec += "|"
        buzzrec += self.metav
        buzzrec += "|"
        buzzrec += self.trending
        buzzrec += "|"
        buzzrec += self.primary_kw
        buzzrec += "|"
        buzzrec += self.tags
        print buzzrec

    def get_in_list(self):
        # ORDER: id, pull_cc, freq, pull_ts, cc, impressions, descr, cat, cat_id, title, metav, trending, primary_kw, tags
        formlist = []
        formlist.append(self.id)
        formlist.append(self.pull_cc)
        formlist.append(self.freq)
        formlist.append(self.pull_ts)
        formlist.append(self.cc)
        formlist.append(self.impressions)
        formlist.append(self.min_impres)
        formlist.append(self.max_impres)
        formlist.append(self.descr)
        formlist.append(self.cat)
        formlist.append(self.cat_id)
        formlist.append(self.title)
        formlist.append(self.metav)
        formlist.append(self.trending)
        formlist.append(self.primary_kw)
        formlist.append(self.tags)
        return formlist


    def __del__(self):
        del self

if __name__ == '__main__':
    keylist = BuzzRec()
