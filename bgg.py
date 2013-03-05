import requests
import xmltodict

class Plays(object):
    def __add_plays(self, plays, xml):
        if xml['plays'].has_key('play'):
            for play in xml['plays']['play']:
                oid = play['item']['@objectid']
                if plays.has_key(oid):
                    plays[oid]['quantity'] += float(play['@quantity'])
                else:
                    plays[oid] = dict(
                            quantity=float(play['@quantity']),
                            name=play['item']['@name']
                    )
        return plays
    def plays(self, user, from_date, to_date):
        page = 0
        total = 1
        ret = {}
        while(page * 100 < total):
            url = ("http://www.boardgamegeek.com/xmlapi2/plays?"
                    "username={0}"
                    "&mindate={1}"
                    "&maxdate={2}"
                    "&page={3}"
                    "&type=thing"
                    ).format(user, from_date, to_date, page+1)
                    
            r = requests.get(url)
            if r.status_code != requests.codes.ok:
                r.raise_for_status()
            d = xmltodict.parse(r.text)
            ret = self.__add_plays(ret, d)
            page += 1
            total = int(d['plays']['@total'])
        return ret
