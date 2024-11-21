CREATE DATABASE IF NOT EXISTS db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE db;

CREATE TABLE IF NOT EXISTS public_records (
	id INT PRIMARY KEY AUTO_INCREMENT,
	processo VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
	ano VARCHAR(4),
	tipo VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
	assunto TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
	data DATETIME,
	situacao VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
	arquivo TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
	autor VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
);

CREATE TABLE IF NOT EXISTS law_records ( 
	id INT PRIMARY KEY AUTO_INCREMENT, 
	tipo VARCHAR(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci, 
	numero INT(4), 
	ano INT(4), 
	data DATETIME, 
	autor VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci, 
	resumo TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci, 
	situacao VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci, 
	tema VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
);
