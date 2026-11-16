CREATE TABLE IF NOT EXISTS `mokoko_seed` (
  `pid` int(10) unsigned NOT NULL,
  `seed_id` smallint(5) unsigned NOT NULL,
  `collected` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`pid`,`seed_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `mokoko_reward` (
  `pid` int(10) unsigned NOT NULL,
  `reward_id` smallint(5) unsigned NOT NULL,
  `claimed` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`pid`,`reward_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

