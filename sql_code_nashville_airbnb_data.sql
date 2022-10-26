Select * from listingdec;

select * from listingjun;

select * from listingsep;

-- Inner Join of Dec and Mar tables
SELECT listingdec.id,
		listingdec.name,
		listingdec.host_id,
		listingdec.host_name,
		listingdec.neighbourhood_group,
		listingdec.neighbourhood,
		listingdec.latitude,
		listingdec.longitude,
		listingdec.room_type,
		listingdec.price,
		listingdec.minimum_nights,
		listingdec.number_of_reviews,
		listingdec.last_review,
		listingdec.reviews_per_month,
		listingdec.calculated_host_listings_count,
		listingdec.availability_365,
		listingdec.number_of_reviews_ltm,
		listingdec.license
FROM 
		listingdec
INNER JOIN listingmar
ON listingmar.id = listingdec.id

-- Union of all 4 data sets
Select * from listingdec
Union 
Select * from listingmar
Union 
Select * from listingjun
Union 
Select * from listingsep

-- Create a table to hold all the combined data from 4 csv files
CREATE TABLE Combined_Data (
	id varchar,
	name varchar (255),
	host_id varchar (255),
	host_name varchar (255),
	neighbourhood_group varchar(255),
	neighbourhood varchar(255),
	latitude decimal,
	longitude decimal,
	room_type varchar(255), 
	price int,
	minimum_nights int,
	number_of_reviews int,
	last_review date,
	reviews_per_month float,
	calculated_host_listings_count int,
	availability_365 int,
	number_of_reviews_ltm int,
	license varchar(255),
	PRIMARY KEY (id)
);

-- Load data from the combined 4 csv files into a new table
SELECT * 
	INTO Combined_Data
FROM (
Select * from listingdec
Union 
Select * from listingmar
Union 
Select * from listingjun
Union 
Select * from listingsep
)a

Select * FROM Combined_Data;

-- Use the Groupby function to aggregate the data
SELECT ID,
	NAME,
	neighbourhood,
	LATITUDE,
	LONGITUDE,
	room_type,
	AVG(PRICE) price,
	AVG(minimum_nights)minimum_nights,
	AVG (number_of_reviews) number_of_reviews
FROM COMBINED_DATA
   GROUP BY ID, NAME, neighbourhood, LATITUDE,LONGITUDE, room_type;

	
-- Select the Dec measures and change the name of the columns
CREATE TABLE december_measures AS
	SELECT
	id,
	price,
	minimum_nights,
	number_of_reviews,
	last_review,
	reviews_per_month,
	availability_365,
	number_of_reviews_ltm
	FROM listingdec;
	
SELECT * FROM december_measures

ALTER TABLE december_measures
	RENAME COLUMN price to dec_price;
ALTER TABLE december_measures
	RENAME COLUMN minimum_nights to dec_minimum_nights;
ALTER TABLE december_measures
	RENAME COLUMN number_of_reviews to dec_number_of_reviews;
ALTER TABLE december_measures
	RENAME COLUMN last_review to dec_last_review;
ALTER TABLE december_measures
	RENAME COLUMN reviews_per_month to dec_reviews_per_month;
ALTER TABLE december_measures
	RENAME COLUMN availability_365 to dec_availability_365;
ALTER TABLE december_measures
	RENAME COLUMN number_of_reviews_ltm to dec_number_of_reviews_ltm;
ALTER TABLE december_measures
	RENAME COLUMN id to dec_id;

SELECT * FROM december_measures

-- Select the Mar measures and change the name of the columns
CREATE TABLE march_measures AS
	SELECT
	id,
	price,
	minimum_nights,
	number_of_reviews,
	last_review,
	reviews_per_month,
	availability_365,
	number_of_reviews_ltm
	FROM listingmar;
	

ALTER TABLE march_measures
	RENAME COLUMN price to mar_price;
ALTER TABLE march_measures
	RENAME COLUMN minimum_nights to mar_minimum_nights;
ALTER TABLE march_measures
	RENAME COLUMN number_of_reviews to mar_number_of_reviews;
ALTER TABLE march_measures
	RENAME COLUMN last_review to mar_last_review;
ALTER TABLE march_measures
	RENAME COLUMN reviews_per_month to mar_reviews_per_month;
ALTER TABLE march_measures
	RENAME COLUMN availability_365 to mar_availability_365;
ALTER TABLE march_measures
	RENAME COLUMN number_of_reviews_ltm to mar_number_of_reviews_ltm;
ALTER TABLE march_measures
	RENAME COLUMN id to mar_id;

SELECT * FROM march_measures

-- Select the June measures and change the name of the columns
-- DROP TABLE june_measures

CREATE TABLE june_measures AS
	SELECT
	id,
	price,
	minimum_nights,
	number_of_reviews,
	last_review,
	reviews_per_month,
	availability_365,
	number_of_reviews_ltm
	FROM listingjun;
	

ALTER TABLE june_measures
	RENAME COLUMN price to jun_price;
ALTER TABLE june_measures
	RENAME COLUMN minimum_nights to jun_minimum_nights;
ALTER TABLE june_measures
	RENAME COLUMN number_of_reviews to jun_number_of_reviews;
ALTER TABLE june_measures
	RENAME COLUMN last_review to jun_last_review;
ALTER TABLE june_measures
	RENAME COLUMN reviews_per_month to jun_reviews_per_month;
ALTER TABLE june_measures
	RENAME COLUMN availability_365 to jun_availability_365;
ALTER TABLE june_measures
	RENAME COLUMN number_of_reviews_ltm to jun_number_of_reviews_ltm;
ALTER TABLE june_measures
	RENAME COLUMN id to jun_id;

SELECT * FROM june_measures


-- Select the September measures and change the name of the columns
CREATE TABLE september_measures AS
	SELECT
	id,
	price,
	minimum_nights,
	number_of_reviews,
	last_review,
	reviews_per_month,
	availability_365,
	number_of_reviews_ltm
	FROM listingsep;
	

ALTER TABLE september_measures
	RENAME COLUMN price to sep_price;
ALTER TABLE september_measures
	RENAME COLUMN minimum_nights to sep_minimum_nights;
ALTER TABLE september_measures
	RENAME COLUMN number_of_reviews to sep_number_of_reviews;
ALTER TABLE september_measures
	RENAME COLUMN last_review to sep_last_review;
ALTER TABLE september_measures
	RENAME COLUMN reviews_per_month to sep_reviews_per_month;
ALTER TABLE september_measures
	RENAME COLUMN availability_365 to sep_availability_365;
ALTER TABLE september_measures
	RENAME COLUMN number_of_reviews_ltm to sep_number_of_reviews_ltm;
ALTER TABLE september_measures
	RENAME COLUMN id to sep_id;


SELECT * FROM september_measures


-- Inner Join of new measurement tables

CREATE TABLE dimensions as
	select
	id,
		name,
		neighbourhood,
		latitude,
		longitude,
		room_type,
	from listingsep;


DROP TABLE combined_measures

SELECT id,
		name,
		neighbourhood,
		latitude,
		longitude,
		room_type,
		sep_price,
		jun_price,
		mar_price,
		dec_price
	INTO combined_measures
FROM dimensions
INNER JOIN september_measures
on september_measures.sep_id = dimensions.id
INNER JOIN june_measures
on june_measures.jun_id = dimensions.id
INNER JOIN march_measures
on march_measures.mar_id = dimensions.id
INNER JOIN december_measures
on december_measures.dec_id = dimensions.id

select * from combined_measures;
