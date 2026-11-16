// Ara:
ACMD(do_energy_crystal);

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
ACMD(do_mokoko_info);
ACMD(do_mokoko_rewards);
ACMD(do_mokoko_claim);
ACMD(do_mokoko_reload);
#endif


// Ara:
	{ "energy_crystal", do_energy_crystal, 0, POS_DEAD, GM_PLAYER },

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
	{ "mokoko_info", do_mokoko_info, 0, POS_DEAD, GM_PLAYER },
	{ "mokoko_rewards", do_mokoko_rewards, 0, POS_DEAD, GM_PLAYER },
	{ "mokoko_claim", do_mokoko_claim, 0, POS_DEAD, GM_PLAYER },
	{ "mokoko_reload", do_mokoko_reload, 0, POS_DEAD, GM_IMPLEMENTOR },
#endif

