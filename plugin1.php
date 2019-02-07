<?php
/*
Plugin Name: Test Plugin
Plugin URI: https://calebaren.github.io/
Description: Testing plugin to access GSheets
Version: 1.0
Author: calebaren
Author URI: http://calebaren.github.io
License: GPLv2 or later
*/
function sheet_value_shortcode($atts) {
    $API = 'AIzaSyDxUjh2yTBudVqBSSVkon_ROypXEfmYWnw';
    $google_spreadsheet_ID = '12ieimF4voBMBUZ-7y_KP6BHR_O-87cKeAGA0fiLW4m0';
    $api_key = esc_attr( $API);

    $location = $atts['location'];

    $get_cell = new WP_Http();
    $cell_url = "https://sheets.googleapis.com/v4/spreadsheets/$google_spreadsheet_ID/values/$location?&key=$api_key";	
    $cell_response = $get_cell -> get( $cell_url);
    $json_body = json_decode($cell_response['body'],true);	
    $cell_value = $json_body['values'][0][0];
    return $cell_value;
}
add_shortcode('get_sheet_value', 'sheet_value_shortcode');