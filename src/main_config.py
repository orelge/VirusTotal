URLS_CSV_FILE_PATH = r"C:\Users\אוראל\PycharmProjects\elementor_task\src\data\csv_files\urls.csv"
URLS_COLUMN = 'urls'
URL_COLUMN = 'url'
URL_CLASSIFICATION_COLUMN = 'url_classification'
INSERTION_TIME_COLUMN = 'insertion_time'
DB_NAME = 'virus-risk.db'
URLS_CLASSIFICATION_TABLE = 'urls_classification'
CATEGORIES_TABLE = 'categories'
VOTING_TABLE = 'voting'
GET_DATA_FROM_URLS_CLASSIFICATION_TABLE_QUERY = f'''SELECT *
FROM 'urls_classification'
'''
IS_TABLE_EXIST_QUERY = '''
SELECT * FROM sqlite_master where type='table';
'''

URLS_LIST = ['www.elementor.com',
             'www.textspeier.de',
             'www.facebook.com',
             'www.google.com',
             'www.wordpress.org',
             'raneevahijab.id',
             'boots.fotopyra.pl',
             'stackoverflow.com ',
             'www.family-partners.fr',
             'boots.fotopyra.pl']
TABLE_IS_NOT_IN_DB_ERROR_STRING = """Execution failed on sql 'SELECT *
FROM 'urls_classification'
': no such table: urls_classification"""

