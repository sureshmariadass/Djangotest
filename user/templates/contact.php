<?php
$con=mysqli_connect("localhost","root","","contact");
if(!$con)
{
	echo"Not Connected";
}
if(!mysqli_select_db($con,'contact'))
{
	echo"Db connection failed";
}
$Name=$_POST('cname');
$Mail=$_POST('c_mail');
$Subject=$_POST("c_sub");
$Message=$_POST('c_msg');
$sql="INSERT INTO form_c(Name,E-Mail,Subject,Message) VALUES ($Name,$Mail,$Subject,$Message)";

if(mysqli_query($con,$sql))
{
	echo 'Not Inserted';
}
else
{
	echo 'Inserted';
}
mysqli_close();
header("refersh:1; url=index.html");
?>