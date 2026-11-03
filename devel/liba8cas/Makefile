
COMMENT =		support for tapes used by Atari 8-bit computers

DISTNAME =		liba8cas-1.5.0
CATEGORIES =		devel

SHARED_LIBS +=		a8cas	0.0 # 2.1

HOMEPAGE =		https://sourceforge.net/projects/a8cas/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB +=		FLAC m mp3lame mpg123 ogg opus pthread sndfile vorbis
WANTLIB +=		vorbisenc pthread

LIB_DEPENDS =		audio/libsndfile

SITES =			${SITE_SOURCEFORGE:=a8cas/}

CONFIGURE_STYLE =	autoconf

AUTOCONF_VERSION =	2.69

NO_TEST =		Yes

.include <bsd.port.mk>
