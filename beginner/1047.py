#Read the start time, start minute, end time and end minute of a game. 
# Then calculate the duration of the game.
#Note: The game has a minimum duration of one (1) minute and a maximum duration of 24 hours.

# Read the start time, start minute, end time and end minute of a game.
start_time, start_minute, end_time, end_minute = map(int, input().split())

# Calculate the total duration in minutes
start_duration = start_time * 60 + start_minute
end_duration = end_time * 60 + end_minute

# Calculate the duration of the game in minutes
duration_minutes = end_duration - start_duration

# If the duration is negative, adjust it to wrap around 24 hours
if duration_minutes < 0:
    duration_minutes += 24 * 60

# Calculate hours and minutes from the total duration
duration_hours = duration_minutes // 60
duration_minutes %= 60

# If the duration is 0, set it to 24 hours
if duration_hours == 0 and duration_minutes == 0:
    duration_hours = 24

print(f'O JOGO DUROU {duration_hours} HORA(S) E {duration_minutes} MINUTO(S)')
