##Database Setup

CREATE TABLE menu (
    ID INT NOT NULL AUTO_INCREMENT,
    ITEM VARCHAR(25) NOT NULL,
    Category VARCHAR(25) NOT NULL,
    Note VARCHAR(40),
    PRIMARY KEY (ID)
) COMMENT '';

##Add the sample Data
INSERT INTO menu ('item' , 'category' , 'note' , 'price') VALUES (2 , 'Sandwish' , 'Main Dish' , '3')



##Install the modules

pip install Flask 
pip install render_template
pip install request
pip install url_for 
pip install redirect

## Run the flask app

flask run --host=0.0.0.0
