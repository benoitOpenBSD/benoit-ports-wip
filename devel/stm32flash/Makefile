# $OpenBSD$

COMMENT =	flashing utility for STM32 and STM32W through UART or I2C

DISTNAME =	stm32flash-0.5
CATEGORIES =	devel

HOMEPAGE =	https://sourceforge.net/projects/stm32flash/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB +=	c

# MASTER_SITES =	http://www.arcane-labs.net/download/OpenBSD/
MASTER_SITES =	${MASTER_SITE_SOURCEFORGE:=stm32flash/}

WRKDIST =	${WRKDIR}/stm32flash

NO_TEST =	Yes

.include <bsd.port.mk>
