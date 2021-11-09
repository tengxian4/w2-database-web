
<?php
class MyDB extends SQLite3
{
	function __construct()
	{
		$this->open('Students.db');
	}
}

$db = new MyDB();


if(!$db)
{
    echo $db->lastErrorMsg();
}

$result = $db->query('SELECT result FROM Grade');

var_dump($result->fetchArray());



?>