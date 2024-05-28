
if not exists(  
select * from sys.tables WHERE object_id = OBJECT_ID(N'dbo.netflix') and type='U')

	create table dbo.netflix(
		show_id varchar(MAX),
		type_show varchar(MAX),
		title varchar(max),
		director varchar (max),
		cast_show  varchar (MAX),
		country varchar (MAX),
		date_added varchar (MAX),
		release_year varchar (MAX),
		rating varchar (MAX),
		duration varchar (MAX),
		listes_id varchar(MAX),
		description_show varchar (max)
	)
-- SI LA TABLA YA EXISTE ENTONCES ELIMINO 

truncate TABLE dbo.netflix
-- insertar el csv dataset
BULK INSERT dbo.netflix 
from 'C:\Users\Margot\Documents\proyecto_parcial\python\dataset\netflix_titles.csv'
with 
(
	FIRSTROW =2, --empieza en la 2da fila, 1 cabecera
	FIELDTERMINATOR =',', -- indicamos separadores de columnas
	ROWTERMINATOR='0x0a' --hace referencia al salto de linea
)

GO


