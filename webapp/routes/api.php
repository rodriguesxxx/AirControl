<?php

use App\Http\Controllers\AirApiController;
use Illuminate\Support\Facades\Route;
use Illuminate\Http\Request;



Route::post('/add', [AirApiController::class, 'addAirControl']);

Route::get('/isActive', [AirApiController::class, 'isActive']); //exemple: /isActive?id=INFO22

Route::put('/active', [AirApiController::class, 'activeAir']); //exemple: /activate?id=INFO22&temp=22

Route::put('/disable', [AirApiController::class, 'disableAir']); //exemple: /disable?id=INFO22


Route::get('/ping', [AirApiController::class, 'ping']);
