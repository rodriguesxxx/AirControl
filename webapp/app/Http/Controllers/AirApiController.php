<?php

namespace App\Http\Controllers;

use App\Models\AirControl;
use Illuminate\Http\Request;

class AirApiController extends Controller
{

    public function isActive($id){
        return response()->json(
            [
                "id" => $id,
                "isActive" => "true",
	            "disableThem" => "120",
	            "temp" => "18"

            ], 201);
    }

    public function active(Request $requestBody){
        $data = [
            "id" => $requestBody->id,
            "isActive" => 0, //padrao: false
	        "disableThem" => 280, //padrao: 3h 40m
	        "temp" => 21 //padrao: 21 graus
        ];

        $air_control = new AirControl();
        
        $air_control->id = $data["id"];
        $air_control->isActive = $data["isActive"];
        $air_control->disableThem = $data["disableThem"];
        $air_control->temp = $data["temp"];
        
        $air_control->save();

        return response()->json(
            $data, 201);
    }


    public function ping(){
        return response()->json( [
            "pong" => "is alive"
        ] , 201);

    }
}
