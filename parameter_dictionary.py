import re

class ConfigParameters:
    """
      A class to encapsulate configuration parameters used in the application. 
      This allows for easy and flexible access to various settings using subscription notation.
      """
    def __init__(self):
        self.parameters = {
            
            'CSV_URL':'freelance_accounts.csv',
            'columns_to_drop': ['description', 'rating'],
            'columns_to_swap': ['account_name', 'orders_done', 'account_condition', 'account_rating', 'take_or_bid', 'account_price']
            ,
            'columns_to_rename': {
                "Header": "description", 
                "Type": "condition", 
                "Rating": "rating", 
                "Price": "price"
            },
            'columns_to_rename_2':{
                'account_name': 'name',
                'orders_done': 'orders_done',
                'account_condition': 'condition',
                'account_rating': 'rating',
                'take_or_bid': 'bid/take',
                'account_price': 'price'
            },
            'account_name_patterns': {
                'Edusson': (r'\bedd?us?s?on\b|Edussion', re.I),
                'Studypool': (r'study\s*?pool|SP|pool|Top\s*?tutor', re.I),
                'Writerbay': (r'iter?s?bay|regular\s*?plus|Writer Bay', re.I),
                'Writezillas': (r'write\s*r?zill?as?', re.I),
                'Echolabs': (r'ech?o\s*?labs?', re.I),
                'Texting Factory': (r'factory', re.I),
                'CoudWorkers': (r'cloud\s*?workers?', re.I),
                'Writedom': (r'dom', re.I),
                'Fiverr': (r'\bfiv+er+\b', re.I),
                'Nerdy Turtlez': (r'nerdy', re.I),
                'Writing Creek': (r'\bcre+k\b|\bwriting\s*cre+k\b', re.I),
                'Academia Research': (r'academia\s*?res.|academia|Top premium acad|Senior Advanced', re.I),
                'Writerslabs': (r'iters*?\s*?labs*?', re.I),
                'Essaypro': (r'es+ay\s*?pro|writers*?\s*?pro|Essapro', re.I),
                'Atlantic Writers': (r'atlantic\s*?writers*?', re.I),
                'Simpletense': (r'simple\s*?ten', re.I),
                'Studybay': (r'study\s*?bay|sage', re.I), 
                'TSM Group': (r'\btsm\b', re.I), 
                'Crown Content': (r'crowd\s*?cont', re.I),
                'Crowdsurf': (r'surf', re.I),
                'Remotask': (r'remotas|gen\s*?ai|outl.', re.I), 
                'Writershub': (r'hub|shub', re.I),
                'Scribie': (r'scrib+i', re.I),
                'Residential Proxies': (r'dential\s*?prox', re.I),
                'Transcribe me': (r'transcribe\s*?me', re.I),
                'Transcription Staff': (r'ptions*?\s*?staf+', re.I),
                'Speech pad': (r'spe+ch\s*?pad', re.I),
                'Sweetstudy': (r'swe+t\s*?stud|work\s*?market', re.I), 
                'Essayshark': (r'es+ay\s*?shark', re.I),
                'Freelance Writing center': (r'fre+lance\s*?writing\s*?(?:center|centre)|fwc', re.I),
                'Essaywriters': (r'es+ay\s*?writers?', re.I),
                'Quality Writers': (r'quality\s*?writers*?', re.I),
                'Livingstone Research': (r'ston', re.I),
                'VIP Writers': (r'VIP\s*?', re.I),
                'Bluecorp Service': (r'Blue\s*?corp\s*?service', re.I),
                '24writers': (r'\b24\s*?write\b|\b24Writers\b', re.I),
                '4writers': (r'\b4writers\b', re.I),
                'ProWritersTime': (r'pro\s*?writers*?\s*?time', re.I),
                'ProWritersPro': (r'\bProwriters.pro\b', re.I),
                'Textbroker': (r'text\s*?broker', re.I),
                'UvoCorp': (r'uvo', re.I),
                'Focus Forward': (r'\bfocus\b', re.I),
                'Verbit': (r'\bverbit\b', re.I),
                '24houranswers': (r'\bhouranswers \b', re.I),
                'Wyzant': (r'Wyzant', re.I),
                'Studydaddy': (r'.dad+y.|studydaddy', re.I),
                'Studygate': (r'.gate', re.I),
                'Transtutors': (r'transtutors?', re.I), #Revisit here
                'Topwriterlist': (r'Top\s*?writers*?\s?list', re.I),
                'Chat from home': (r'Chat\s*?from\s*?home', re.I),
                'Hirewriters': (r'hire\s*?writer', re.I), #Revisit here
                'Enemployed Professor': (r'.Unemployed\s*?prof.|UNEMPLOYED PROFESSOR', re.I),
                'Course Hero': (r'Course\s*?Hero', re.I),
                'GoTranscript': (r'Go\s*?Transcript', re.I),
                'Jobs4Writers': (r'Jobs?(4|for)writer(s)?', re.I),
                'Homeworkforyou': (r'homeworkforyou', re.I)
            },
            'order_patterns': {
                'zero_plus': (r'(?:done\s*|whip?ped\s*|completed?\s*|executed\s*)?\s*?(\d+k?|\d+|\d+\s*?\+)\+?\s*(?:\s*?order?s?|question.?|plus?|whipped?|done.?)', re.IGNORECASE),
                'zero_orders': (r'\b(?:new|brand|mpya|newly|custom.)\b', re.IGNORECASE)
            },
            'condition_pattern': (r'\bnew\b', re.I), 
            'rating_patterns': {
                'new_unranked': (r'\b(new|unranked|not|yet)\b', re.I),
                'percentage': (r'(\d+(\.\d+)?)%', re.I),
                'fraction': (r'(\d+(\.\d+)?)/(\d+(\.\d+)?)', re.I),
                'stand_alone': (r'\b(\d+(\.\d+)?)\b', re.I)
            },
            'bid_take_group': {
                'Edusson': 'bid', 
                'Studypool': 'bid',
                'Writerbay': 'both',
                'Writezillas': 'bid',
                'Echolabs': 'bid',
                'Texting Factory': 'bid',
                'CoudWorkers': 'bid',
                'Writedom': 'bid',
                'Fiverr': 'bid',
                'Nerdy Turtlez': 'take',
                'Writing Creek': 'bid',
                'Academia Research': 'bid',
                'Writerslabs': 'both',
                'Essaypro': 'bid',
                'Atlantic Writers': 'bid',
                'Simpletense': 'bid',
                'TSM Group': 'take',
                'Studybay': 'bid',
                'Crowdsurf': 'bid',
                'Transcribe me': 'bid',
                'Sweetstudy': 'bid',
                'Essayshark': 'bid',
                'Freelance Writing center': 'bid',
                'Writershub': 'both',
                'Verbit': 'bid',
                'Focus Forward': 'bid',
                'Essaywriters': 'both',
                None: 'bid',
                '4writers': 'take',
                'Livingstone Research': 'take',
                'Quality Writers': 'take',
                '24writers': 'bid',
                'Remotask': 'bid',
                'Studygate': 'bid',
                'Course Hero': 'take',
                'Crown Content': 'bid',
                'GoTranscript': 'bid',
                'Transtutors': 'bid',
                'Scribie': 'bid',
                'Bluecorp Service': 'bid',
                'Hirewriters': 'bid',
                'Transcription Staff': 'bid',
                'Textbroker': 'bid',
                'Residential Proxies': 'bid',
                'VIP Writers': 'bid',
                'Chat from home': 'bid',
                'Topwriterlist': 'take',
                'Enemployed Professor': 'bid',
                'UvoCorp': 'both',
                'ProWritersTime': 'bid',
                'Studydaddy': 'bid',
                'ProWritersPro': 'bid',
                'Wyzant': 'bid'
            }
        }

    def __getitem__(self, key):
        return self.parameters[key]

