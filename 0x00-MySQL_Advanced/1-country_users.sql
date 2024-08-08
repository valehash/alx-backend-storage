-- script to CREATE a user tbale it's params
-- icountry, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
CREATE TABLE IF NOT EXISTS users (

  id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,

  email VARCHAR(255) NOT NULL UNIQUE,

  name VARCHAR(255),

  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'

);
