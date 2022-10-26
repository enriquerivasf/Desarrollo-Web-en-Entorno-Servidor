<?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
    
    session_start();
$contrasenaIntroducida= $_POST['contrasena'];
	echo $_SESSION['user_id'];
	echo "$contrasenaIntroducida";
    if (empty($_SESSION['user_id'])) {
        echo "Error: es necesario tener sesión iniciada";
    } else {
       
        $query1 = "UPDATE tUsuarios SET contraseña='".$contrasenaIntroducida."' WHERE id=".$_SESSION['user_id'];
        $result1 = mysqli_query($db, $query1) or die('Error al actualizar la contraseña');

      
        if ($result1) {
            echo "<h1>Contraseña actualizada</h1>";
            echo "<a href='main.php'>Volver a la página principal</a>";
        } else {
            echo "<h1>Error al actualizar contraseña</h1>";
        }
    }
?>
