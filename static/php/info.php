<?php

$host=""; // Host name
$username=""; // Mysql username
$password=""; // Mysql password
$db_name=""; // Database name
$tbl_name=""; // Table name

// Connect to server and select database.
mysql_connect("$host", "$username", "$password")or die("cannot connect");
mysql_select_db("$db_name")or die("cannot select DB");

// Get values from form
$name=$_POST['fname'];
$lastname=$_POST['lname'];
$email=$_POST['email'];
$occupation=$_POST['occupation'];
$add1=$_POST['add1']
$add2=$_POST['add2']
$zip=$_POST['zip']
$city=$_POST['city']
$state=$_POST['state']
$phone=$_POST['phone']
$denomination=$_POST['denomination']
$studies=$_POST['studies']
$amount=$_POST['amount']
// Insert data into mysql
$sql="INSERT INTO $donor_info(name, lastname, email, occupation, add1, add2, zip, state, phone)VALUES('$name', '$lastname', '$email', '$occupation', '$add1', '$add2', '$zip', '$city', '$state', '$phone', '$denomination', '$studies', '$amount' )";
$result=mysql_query($sql);

// if successfully insert data into database, displays message "Successful".
if($result){
echo "Successful";
echo "<BR>";
echo "<a href='insert.php'>Back to main page</a>";
}
else {
echo "ERROR";
}
?>

<?php
// close connection
mysql_close();