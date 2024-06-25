-- creacion de una nueva base de datos 
CREATE DATABASE JacarandaCLienteUser;
-- Apuntamosa o llamamos a la base de datos
USE JacarandaClienteUser;
/* creacion de las tablas ( por convenencia se crea
la tabla con el valor relacional de ultima instancia
*/

CREATE TABLE dataLogin (
id INT NOT NULL AUTO_INCREMENT,
user_id INT NOT NULL,
userName VARCHAR(25),
userPassword VARCHAR(8),
PRIMARY KEY (id)
);

CREATE TABLE usuario (
id INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(50),
apellido VARCHAR(50),
email VARCHAR(50),
telefono VARCHAR(10),
PRIMARY KEY (id)
);

CREATE TABLE acumCarrito(
id INT NOT NULL AUTO_INCREMENT,
user_id INT NOT NULL,
imagen VARCHAR(100),
descripcion VARCHAR(200),
precio VARCHAR(15),
PRIMARY KEY (id)
);


/*
luego de crear las tablas establesemos las claves forañas
*/

ALTER TABLE dataLogin 
	ADD FOREIGN KEY(user_id) REFERENCES usuario(id)
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;
    
ALTER TABLE acumCarrito
	ADD FOREIGN KEY(user_id) REFERENCES usuario(id)
    ON UPDATE NO ACTION 
    ON DELETE NO ACTION;
