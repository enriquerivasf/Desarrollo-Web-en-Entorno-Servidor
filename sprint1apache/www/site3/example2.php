<html>
	<body>
		<h1>Pagina de bienvenida</h1>
		<?php
			function dar_bienvenida($nombre) {
				echo "Bienvenido/a, " . $nombre . "!";
			}

			dar_bienvenida("Robert Downey Jr");
		?>
	</body>
</html>
