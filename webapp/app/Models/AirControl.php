<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class AirControl extends Model
{
    protected $table = 'air_controls';

    protected $fillable = ['id', 'isActive', 'disableThem', 'temp'];
}