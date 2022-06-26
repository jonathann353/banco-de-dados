#criando o banco de dados
create database banco;
#indicando o banco a ser usado
use banco;
#tabela usuario
create table usuario(
id_usuario int primary key auto_increment not null,
nome varchar(50) not null,
num_rfid int not null
);
#tabela livros
create table livros(
id_livro int primary key auto_increment not null,
Cód_acervo int not null,
Cód_exemplar int not null,
Cód_Título varchar(125) not null,
Cód_Classificação varchar(125) not null
);
#tabela emprestimo
create table empLivro(
id_emplivro int primary key auto_increment, 
fk_id_usuario int,
foreign key (fk_id_usuario) references usuario(id_usuario),
fk_id_livro int,
foreign key (fk_id_livro) references livros(id_livro),
data TIMESTAMP DEFAULT now()
);
#inserir dados na tabela emplivro
insert into emplivro(fk_id_usuario,fk_id_livro) values(4, 1345);
#consulta na tabela emprestimo
select usuario.nome, livros.Cód_Título, data from emplivro 
inner join usuario 
on emplivro.fk_id_usuario = usuario.id_usuario
inner join livros
on emplivro.fk_id_livro = livros.id_livro;