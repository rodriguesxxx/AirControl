<?php

namespace App\Http\Controllers;

use App\Models\AirControl;
use Exception;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use PDOException;

class AirApiController extends Controller
{

    public function isActive($id){

        $airControl = DB::select("SELECT * FROM air_controls WHERE id = ?", [$id]);
        
        if($airControl){
            return response()->json( $airControl, 201);
        } 

        return response()->json( $airControl, 404);

    }

    public function addAirControl(Request $requestBody){

        $airControl = new AirControl();
        
        $airControl->id = $requestBody->id;
        $airControl->isActive = 0;
        $airControl->disableThem = 280;
        $airControl->temp = 18;

        try{
            $airControl->save();
            
        } catch(PDOException $e){
            return $e;
        }
        
    }


    public function ping(){
        return response()->json( [
            "pong" => "is alive"
        ] , 201);

    }
}
