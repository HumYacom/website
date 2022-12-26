<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "table";

try {
  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $sql = "INSERT INTO list_products(ID, name_products, size, quantity) 
  VALUES ('$ID','$name_products','$size','$quantity')";
  
  if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $ID = $_POST['ID'];
    $name_products = $_POST['name_products'];
    $size = $_POST['size'];
    $quantity = $_POST['quantity'];
  }
  // use exec() because no results are returned
  $conn->exec($sql);
  echo "New record created successfully";
} catch(PDOException $e) {
  echo $sql . "<br>" . $e->getMessage();
}

$conn = null;
?>
