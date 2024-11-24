COMMENT =	digital soundcard software for amateur radio

GH_ACCOUNT =	wb2osz
GH_PROJECT =	direwolf
GH_TAGNAME =	1.7

CATEGORIES =	comms hamradio

MAINTAINER =	Bryan Vyhmeister <bryan@bsdjournal.net>

# GPLv2
PERMIT_PACKAGE =	Yes

MODULES = 	devel/cmake
WANTLIB += 	c m pthread sndio gps hamlib

LIB_DEPENDS =	comms/hamlib \
		misc/gpsd

RUN_DEPENDS =	audio/espeak

post-configure:
	find ${WRKSRC} -name '*.sh' -print0 | xargs -0r \
		perl -pi -e 's,^#!/bin/bash,#!/bin/sh,g'
#		perl -pi -e 's,^#!/bin/bash,#!${LOCALBASE}/bin/bash,g'

.include <bsd.port.mk>
