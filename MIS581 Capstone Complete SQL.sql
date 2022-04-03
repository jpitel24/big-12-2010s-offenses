#Creation of the table to hold the dataset in PostgreSQL
CREATE TABLE play_data
(
    offense character varying(50),
    offense_conference character varying(50),
    defense character varying(50),
    defense_conference character varying(50),
    home character varying(50),
    away character varying(50),
    offense_score integer,
    defense_score integer,
    game_id integer,
    drive_number integer,
    play_number integer,
    quarter integer,
    clock_minutes integer,
    clock_seconds integer,
    offense_tos integer,
    defense_tos integer,
    yard_line integer,
    yards_to_goal integer,
    down integer,
    distance integer,
    scoring boolean,
    yards_gained integer,
    play_type character varying(100)
);

#Importing the dataset from local .csv file to table created above
COPY play_data
FROM 'C:\Users\Public\Documents\Big 12 Offense 2010 thru 2019.csv'
DELIMITER ','
CSV HEADER;

#Clearing irrelevant plays from the dataset to focus on the actual offensive production
DELETE FROM play_data
WHERE play_type = 'Kickoff'
OR play_type = 'Punt'
OR play_type = 'Penalty'
OR play_type = 'Timeout'
OR play_type = 'End Period'
OR play_type = 'End of Half'
OR play_type = 'Field Goal Good'
OR play_type = 'Field Goal Missed'
OR play_type = 'Kickoff Return (Offense)'
OR play_type = 'Blocked Field Goal'
OR play_type = 'Blocked Punt'
OR play_type = 'Kickoff Return Touchdown'

#Export cleaned dataset back to .csv for import into Python
COPY play_data 
TO 'C:\Users\Public\Documents\Capstone_SQL.csv'
DELIMITER ','
CSV HEADER;