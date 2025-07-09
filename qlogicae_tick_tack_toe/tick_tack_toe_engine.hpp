#pragma once

#include "pch.h"

#include "qlogicae_core.hpp"

namespace QLogicaeTickTackToe
{
	enum class PlayerId : uint8_t
	{
		PLAYER_1 = 0,
		PLAYER_2 = 1
	};

	enum class GameMatchStatus : uint8_t
	{
		PLAYER_1_WINS = 0,
		PLAYER_2_WINS = 2,
		DRAW = 3,
		FOREFIT = 4
	};

	struct PlayerData
	{
		PlayerId id;
		std::string name;
	};

	struct PlayerMoveData
	{
		PlayerId player_id;
		uint8_t row_index;
		uint8_t column_index;
		std::chrono::nanoseconds time_since_previous_move;
		std::chrono::steady_clock::time_point timestamp_created;
	};

	struct GameSession
	{
		std::chrono::steady_clock::time_point timestamp_started;
		std::chrono::steady_clock::time_point timestamp_ended;
	};

	struct GameMatch
	{
		PlayerId winning_player_id;
		PlayerId losing_player_id;
		std::chrono::steady_clock::time_point timestamp_started;
		std::chrono::steady_clock::time_point timestamp_ended;
	};


}

/*

NOTES

start_session

setup
start
move
end
reset

data
- player
	- count
	- name
	- icon_uri
	- icon_url
	- id
- session
	- 
- game
	- total elapsed time in nanoseconds
	- total move count
	- total move count per player
	- win count
	- lose count
	- draw count
	- timestamp_created
- move
	- timestamp_created
	- player_id
	- row_index
	- column_index
- analysis
	- 
*/
