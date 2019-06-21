<?php
namespace ccxt;
include_once (__DIR__.'/../Exchange.php');

// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -----------------------------------------------------------------------------

$exchange = new \ccxt\Exchange (array (
    'id' => 'regirock',
));

// ----------------------------------------------------------------------------

assert ($exchange->iso8601 (514862627000) === '1986-04-26T01:23:47.000Z');
assert ($exchange->iso8601 (514862627559) === '1986-04-26T01:23:47.559Z');
assert ($exchange->iso8601 (514862627062) === '1986-04-26T01:23:47.062Z');

assert ($exchange->iso8601 (0) === '1970-01-01T00:00:00.000Z');

assert ($exchange->iso8601 (-1) === null);
assert ($exchange->iso8601 () === null);
assert ($exchange->iso8601 (null) === null);
assert ($exchange->iso8601 ('') === null);
assert ($exchange->iso8601 ('a') === null);
assert ($exchange->iso8601 (array()) === null);

// ----------------------------------------------------------------------------

assert ($exchange->parse8601 ('1986-04-26T01:23:47.000Z') === 514862627000);
assert ($exchange->parse8601 ('1986-04-26T01:23:47.559Z') === 514862627559);
assert ($exchange->parse8601 ('1986-04-26T01:23:47.062Z') === 514862627062);

assert ($exchange->parse8601 ('1977-13-13T00:00:00.000Z') === null);
assert ($exchange->parse8601 ('1986-04-26T25:71:47.000Z') === null);

assert ($exchange->parse8601 ('3333') === null);
assert ($exchange->parse8601 ('Sr90') === null);
assert ($exchange->parse8601 ('') === null);
assert ($exchange->parse8601 () === null);
assert ($exchange->parse8601 (null) === null);
assert ($exchange->parse8601 (array()) === null);
assert ($exchange->parse8601 (33) === null);

// ----------------------------------------------------------------------------

assert ($exchange->parse_date('1986-04-26 00:00:00') === 514857600000);
assert ($exchange->parse_date('1986-04-26T01:23:47.000Z') === 514862627000);
assert ($exchange->parse_date('1986-13-13 00:00:00') === null);
