
COMMENT =		another graphical (SDL-based) hexadecimal dump tool

DISTNAME =		vix-0.1
CATEGORIES =		textproc

HOMEPAGE =		http://actinid.org/vix/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c SDL iconv m pthread sndio usbhid

SITES =			http://actinid.org/outcoming/

MODULES =		converters/libiconv

CONFIGURE_STYLE =	gnu

LIB_DEPENDS =		devel/sdl

NO_TEST =		Yes

# XXX
# On startup :
# (20639) error (draw_from_bmp@load.c:27): Couldn't open file "/usr/lib/vix/background.bmp": Fichier ou repertoire introuvable
#
# Need to modify :
#  src/main.c:  simtk_container_set_background (simtk_get_root_container (), "/usr/lib/vix/background.bmp");

.include <bsd.port.mk>
