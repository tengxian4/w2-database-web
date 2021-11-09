<?php 
	{

	class MyDB extends SQLite3
	{
		function __construct()
		{
			$this->open('../student-dashboard-master/Students.db');
		}
	}

	$db = new MyDB();
  
     
    /* 
    The Above code can be in a different file, then you can place include'filename.php'; instead. 
    */ 
     
    //Lets search the databse for the user name and password 
    //Choose some sort of password encryption, I choose sha256 
    //Password function (Not In all versions of MySQL). 
    $usr = 1;//$_POST['username']; 
    $pas = "123";//$_POST['password']; 
	$sql = $db->query("SELECT * FROM Student WHERE Id='$usr' AND Password='$pas';");
    

		
		if($sql != NULL){ 
			$row = $sql->fetchArray(); 
			session_start(); 
			$_SESSION['name'] = $row['name']; 		
			$_SESSION['logged'] = TRUE; 
			header("Location: ../student-dashboard-master/index.html"); // Modify to go to the page you would like 
			
			exit; 
		}else{ 
			header("Location: login_page.php"); 
			exit; 
			}
		} 
		?> 