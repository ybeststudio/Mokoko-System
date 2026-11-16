// Ara:
{
	EnergyCrystal::OnCommand(ch, argument);
}

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
#include "mokoko.h"
ACMD(do_mokoko_info)
{
	Mokoko_Command(ch, "info", argument);
}

ACMD(do_mokoko_rewards)
{
	Mokoko_Command(ch, "rewards", argument);
}

ACMD(do_mokoko_claim)
{
	Mokoko_Command(ch, "claim", argument);
}

ACMD(do_mokoko_reload)
{
	Mokoko_Command(ch, "reload", argument);
}
#endif

