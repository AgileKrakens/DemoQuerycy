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
SET character_set_client = utf8mb4;
SET character_set_connection = utf8mb4;
SET character_set_results = utf8mb4;
