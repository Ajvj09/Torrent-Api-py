from torrents.bitsearch import Bitsearch
from torrents.glodls import Glodls
from torrents.kickass import Kickass
from torrents.libgen import Libgen
from torrents.limetorrents import Limetorrent
from torrents.magnet_dl import Magnetdl
from torrents.nyaa_si import NyaaSi
from torrents.pirate_bay import PirateBay
from torrents.torlock import Torlock
from torrents.torrent_galaxy import TorrentGalaxy
from torrents.torrentfunk import TorrentFunk
from torrents.torrentProject import TorrentProject
from torrents.x1337 import x1337
from torrents.your_bittorrent import YourBittorrent
from torrents.yts import Yts
from torrents.zooqle import Zooqle


def check_if_site_available(site):
    all_sites = {
        "1337x": {
            "website": x1337,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": True,
            "recent_available": True,
            "recent_category_available": True,
            "categories": [
                "anime",
                "music",
                "games",
                "tv",
                "apps",
                "documentaries",
                "other",
                "xxx",
                "movies",
            ],
            "limit": 100,
        },
        "torlock": {
            "website": Torlock,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": [
                "anime",
                "music",
                "games",
                "tv",
                "apps",
                "documentaries",
                "other",
                "xxx",
                "movies",
                "books",
                "images",
            ],  # ebooks
            "limit": 100,
        },
        "zooqle": {
            "website": Zooqle,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": [],
            "limit": 100,
        },
        "magnetdl": {
            "website": Magnetdl,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            # e-books
            "categories": ["apps", "movies", "music", "games", "tv", "books"],
            "limit": 100,
        },
        "tgx": {
            "website": TorrentGalaxy,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": [
                "anime",
                "music",
                "games",
                "tv",
                "apps",
                "documentaries",
                "other",
                "xxx",
                "movies",
                "books",
            ],
            "limit": 100,
        },
        "nyaasi": {
            "website": NyaaSi,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": [],
            "limit": 100,
        },
        "piratebay": {
            "website": PirateBay,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["tv"],
            "limit": 100,
        },
        "bitsearch": {
            "website": Bitsearch,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": [],
            "limit": 100,
        },
        "kickass": {
            "website": Kickass,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": [
                "anime",
                "music",
                "games",
                "tv",
                "apps",
                "documentaries",
                "other",
                "xxx",
                "movies",
                "books",
            ],  # television applications
            "limit": 100,
        },
        "libgen": {
            "website": Libgen,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": [],
            "limit": 100,
        },
        "yts": {
            "website": Yts,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": [],
            "limit": 100,
        },
        "limetorrent": {
            "website": Limetorrent,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": [
                "anime",
                "music",
                "games",
                "tv",
                "apps",
                "other",
                "movies",
                "books",
            ],  # applications and tv-shows
            "limit": 100,
        },
        "torrentfunk": {
            "website": TorrentFunk,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": [
                "anime",
                "music",
                "games",
                "tv",
                "apps",
                "xxx",
                "movies",
                "books",
            ],  # television # software #adult # ebooks
            "limit": 100,
        },
        "glodls": {
            "website": Glodls,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": [],
            "limit": 100,
        },
        "torrentproject": {
            "website": TorrentProject,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": [],
            "limit": 100,
        },
        "ybt": {
            "website": YourBittorrent,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": [
                "anime",
                "music",
                "games",
                "tv",
                "apps",
                "xxx",
                "movies",
                "books",
                "pictures",
                "other",
            ],  # book -> ebooks
            "limit": 100,
        },
    }

    if site in all_sites.keys():
        return all_sites
    return False
