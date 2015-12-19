from __future__ import absolute_import, division, print_function

import json

from . import GamesFactory
from . import YahooFantasySportsError
from .utils import base_url, build_uri, yfs_request

from requests import HTTPError


class YahooFantasySports(object):
    """
    Interact with the Yahoo Fantasy Sports Servers.

    :param oauth: OAuth1 instance connected to the Yahoo servers.
    :type oauth: yahoo_oauth.Oauth1
    :param fmt: Format of the response. Either 'json' or 'xml'. Defaults
        to 'json'.
    :type fmt: str
    :param use_login:
    :type use_login: bool
    """

    def __init__(self, oauth, fmt='json', use_login=False):
        self.oauth = oauth
        self.fmt = fmt
        self.use_login = use_login
        self.games = GamesFactory(oauth)

    def __repr__(self):
        return "<{0}> <{1}>".format(base_url, self.fmt)

    def test_uri(self, uri):
        print(json.dumps(yfs_request(self.oauth, base_url + uri),
              indent=4))

#    def get_collections(self, resource_type, resource_ids, sub_resources):
#        """Test Generic method to get collections
#        """
#        uri = self._build_uri(resource_type, resource_ids, sub=sub_resources)
#        response = self._get(uri)
#        return response
#
#    #################################
#    #
#    #           GAMES
#    #
#    #################################
#
#    def get_games_info(self, game_keys, leagues=None, teams=False, players=None):
#        """Return game info
#        >>> yfs.get_games_info('mlb')
#        Must set use_login to True to pull teams data
#        """
#        uri = self._build_uri('games;game_keys', game_keys)
#        
#        if leagues:
#            uri += '/leagues;league_keys={0}'.format(leagues)
#        
#        if teams:
#            uri += '/teams'
#            
#        if players:
#            uri += '/players;player_keys={0}'.format(players)
#            
#        response = self._get(uri)
#
#        return response
#
#
#    ####################################
#    #
#    #           LEAGUES 
#    #
#    ####################################
#    def get_leagues(self, league_keys):
#        """Return league data
#        >>> yfs.get_leagues(['league_key'])
#        """     
#        uri = self._build_uri('leagues;league_keys',league_keys)
#        response = self._get(uri)
#        return response
#
#    def get_leagues_teams(self, league_keys):
#        """Return leagues teams
#        >>> yfs.get_leagues_teams(['238.l.627062'])
#        """
#        uri = self._build_uri('leagues;league_keys', league_keys, sub='teams')
#        response = self._get(uri)
#        return response
#        
#    def get_leagues_players(self, league_keys):
#        """Return leagues players
#        >>> yfs.get_leagues_teams(['238.l.627062'])
#        """
#        uri = self._build_uri('leagues;league_keys', league_keys, sub='players')
#        response = self._get(uri)
#        return response    
#
#    def get_leagues_scoreboard(self, league_keys, week=None):
#        """Return leagues scoreboard
#        >>> yfs.get_leagues_scoreboard(['league_key'])
#        """
#        uri = self._build_uri('leagues;league_keys',league_keys, sub='scoreboard')
#
#        if week:
#            uri += ';week={0}'.format(week)
#
#        response = self._get(uri)
#        return response
#
#    def get_leagues_settings(self, league_keys):
#        """Return leagues settings
#        >>> yfs.get_leagues_settings(['238.l.627062','238.l.627062'])
#        """
#        uri = self._build_uri('leagues;league_keys', league_keys, sub='settings')
#        response = self._get(uri)
#        return response
#
#    def get_leagues_standings(self, league_keys, teams=None, players=None):
#        """Return leagues settings
#        >>> yfs.get_leagues_settings(['238.l.627062','238.l.627062'])
#        """
#        uri = self._build_uri('leagues;league_keys', league_keys, sub='standings')
#        
#        if teams:
#            uri += '/teams/{0}'.format(teams)
#            
#        if teams=='roster' and players:
#            uri += '/players/{0}'.format(players)
#        
#        response = self._get(uri)
#        return response
#
#    def get_leagues_transactions(self, league_keys):
#        """Return leagues settings
#        >>> yfs.get_leagues_transactions(['238.l.627062'])
#        """
#        uri = self._build_uri('leagues;league_keys', league_keys, sub='transactions')
#        response = self._get(uri)
#        return response
#
#    def get_leagues_draftresults(self, league_keys):
#        """Return leagues draftresults
#        >>> yfs.get_leagues_draftresults(['238.l.627062'])
#        """
#        uri = self._build_uri('leagues;league_keys', league_keys, sub='draftresults')
#        response = self._get(uri)
#        return response
#
#
#    #########################################
#    #
#    #       PLAYERS (not league specific)
#    #
#    #########################################
#    
#    def get_players(self, player_keys, filters=None):
#        """Return player data
#        >>> yfs.get_players(['player_key'])
#        """     
#        uri = self._build_uri('players;player_keys', player_keys)
#        
#        if filters and isinstance(filters, str):
#            uri += ';{0}'.format(filters)
#        if filters and not isinstance(filters, str):
#            uri += ";{0}".format(','.join([e for e in filters]))
#
#        response = self._get(uri)
#        return response
#        
#    def get_players_stats(self, player_keys, week=None):
#        """Return player stats (not league specific)
#        >>> yfs.get_players_stats(['223.p.5479'], week=3)
#        """     
#        uri = self._build_uri('players;player_keys', player_keys, sub='stats')
#        
#        if week:
#            uri += ';type=week;week={0}'.format(week)
#        
#        response = self._get(uri)
#        return response
#        
#    def get_players_percent_owned(self, player_keys):
#        """Return ownership percentage of player (not league specific)
#        >>> yfs.get_players_percent_owned([223.p.5479])
#        """     
#        uri = self._build_uri('players;player_keys', player_keys, sub='percent_owned')
#        response = self._get(uri)
#        return response
#          
#    def get_players_draft_analysis(self, player_keys):
#        """Return draft metrics for player (not league specific)
#        >>> yfs.get_players_draft_analysis([223.p.5479])
#        """     
#        uri = self._build_uri('players;player_keys', player_keys, sub='draft_analysis')
#        response = self._get(uri)
#        return response
#
#    ###################################
#    #
#    #           TEAMS
#    #   
#    ###################################
#    
#    
#    def get_teams(self, team_keys):
#        """Return team data
#        >>> yfs.get_teams(['league_key'])
#        """     
#        uri = self._build_uri('teams;team_keys',team_keys)
#        response = self._get(uri)
#        return response
#        
#    def get_teams_players(self, team_keys):
#        """Return teams players
#        >>> yfs.get_teams_players(['238.l.627062'])
#        """
#        uri = self._build_uri('teams;team_keys', team_keys, sub='players')
#        response = self._get(uri)
#        return response        
#        
#    def get_teams_stats(self, team_keys, week=None):
#        """Return team stats (week only for H2H league)
#        >>> yfs.get_teams_stats(['238.l.627062.t.1'], week=3)
#        """     
#        uri = self._build_uri('teams;team_keys',team_keys, sub='stats')
#        
#        if week:
#            uri += ';type=week;week={0}'.format(week)
#        
#        response = self._get(uri)
#        return response
#    
#    def get_teams_standings(self, team_keys):
#        """Return team standings
#        >>> yfs.get_teams_standings(['238.l.627062.t.1'])
#        """     
#        uri = self._build_uri('teams;team_keys',team_keys, sub='standings')
#        response = self._get(uri)
#        return response
#        
#    def get_teams_roster(self, team_keys, week=None, players=None, filters=None):
#        """Return team roster
#        >>> yfs.get_teams_roster(['238.l.627062.t.1'], week=3)
#        """     
#        uri = self._build_uri('teams;team_keys',team_keys, sub='roster')
#            
#        if week:
#            uri += ';week={0}'.format(week)
#        
#        if players and filters:
#            uri += '/players;{1}/{0}'.format(filters, players)
#            
#        elif filters and not players:
#            uri += '/players;{0}'.format(filters) 
#            
#        elif players and not filters:
#            uri += '/players/{0}'.format(players)   
#        
#        response = self._get(uri)
#        return response
#        
#    def get_teams_draftresults(self, team_keys):
#        """Return a team's draft results
#        >>> yfs.get_teams_draftresults(['238.l.627062.t.1'])
#        """     
#        uri = self._build_uri('teams;team_keys',team_keys, sub='draftresults')
#        response = self._get(uri)
#        return response
#        
#    def get_teams_matchups(self, team_keys, weeks=None):
#        """Return team matchups (H2H leagues only)
#        >>> yfs.get_teams_matchups(['238.l.627062.t.1'], weeks='1,3,6')
#        """     
#        uri = self._build_uri('teams;team_keys',team_keys, sub='matchups')
#        
#        if weeks and isinstance(weeks, str):   
#            uri += ';weeks={0}'.format(weeks)    
#        if weeks and not isinstance(weeks, str):
#            uri += ";weeks{0}".format(','.join([e for e in weeks]))
#            
#        response = self._get(uri)
#        return response
#        
#        
#        
#    ##############################################
#    #
#    #    ROSTERS (team specific player info)
#    #
#    ##############################################
#    
#    def get_roster_players(self, team_keys, week=None, date=None):
#        """Access roster info, with player sub option
#        >>> yfs.get_roster_players(['238.l.627062'])
#        """
#        uri = self._build_uri(None, team_keys, sub='roster/players')
#        uri = 'team/{0}'.format(uri) # Done to avoid having 'team=238.l.627062', which doesn't work for this resource
#
#        if week: 
#            uri += ';week={0}'.format(week)
#        if date:
#            uri += ';date={0}'.format(date)
#        
#        response = self._get(uri)
#        return response 
#
#    def set_roster_players(self, team_keys, roster):
#        """
#        >>> from fantasy_sport import Roster, Player
#        >>> p1 = Player('242.p.8332','WR')
#        >>> p2 = Player('242.p.8334','WL')
#        >>> roster = Roster([p1, p2], date='2015-01-11')
#        >>> ysf.set_roster_players(['238.l.627062'], roster)
#        """
#        uri = self._build_uri(None, team_keys, sub='roster/players')
#        uri = 'team/{0}'.format(uri)
#
#        response = self._put(uri, roster)
#        return response 
#        
#        
#    ##############################################
#    #
#    #    TRANSACTIONS
#    #
#    ##############################################
#    
#    def get_transactions(self, transaction_keys, players=None):
#        """Return transaction data
#        >>> yfs.get_transaction(['transaction_key'])
#        """ 
#        
#        if players:
#            subtext = 'players/{0}'.format(players)    
#            uri = self._build_uri('transactions;transaction_keys', transaction_keys, sub=subtext)
#        else:
#            uri = self._build_uri('transactions;transaction_keys', transaction_keys)
#            
#        response = self._get(uri)
#        return response
