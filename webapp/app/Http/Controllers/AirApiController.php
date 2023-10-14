<?php

namespace App\Http\Controllers;

use App\Models\AirControl;
use Exception;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use PDOException;
use App\Utils\AirUtil;

class AirApiController extends Controller
{

    

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

    public function isActive($id){

        $query = DB::select("SELECT * FROM air_controls WHERE id = ?", [$id]);
        $airControl = AirUtil::thereIsAir($query) ? $query[0] : null;

        try{
            if( $airControl->isActive ){
                return response()->json( $airControl, 200);
            } else{
                return response()->json("The air conditioning is deactivated", 202);
            }
        } catch(Exception $e){
            return response()->json("Air conditioning does not exist", 404);
        }
    }
    
    public function activeAir($id, $temp = 18){
        
    }
    
    




    public function ping(){
        return response()->json( [
            "pong" => "is alive"
        ] , 201);

    }
}
