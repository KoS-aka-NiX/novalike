<?php
header('Content-Type: application/json; charset=utf-8');

echo json_encode([
    'name' => 'NovaLike',
    'status' => 'online',
    'timestamp' => date(DATE_ATOM)
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
