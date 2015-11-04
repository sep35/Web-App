CREATE TABLE Users
( user_id INTEGER PRIMARY KEY,
  name VARCHAR(256) NOT NULL,
  email VARCHAR(256) NOT NULL UNIQUE,
  password VARCHAR(256) NOT NULL
);
 CREATE TABLE Team_Member
 ( user_id INTEGER REFERENCES Users (user_id),
   team_id INTEGER REFERENCES Team (team_id),
   UNIQUE (user_id,team_id)
 );
 CREATE TABLE Team
( id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(256) NOT NULL UNIQUE
);
CREATE TABLE Shoe
( shoe_id INTEGER PRIMARY KEY,
  name VARCHAR(256),
  mileage INTEGER DEFAULT 0,
  expiration_mileage INTEGER DEFAULT 500
);
CREATE TABLE Activity
( activity_id Integer NOT NULL PRIMARY KEY,
  date DATE NOT NULL,
  user_id INTEGER REFERENCES Users (user_id),
  distance INTEGER,
  time INTEGER,
  shoe_id INTEGER REFERENCES Shoe,
  activity_Type VARCHAR(256) DEFAULT 'Normal Run',
  conditions VARCHAR(512),
  location VARCHAR(512),
  comments VARCHAR(512)
);
CREATE TABLE RACES
( activity_id INTEGER REFERENCES Activity (activity_id),
  UNIQUE (activity_id),
  name VARCHAR(256),
  distance INTEGER,
  time INTEGER,
  place VARCHAR(256)
);
CREATE TABLE WORKOUT
( activity_id INTEGER REFERENCES Activity (activity_id),
  interval_num INTEGER NOT NULL,
  distance INTEGER,
  actual_time VARCHAR(256),
  goal_time VARCHAR(256),
  rest VARCHAR(256),
  PRIMARY KEY (activity_id,interval_num)
);

CREATE FUNCTION update_s() RETURNS TRIGGER AS $$
  BEGIN
    -- YOUR IMPLEMENTATION GOES HERE
    RETURN NEW;
  END;
  $$ LANGUAGE plpgsql;
CREATE TRIGGER UPDATE_SHOE
  AFTER INSERT ON Activity
  FOR EACH ROW
  EXECUTE PROCEDURE update_s();

INSERT INTO Users VALUES(1,'aaron', 'a@aaron.com', 'hiuadhf');
INSERT INTO Users VALUES(2,'Weston', 'w@aaron.com', 'highds');
INSERT INTO Shoe Values(1,'Pegs','0');

SELECT * FROM SHOE;
