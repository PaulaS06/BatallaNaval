create table navalbattle (
  starting_code varchar(5) primary key not null,
  rows varchar(1) not null,
  columns varchar(1) not null,
  ship_count varchar(1) ,
  hits int ,
  misses int ,
  total_shots int ,
  max_possible_shots int ,
  score int not null
);
