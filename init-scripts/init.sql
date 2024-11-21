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
