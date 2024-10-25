CREATE TABLE Politico (
  pol_id INT PRIMARY KEY,
  pol_nome VARCHAR(100)
);

CREATE TABLE Proposicao (
  prop_tipo VARCHAR(25),
  prop_id VARCHAR(10) PRIMARY KEY,
  prop_data DATE,
  prop_descricao VARCHAR(300),
  prop_situacao VARCHAR(30)
);

CREATE TABLE Lei (
  lei_tipo VARCHAR(25),
  lei_id VARCHAR(12) PRIMARY KEY,
  lei_data DATE,
  lei_descricao VARCHAR(300),
  lei_situacao VARCHAR(30),
  lei_tema VARCHAR(1000)
);

CREATE TABLE AutoriaProp (
  Proposicao_prop_tipo VARCHAR(25),
  Proposicao_prop_id VARCHAR(10),
  Politicos_pol_id INT,
  PRIMARY KEY (Proposicao_prop_tipo, Proposicao_prop_id, Politicos_pol_id),
  FOREIGN KEY (Proposicao_prop_tipo, Proposicao_prop_id) REFERENCES Proposicao(prop_tipo, prop_id),
  FOREIGN KEY (Politicos_pol_id) REFERENCES Politico(pol_id)
);

CREATE TABLE AutoriaLei (
  Politico_pol_id INT,
  Lei_lei_tipo VARCHAR(25),
  Lei_lei_id VARCHAR(12),
  PRIMARY KEY (Politico_pol_id, Lei_lei_tipo, Lei_lei_id),
  FOREIGN KEY (Politico_pol_id) REFERENCES Politico(pol_id),
  FOREIGN KEY (Lei_lei_tipo, Lei_lei_id) REFERENCES Lei(lei_tipo, lei_id)
);