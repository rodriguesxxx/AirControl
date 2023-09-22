<?php

use App\Http\Controllers\AirApiController;
use Illuminate\Support\Facades\Route;
use Illuminate\Http\Request;


Route::get('/isActive/{id}', [AirApiController::class, 'isActive']);

Route::post('/active', [AirApiController::class, 'active']);

Route::get('/ping', [AirApiController::class, 'ping']);