LOCAL_REPORT = {
    "data": {
        "attributes": {
            "last_modification_date": 1651081456,
            "last_http_response_cookies": {
                "__cf_bm": "k9ePMIlBUIIf7tfVYp0Lror2Z68uGY6ALCP2HcsyzgA-1651081099-0-AXcYI+B+2RhRIJDGfUDznR4a0+xqWRihPUKOlmb6/PclRgJYMJkmhhA9zDiBBPZzmvK9UQj30DX0XdwD30s1KIc=",
                "SameSite": "None"
            },
            "times_submitted": 278,
            "total_votes": {
                "harmless": 0,
                "malicious": 0
            },
            "threat_names": [],
            "redirection_chain": [
                "http://www.elementor.com/"
            ],
            "last_submission_date": 1651081072,
            "last_http_response_content_length": 293763,
            "last_http_response_headers": {
                "transfer-encoding": "chunked",
                "set-cookie": "__cf_bm=k9ePMIlBUIIf7tfVYp0Lror2Z68uGY6ALCP2HcsyzgA-1651081099-0-AXcYI+B+2RhRIJDGfUDznR4a0+xqWRihPUKOlmb6/PclRgJYMJkmhhA9zDiBBPZzmvK9UQj30DX0XdwD30s1KIc=; path=/; expires=Wed, 27-Apr-22 18:08:19 GMT; domain=.elementor.com; HttpOnly; Secure; SameSite=None",
                "cf-cache-status": "HIT",
                "expires": "Wed, 27 Apr 2022 18:08:19 GMT",
                "vary": "Accept-Encoding",
                "last-modified": "Mon, 25 Apr 2022 09:05:47 GMT",
                "link": "<https://elementor.com/wp-json/>; rel=\"https://api.w.org/\", <https://elementor.com/wp-json/wp/v2/pages/38>; rel=\"alternate\"; type=\"application/json\", <https://elementor.com/>; rel=shortlink",
                "date": "Wed, 27 Apr 2022 17:38:19 GMT",
                "cf-ray": "702954c669fe66e3-DFW",
                "expect-ct": "max-age=604800, report-uri=\"https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct\"",
                "x-xss-protection": "1; mode=block",
                "x-content-type-options": "nosniff",
                "content-encoding": "br",
                "age": "203552",
                "strict-transport-security": "max-age=10886400; includeSubDomains;",
                "server": "cloudflare",
                "connection": "keep-alive",
                "cache-control": "public, max-age=1800",
                "x-frame-options": "SAMEORIGIN, SAMEORIGIN",
                "content-type": "text/html; charset=UTF-8"
            },
            "reputation": 0,
            "tags": [],
            "last_analysis_date": 1651081072,
            "first_submission_date": 1465927749,
            "categories": {
                "Forcepoint ThreatSeeker": "information technology",
                "Sophos": "information technology",
                "BitDefender": "computersandsoftware"
            },
            "last_http_response_content_sha256": "61e620e5da2c80477ac54f357b3ab2c144e1ead4ad0f280b88ae9ae8aa24ae83",
            "last_http_response_code": 200,
            "last_final_url": "https://elementor.com/",
            "trackers": {
                "Google Tag Manager": [
                    {
                        "url": "//www.googletagmanager.com/ns.html?id=GTM-NJK8HW",
                        "timestamp": 1642290108,
                        "id": "GTM-NJK8HW"
                    }
                ],
                "New Relic": [
                    {
                        "url": "",
                        "timestamp": 1650103553
                    }
                ]
            },
            "url": "http://www.elementor.com/",
            "title": "Elementor: #1 Free WordPress Website Builder | Elementor.com",
            "last_analysis_stats": {
                "harmless": 82,
                "malicious": 0,
                "suspicious": 0,
                "undetected": 10,
                "timeout": 0
            },
            "last_analysis_results": {
                "CMC Threat Intelligence": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "CMC Threat Intelligence"
                },
                "Snort IP sample list": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Snort IP sample list"
                },
                "VX Vault": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "VX Vault"
                },
                "Armis": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Armis"
                },
                "ViriBack": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "ViriBack"
                },
                "Comodo Valkyrie Verdict": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Comodo Valkyrie Verdict"
                },
                "PhishLabs": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "PhishLabs"
                },
                "K7AntiVirus": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "K7AntiVirus"
                },
                "CINS Army": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "CINS Army"
                },
                "Cyren": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Cyren"
                },
                "Quttera": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Quttera"
                },
                "BlockList": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "BlockList"
                },
                "OpenPhish": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "OpenPhish"
                },
                "0xSI_f33d": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "0xSI_f33d"
                },
                "Feodo Tracker": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Feodo Tracker"
                },
                "Web Security Guard": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Web Security Guard"
                },
                "Scantitan": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Scantitan"
                },
                "AlienVault": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "AlienVault"
                },
                "Sophos": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Sophos"
                },
                "Phishtank": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Phishtank"
                },
                "EonScope": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "EonScope"
                },
                "Cyan": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "Cyan"
                },
                "Spam404": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Spam404"
                },
                "SecureBrain": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "SecureBrain"
                },
                "Hoplite Industries": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Hoplite Industries"
                },
                "CRDF": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "CRDF"
                },
                "Rising": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Rising"
                },
                "Fortinet": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Fortinet"
                },
                "alphaMountain.ai": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "alphaMountain.ai"
                },
                "Lionic": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Lionic"
                },
                "Virusdie External Site Scan": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Virusdie External Site Scan"
                },
                "Artists Against 419": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Artists Against 419"
                },
                "Google Safebrowsing": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Google Safebrowsing"
                },
                "SafeToOpen": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "SafeToOpen"
                },
                "ADMINUSLabs": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "ADMINUSLabs"
                },
                "CyberCrime": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "CyberCrime"
                },
                "Heimdal Security": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Heimdal Security"
                },
                "AutoShun": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "AutoShun"
                },
                "Trustwave": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "Trustwave"
                },
                "AICC (MONITORAPP)": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "AICC (MONITORAPP)"
                },
                "CyRadar": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "CyRadar"
                },
                "Dr.Web": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Dr.Web"
                },
                "Emsisoft": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Emsisoft"
                },
                "Abusix": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Abusix"
                },
                "Webroot": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Webroot"
                },
                "Avira": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Avira"
                },
                "securolytics": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "securolytics"
                },
                "Antiy-AVL": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Antiy-AVL"
                },
                "Acronis": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Acronis"
                },
                "Quick Heal": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Quick Heal"
                },
                "DNS8": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "DNS8"
                },
                "benkow.cc": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "benkow.cc"
                },
                "EmergingThreats": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "EmergingThreats"
                },
                "Chong Lua Dao": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Chong Lua Dao"
                },
                "Yandex Safebrowsing": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Yandex Safebrowsing"
                },
                "MalwareDomainList": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "MalwareDomainList"
                },
                "Lumu": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "Lumu"
                },
                "zvelo": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "zvelo"
                },
                "Kaspersky": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Kaspersky"
                },
                "Sucuri SiteCheck": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Sucuri SiteCheck"
                },
                "desenmascara.me": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "desenmascara.me"
                },
                "URLhaus": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "URLhaus"
                },
                "PREBYTES": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "PREBYTES"
                },
                "StopForumSpam": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "StopForumSpam"
                },
                "Blueliv": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Blueliv"
                },
                "Netcraft": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "Netcraft"
                },
                "ZeroCERT": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "ZeroCERT"
                },
                "Phishing Database": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Phishing Database"
                },
                "MalwarePatrol": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "MalwarePatrol"
                },
                "MalBeacon": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "MalBeacon"
                },
                "Sangfor": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Sangfor"
                },
                "IPsum": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "IPsum"
                },
                "Malwared": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Malwared"
                },
                "BitDefender": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "BitDefender"
                },
                "GreenSnow": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "GreenSnow"
                },
                "G-Data": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "G-Data"
                },
                "StopBadware": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "StopBadware"
                },
                "SCUMWARE.org": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "SCUMWARE.org"
                },
                "malwares.com URL checker": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "malwares.com URL checker"
                },
                "NotMining": {
                    "category": "undetected",
                    "result": "unrated",
                    "method": "blacklist",
                    "engine_name": "NotMining"
                },
                "Forcepoint ThreatSeeker": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Forcepoint ThreatSeeker"
                },
                "Certego": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Certego"
                },
                "ESET": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "ESET"
                },
                "Threatsourcing": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Threatsourcing"
                },
                "MalSilo": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "MalSilo"
                },
                "Nucleon": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Nucleon"
                },
                "BADWARE.INFO": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "BADWARE.INFO"
                },
                "ThreatHive": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "ThreatHive"
                },
                "FraudScore": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "FraudScore"
                },
                "Tencent": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Tencent"
                },
                "Bfore.Ai PreCrime": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Bfore.Ai PreCrime"
                },
                "Baidu-International": {
                    "category": "harmless",
                    "result": "clean",
                    "method": "blacklist",
                    "engine_name": "Baidu-International"
                }
            },
            "html_meta": {
                "twitter:creator": [
                    "@elemntor"
                ],
                "googlebot": [
                    "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"
                ],
                "twitter:image": [
                    "https://elementor.com/marketing/wp-content/uploads/2021/07/HP.png"
                ],
                "og:locale": [
                    "en_US"
                ],
                "robots": [
                    "max-image-preview:large",
                    "index, follow"
                ],
                "og:image:width": [
                    "1200"
                ],
                "msapplication-TileImage": [
                    "https://elementor.com/marketing/wp-content/uploads/2021/04/elementor-favicon-512.png"
                ],
                "twitter:site": [
                    "@elemntor"
                ],
                "article:publisher": [
                    "https://www.facebook.com/elemntor"
                ],
                "og:image": [
                    "https://elementor.com/marketing/wp-content/uploads/2021/07/HP.png"
                ],
                "viewport": [
                    "width=device-width, initial-scale=1"
                ],
                "og:image:height": [
                    "630"
                ],
                "og:url": [
                    "https://elementor.com/"
                ],
                "og:title": [
                    "Elementor: #1 Free WordPress Website Builder | Elementor.com"
                ],
                "og:site_name": [
                    "Elementor"
                ],
                "twitter:card": [
                    "summary_large_image"
                ],
                "description": [
                    "Elementor is the platform web creators choose to build professional WordPress websites, grow their skills, and build their business. Start for free today!"
                ],
                "og:type": [
                    "website"
                ],
                "og:description": [
                    "Elementor is the platform web creators choose to build professional WordPress websites, grow their skills, and build their business. Start for free today!"
                ],
                "bingbot": [
                    "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"
                ],
                "article:modified_time": [
                    "2022-04-19T07:40:55+00:00"
                ]
            },
            "outgoing_links": [
                "https://elementor.careers/explore/",
                "https://www.producthunt.com/posts/elementor",
                "https://www.instagram.com/elementor/",
                "https://wordpress.org/plugins/elementor/",
                "https://www.facebook.com/elemntor/",
                "https://twitter.com/elemntor",
                "https://www.youtube.com/channel/UCt9kG_EDX8zwGSC1-ycJJVA?sub_confirmation=1",
                "https://www.facebook.com/groups/916625091796611",
                "http://www.pinterest.com/elemntor",
                "https://github.com/pojome/elementor"
            ]
        },
        "type": "url",
        "id": "5fb9634584e7079213e638de0891935c1602368760d06233dc4f6ffa2549a4f4",
        "links": {
            "self": "https://www.virustotal.com/api/v3/urls/5fb9634584e7079213e638de0891935c1602368760d06233dc4f6ffa2549a4f4"
        }
    }
}
