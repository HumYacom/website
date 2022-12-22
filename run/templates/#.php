<?php
   if(isset($_POST['submit'])){
    $ID=$_POST['no'];
    $Products_name=$_POST['รายการสินค้า'];
    $Size=$_POST['ขนาดบรรจุ'];
    $quantity=$_POST['จำนวน'];
    $unit_price=$_POST['ราคาต่อหน่วย'];

    $host = 'localhost';
    $user = 'root';
    $pass = '';
    $dbname = "table";

    $conn = mysqli_connect($host, $user, $pass, $dbname);
    
    $sql = "INSERT INTO calculate(no,รายการสินค้า, ขนาดบรรจุ, จำนวน, ราคาต่อหน่วย) values ($ID,$Products_name,$Size,$quantity,$unit_price)";
    mysqli_query($conn,$sql);
   }
?>