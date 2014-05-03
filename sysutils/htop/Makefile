# $OpenBSD$

COMMENT =	htop, an interactive process viewer

V =		1.0.3
DISTNAME =	htop-${V}
CATEGORIES =	sysutils
HOMEPAGE =	http://hisham.hm/htop/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${HOMEPAGE}/releases/${V}/

CONFIGURE_STYLE = 	gnu
CONFIGURE_ARGS =	--disable-taskstats --disable-hwloc --disable-native-affinity
CONFIGURE_ENV =		ac_cv_file__proc_stat=yes ac_cv_file__proc_meminfo=yes

NO_TEST =		Yes

.include <bsd.port.mk>
