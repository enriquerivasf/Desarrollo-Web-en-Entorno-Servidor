<?php
	$db = mysqli_connect('172.16.0.2','root','1234','mysitedb') or die('Fail');
?>
<html>
<head>
<style>
table, td,th{
border: 1px solid black;
	border-collapse: collapse;
}
.tr1:hover{
	background-color: green;
}
.id:hover{
	color:red;
}
.imagen{
	width: 100px;
	height: 100px;
	background: #f92672;
	transition: width 2s, height 2s, margin 2s;
	margin: 50px auto 0;
}
.imagen:hover{
	width: 100%;
	height: 200px;
	margin: 0 auto;

}

</style>
</head>
<body>
<h1>Conexión establecida</h1>
<table>
<tr>
<th>Id</th>
<th>Nombre</th>
<th>Imagen</th>
<th>genero</th>
<th>Edad recomendada</th>
</tr>
<?php
	//Lanzar una query
	$query = 'SELECT * FROM tPeliculas';
	$result = mysqli_query($db, $query) or die('Query error');
	// Recorrer el resultado
	while ($row = mysqli_fetch_array($result)) {
		echo '<tr class="tr1">';
		echo '<td>';
		echo '<a class="id" href="/detail.php?pelicula_id='.$row["id"].'">'.$row["id"].'</a>';
		echo '</td>';
		echo '<td>';
		echo '<div class="nombre">'.$row["nombre"].'</div>';
		echo '</td>';
		echo '<td>';
		echo '<img class="imagen" src="'.$row["url_imagen"];
		echo '"width="100" height="100">';
		echo '</td>';
		echo '<td>';
		echo $row["genero"];
		echo '</td>';
		echo '<td>';
		echo $row["edadRecomendada"];
		echo '</td>';
		echo '</tr>';
	}
?>
</table>
<a href="/logout.php">Logout</a>
<a href="cambiarContrasena.html">Cambiar contraseña</a>
</body>
</html>
