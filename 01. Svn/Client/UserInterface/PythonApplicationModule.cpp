// void initapp() icinde:
// Ara:
	PyModule_AddIntConstant(poModule, "ENABLE_TARGET_DROP_CHANCE", 0);

// Altina ekle:
#ifdef ENABLE_MOKOKO_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_MOKOKO_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_MOKOKO_SYSTEM", 0);
#endif

