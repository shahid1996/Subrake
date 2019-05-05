import sys
import os
import random

__logo__ = """%s
  ______            _____              ______
 /_/_/__/      |    | \\  \       |     | |  /
 \______       |___ |__\\_/  __   |  /  |____\\
   _____\ |  | |\\  ||   /  /\\ \  | /   |    /
  /_/_/_/ |__| |_\\_||   \_ \_\\/_/| \\_/\\|_|__\\
%s      
                               %sv1.0. @hash3liZer%s
"""

__help__ = """
Description:
            A subdomain Enumeration tool for identifying subdomains, their response codes on HTTP and HTTPS, Possible used server using headers and CNAMES of identified subdomains.

Syntax: 
    $ python subrake -d shellvoide.com -w small     // SMALL wordlist scan
    $ python subrake -d shellvoide.com -w large --threads 30

Options:
   Args                 Description                      Default
   -h, --help           Show this manual                  NONE
   -d, --domain         Target domain. Possible
                        example: [example.com]            NONE
   -w, --wordlist       Wordlist for subdomains
                        to test. Two internal wordlists
                        can be specified as `small` and
                        `large`.                          NONE
   -t, --threads        Number of threads to spawn         25
   -o, --output         Push discovered information to
                        an output file in csv 
                        or simple format                  NONE
   -s, --output-subs    Push discovered subdomains to
                        an output file                    NONE
   -f, --format         Output format. Possible Values
                        are simple and csv               simple
   -p, --ports          Comma-seperated ports to scan.
                        50 most common used ports are      50
                        scanned by default                 
       --skip-ports     Skip Port Scanning.               FALSE
       --skip-online    Skip Online Subdomain Scan        FALSE
       --skip-wordlist  Skip Wordlist Scan                FALSE
"""

class PULLY:

	WHITE = '\033[0m'
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'
	LINEUP = '\033[F'

	MIXTURE = {
		'WHITE': '\033[0m',
		'PURPLE': '\033[95m',
		'CYAN': '\033[96m',
		'DARKCYAN': '\033[36m',
		'BLUE': '\033[94m',
		'GREEN': '\033[92m',
		'YELLOW': '\033[93m',
		'RED': '\033[91m',
		'BOLD': '\033[1m',
		'UNDERLINE': '\033[4m',
		'END': '\033[0m',
		'LINEUP': '\033[F'
	}

	VACANT = {
		'WHITE': '',
		'PURPLE': '',
		'CYAN': '',
		'DARKCYAN': '',
		'BLUE': '',
		'GREEN': '',
		'YELLOW': '',
		'RED': '',
		'BOLD': '',
		'UNDERLINE': '',
		'END': '',
		'LINEUP': ''
	}


	def __init__(self):
		if not self.support_colors:
			self.win_colors()

	def support_colors(self):
		plat = sys.platform
		supported_platform = plat != 'Pocket PC' and (plat != 'win32' or \
														'ANSICON' in os.environ)
		is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
		if not supported_platform or not is_a_tty:
			return False
		return True


	def win_colors(self):
		self.WHITE = ''
		self.PURPLE = ''
		self.CYAN = ''
		self.DARKCYAN = ''
		self.BLUE = ''
		self.GREEN = ''
		self.YELLOW = ''
		self.RED = ''
		self.BOLD = ''
		self.UNDERLINE = ''
		self.END = ''
		self.MIXTURE = {
			'WHITE': '',
			'PURPLE': '',
			'CYAN': '',
			'DARKCYAN': '',
			'BLUE': '',
			'GREEN': '',
			'YELLOW': '',
			'RED': '',
			'BOLD': '',
			'UNDERLINE': '',
			'END': '',
			'LINEUP': ''
		}

		for (key, val) in self.MIXTURE.items():
			self.MIXTURE[ key ] = ''

	def gthen(self, _tshow, cc='', *colors):
		for color in colors:
			cc += color
		print "%s[>]%s %s" % ( cc, self.END, _tshow )

	def lthen(self, _tshow, cc='', *colors):
		for color in colors:
			cc += color
		print "%s[<]%s %s" % ( cc, self.END, _tshow )

	def brick(self, _tshow, cc='', *colors):
		for color in colors:
			cc += color
		sys.exit( "%s[~]%s %s" % ( cc, self.END, _tshow ) )

	def slasher(self, _tshow, cc='', *colors):
		for color in colors:
			cc += color
		print "    %s-%s %s" % ( cc, self.END, _tshow )

	def psheada(self, color, **headfms):
		rs = headfms[ 'rs' ]	# Resolution
		cd = headfms[ 'cd' ]	# Codes
		sv = headfms[ 'sv' ]	# Server
		sb = headfms[ 'sb' ]	# Subdomain

		print color + rs.format( "RESOLUTION" ) + cd.format( "[HTTP/HTTPS]" ) + sb.format( "SUBOMAIN" ) + sv.format( "SERVER" ) + self.END

	def psrowa(self, color, **rowhvals):
		rsv = rowhvals[ 'rsv' ]
		cdv = rowhvals[ 'cdv' ]
		svv = rowhvals[ 'svv' ]
		sbv = rowhvals[ 'sbv' ]

		print rsv + cdv + sbv + svv

	def psheadb(self, color, **headfms):
		cdh = headfms[ 'cdh' ]
		sbh = headfms[ 'sbh' ]
		pth = headfms[ 'pth' ]
		cnh = headfms[ 'cnh' ]

		print color + cdh.format( "[HTTP/HTTPS]" ) + sbh.format( "SUBDOMAIN" ) + pth.format( "PORTS" ) + cnh.format( "CNAME" ) + self.END

	def psrowb(self, color, **rowfms):
		cdv = rowfms[ 'cdv' ]
		sbv = rowfms[ 'sbv' ]
		ptv = rowfms[ 'ptv' ]
		cnv = rowfms[ 'cnv' ]

		print cdv + sbv + ptv + cnv

	def linebreak(self, _num = 1):
		sys.stdout.write( "\n" * _num )

	def logo(self):
		_tochoose = [self.BLUE, self.YELLOW, self.RED, self.DARKCYAN, self.GREEN]
		print __logo__ % (self.BOLD + random.choice(_tochoose), self.END, self.BOLD, self.END)

	def help(self):
		print __help__