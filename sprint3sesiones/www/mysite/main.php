<?php
	$db = mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
?>
<html>
<head>
<style>
table, td,th{
border: 1px solid black;
	border-collapse: collapse;
}</style>
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
		echo '<tr>';
		echo '<td>';
		echo '<a href="/detail.php?id='.$row["id"].'">'.$row["id"].'</a>';
		echo '</td>';
		echo '<td>';
		echo $row["nombre"];
		echo '</td>';
		echo '<td>';
		echo '<img src="'.$row["url_imagen"];
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
</body>
</html>
