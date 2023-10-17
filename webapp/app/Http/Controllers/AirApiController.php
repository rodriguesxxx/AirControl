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

    public function isActive(Request $request){

        $id = $request->query('id');
        
        try{

            $query = DB::select("SELECT \"isActive\" FROM air_controls WHERE id = ?", [$id]);
            $airControl = AirUtil::thereIsAir($query) ? $query[0] : null;
            
            if( $airControl->isActive ){
                return response()->json( true, 200);
            } else{
                return response()->json( false, 200);
            }

        } catch(Exception $e){
            return response()->json("Air conditioning does not exist", 404);
        }
    }
    
    public function activeAir(Request $request){

        $id = $request->query('id');

        $temp = ( $request->query('temp') != null || $request->query('temp') < 16 ) ? $request->query('temp') : 18;

        try{
            $query = DB::update("UPDATE air_controls SET \"isActive\" = 1, temp = ? WHERE id = ?;", [$temp, $id]);   
            
            if($query){
                return response()->json("The air conditioning will be turned on soon", 201);
            } else{
                return response()->json("Air conditioning does not exist", 404);
            }
        } catch(Exception $e) {
            return response()->json("Internal Server Error", 500);
        }
    }  

    public function disableAir(Request $request){

        $id = $request->query('id');

        try{
            $query = DB::update("UPDATE air_controls SET \"isActive\" = 0 WHERE id = ?;", [$id]);   
            
            if($query){
                return response()->json("The air conditioning will be deactivated soon", 201);
            } else{
                return response()->json("Air conditioning does not exist", 404);
            }
        } catch(Exception $e) {
            return response()->json("Internal Server Error", 500);
        }
    } 

    public function ping(){
        return response()->json( [
            "pong" => "is alive"
        ] , 200);

    }
}
