<?php

require_once 'vendor/autoload.php';

use MaxMind\Db\Reader;

$reader = new Reader('path/to/GeoLite2-City.mmdb');

$ip = '';
$record = $reader->get($ip);

print($record['country']['name'] . "\n"); // 'United States'
print($record['subdivisions'][0]['name'] . "\n"); // 'California'
print($record['city']['name'] . "\n"); // 'Mountain View'
print($record['postal']['code'] . "\n"); // '94043'
print($record['location']['latitude'] . "\n"); // 37.38600
print($record['location']['longitude'] . "\n"); // -122.08380

$reader->close();

?>
