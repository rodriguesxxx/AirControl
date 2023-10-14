<?php

namespace App\Utils;

class AirUtil{
    public static function thereIsAir($query){
        if(count($query) > 0){
            return true;
        }
        return false;
    }
}