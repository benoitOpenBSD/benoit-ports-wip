# $OpenBSD$

COMMENT =	read, modify, create ELF files on any arch
DISTNAME =	elfutils-0.143
#SHARED_LIBS =	elf 0.10
CATEGORIES = 	devel

HOMEPAGE =	https://fedorahosted.org/elfutils/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		https://fedorahosted.org/releases/e/l/elfutils/

EXTRACT_SUFX =         .tar.bz2

#MAKE_FLAGS =		SHLIB_SFX=.so.$(LIBelf_VERSION)

USE_GMAKE =		Yes
 
CONFIGURE_STYLE =	gnu

CONFIGURE_ENV +=	CFLAGS='${CFLAGS} -pthread -I${LOCALBASE}/include' \
			LDFLAGS='${LDFLAGS} -L${LOCALBASE}/lib'
			
CONFIGURE_ARGS =	--disable-nls --with-zlib --with-bzlib

.include <bsd.port.mk>
