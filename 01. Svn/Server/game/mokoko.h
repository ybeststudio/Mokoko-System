/*********************************************************************
 * File Name : mokoko.h
 * Author    : BestStudio
 * Version   : 1.0.0
 * Date      : 10-11-2026  
 */

#pragma once

#ifdef ENABLE_MOKOKO_SYSTEM
// Anka Mokoko seeds: NPC 9101 spawned on the teleport-window maps, collected once per character by clicking it.
//   locale/<locale>/mokoko_seeds.txt   : id region mapIndex localX localY
//   locale/<locale>/mokoko_rewards.txt : id type(0 milestone, 1 chest) required vnum count
// Commands: /mokoko_info, /mokoko_rewards, /mokoko_claim <id>, /mokoko_reload (GM)
//           MokokoRewardsBegin <found> <total>, MokokoRewardEntry <id> <type> <required> <claimed> <vnum:count>,
//           MokokoRewardsEnd <pending>, MokokoRewardResult <code> <id>, MokokoFound <found> <total> <region> <regionFound> <regionTotal>
enum EMokokoRewardResult
{
	MOKOKO_REWARD_RESULT_OK,
	MOKOKO_REWARD_RESULT_INVALID,
	MOKOKO_REWARD_RESULT_LOCKED,
	MOKOKO_REWARD_RESULT_ALREADY_CLAIMED,
	MOKOKO_REWARD_RESULT_INVENTORY_FULL,
	MOKOKO_REWARD_RESULT_DATABASE_ERROR,
};

void Mokoko_SpawnMap(long lMapIndex, long lBaseX, long lBaseY);
bool Mokoko_IsHiddenFor(const CHARACTER* pkSeed, const CHARACTER* pkViewer);
bool Mokoko_OnClick(LPCHARACTER ch, LPCHARACTER pkSeed);
void Mokoko_OnLogin(LPCHARACTER ch);
void Mokoko_OnDestroy(LPCHARACTER ch);
void Mokoko_Command(LPCHARACTER ch, const char* szCommand, const char* argument);
#endif
